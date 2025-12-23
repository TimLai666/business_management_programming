import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import io

fm.fontManager.addfont("TaipeiSansTCBeta-Regular.ttf")
matplotlib.rc("font", family="Taipei Sans TC Beta")

def prepare_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """準備並清理資料"""
      
    # 讀取中學畢業生出路資料
    res: requests.Response = requests.get(
        url="https://tsis.dbas.gov.taipei/statis/webMain.aspx?sys=220&ymf=5700&kind=21&type=0&funid=a05009501&cycle=4&outmode=12&compmode=0&outkind=3&deflst=2&nzo=1", 
        verify=False
    )
    graduates_data_1: pd.DataFrame = pd.read_csv(
        io.StringIO(res.content.decode("utf-8")),
        encoding="utf-8",
    )
    print(f"""臺北市中等學校畢業生出路(57學年度至102學年度)
    {graduates_data_1.head()}
    """)

    res: requests.Response = requests.get(
        url="https://tsis.dbas.gov.taipei/statis/webMain.aspx?sys=220&ymf=5700&kind=21&type=0&funid=a05009503&cycle=4&outmode=12&compmode=0&outkind=3&deflst=2&nzo=1", 
        verify=False
    )
    graduates_data_2: pd.DataFrame = pd.read_csv(
        io.StringIO(res.content.decode("utf-8")),
        encoding="utf-8",
    )
    print(f"""臺北市中等學校畢業生出路(103學年度以後)
    {graduates_data_2.head()}
    """)

    graduates_data_1_only_senior_high: pd.DataFrame = graduates_data_1[
        (graduates_data_1["學制別"] == "高中(職)")
        | (graduates_data_1["學制別"] == "高級中學")
        | (graduates_data_1["學制別"] == "高級職業學校")
    ]
    graduates_data_1_only_senior_high = graduates_data_1_only_senior_high.drop(columns=["學制別"])
    graduates_data_1_only_senior_high = (
        graduates_data_1_only_senior_high.groupby("統計期")
        .sum(numeric_only=True)
        .reset_index()
    )
    print(f"""臺北市中等學校畢業生出路(57學年度至102學年度) - 只含高中職
    {graduates_data_1_only_senior_high}
    """)

    graduates_data_full: pd.DataFrame = pd.concat(
        [graduates_data_1_only_senior_high, graduates_data_2]
    )
    graduates_data_full["學年度"] = graduates_data_full["統計期"].apply(
        lambda x: int(x.replace("學年", ""))
    )
    graduates_data_full.sort_values(by="學年度", inplace=True)
    graduates_data_full.fillna(0, inplace=True)
    print(f"""臺北市中等學校畢業生出路(全)
    {graduates_data_full}
    """)
    
    # 讀取每人所得資料
    res: requests.Response = requests.get(
        url="https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=90194984-ed88-492e-bf24-9c47778239cf", 
        verify=False
    )
    income_data: pd.DataFrame = pd.read_csv(
        io.StringIO(res.content.decode("big5")), encoding="big5"
    )
    income_data.replace("-", np.nan, inplace=True)
    income_data.dropna(subset=["[三]可支配所得[NT]"], inplace=True)
    # 清理 1.受僱人員報酬[NT]：去掉千位分隔符或其他非數字字元，再轉為數值
    income_data["1.受僱人員報酬[NT]"] = (
        income_data["1.受僱人員報酬[NT]"].astype(str).str.replace(r"[^\d\.\-]", "", regex=True)
    )
    income_data["1.受僱人員報酬[NT]"] = pd.to_numeric(
        income_data["1.受僱人員報酬[NT]"], errors="coerce"
    ).astype(float)
    income_data["行業"] = income_data["行業"].str.strip()
    # 檢查 113 年農林漁牧業是否正確載入與轉換
    mask_af = (
        income_data["年別"].astype(str).str.contains("113")
        & income_data["行業"].str.contains("農林", na=False)
    )
    if mask_af.any():
        print("113 年農林漁牧業資料（年別, 行業, 1.受僱人員報酬[NT]）:\n", income_data.loc[mask_af, ["年別","行業","1.受僱人員報酬[NT]"]])
    print(f"""臺北市所得收入者每人所得－行業別按年別
    {income_data.head()}
    """)
    
    # 讀取勞動力資料
    res: requests.Response = requests.get(
        url="https://tsis.dbas.gov.taipei/statis/webMain.aspx?sys=220&ymf=9400&kind=21&type=0&funid=a04000901&cycle=3&outmode=12&compmode=0&outkind=1&deflst=2&nzo=1", 
        verify=False
    )
    labor_force_data: pd.DataFrame = pd.read_csv(
        io.StringIO(res.content.decode("utf-8")), encoding="utf-8"
    )
    print(f"""臺北市勞動力及就業按半年別時間數列統計資料
    {labor_force_data.head()}
    """)


    return graduates_data_full, income_data, labor_force_data



graduates_data, income_data, labor_force_data = prepare_data()



# 圖一：畢業生出路（升學 vs 就業 vs 其他）長期趨勢圖
def plot1_graduates_trends(graduates_data: pd.DataFrame) -> None:
    """繪製畢業生出路趨勢圖"""
    academic_years: pd.Series = graduates_data["學年度"]
    total_graduates: pd.Series = graduates_data["總計[人]"]
    further_education: pd.Series = (
        graduates_data["升學/合計[人]"] / total_graduates * 100
    )
    graduates_employment_percentage: pd.Series = graduates_data["就業/合計[人]"] / total_graduates * 100
    others: pd.Series = (
        (graduates_data["其他[人]"] + graduates_data["閒居[人]"])
        / total_graduates
        * 100
    )
    plt.figure(figsize=(12, 6))
    plt.plot(academic_years, further_education, label="升學", marker="o")
    plt.plot(academic_years, graduates_employment_percentage, label="就業", marker="^")
    plt.plot(academic_years, others, label="其他", marker="s")
    plt.xlabel("學年度")
    plt.xticks(range(min(academic_years), max(academic_years) + 1, 2), rotation=45)
    plt.ylabel("百分比(%)")
    plt.title("臺北市高中職畢業生出路趨勢圖")
    plt.legend()
    plt.show()

plot1_graduates_trends(graduates_data)

# 圖二：勞動力（參與率、就業率、失業率）變動圖
def plot2_labor_force_trends(labor_force_data: pd.DataFrame) -> None:
    """繪製勞動力變動圖"""
    time_periods: pd.Series = labor_force_data["統計期"]
    labor_participation_rate: pd.Series = labor_force_data["勞動力參與率[%]"].astype(float)
    unemployment_rate: pd.Series = labor_force_data["失業率[%]"].astype(float)
    labor_force: pd.Series = labor_force_data["勞動力人口/合計[千人]"].astype(float)
    total_employed_population: pd.Series = labor_force_data["勞動力人口/就業者[千人]"].astype(float)
    employment_rate: pd.Series = (
        total_employed_population / labor_force * 100
    )
    plt.figure(figsize=(14, 6))
    plt.suptitle("臺北市勞動力變動圖", fontsize=14, y=0.98)

    # 勞動參與率
    plt.subplot(2, 2, 1)
    plt.plot(time_periods, labor_participation_rate, label="勞動參與率", marker="o", color="blue")
    plt.ylabel("百分比(%)")
    plt.xlabel("統計期")
    plt.ylim(54, 60)  # 設定Y軸範圍更貼近數據
    # 只顯示部分X軸標籤，避免重疊
    x_ticks = range(0, len(time_periods), max(1, len(time_periods) // 10))
    plt.xticks(x_ticks, [time_periods.iloc[i] for i in x_ticks], rotation=45, ha="right")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # 失業率
    plt.subplot(2, 2, 2)
    plt.plot(time_periods, unemployment_rate, label="失業率", marker="^", color="red")
    plt.ylabel("百分比(%)")
    plt.xlabel("統計期")
    plt.ylim(3, 6.5)  # 設定Y軸範圍更貼近數據
    # 只顯示部分X軸標籤，避免重疊
    plt.xticks(x_ticks, [time_periods.iloc[i] for i in x_ticks], rotation=45, ha="right")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # 就業率
    plt.subplot(2, 1, 2)
    plt.plot(time_periods, employment_rate, label="就業率", marker="s", color="green")
    plt.ylabel("百分比(%)")
    plt.xlabel("統計期")
    plt.ylim(93, 98)  # 設定Y軸範
    # 只顯示部分X軸標籤，避免重疊
    plt.xticks(x_ticks, [time_periods.iloc[i] for i in x_ticks], rotation=45, ha="right")
    plt.legend()

    plt.tight_layout()
    plt.show()

plot2_labor_force_trends(labor_force_data)


# 圖三：全產業受僱人員報酬變化趨勢圖
def plot3_industry_income_trends(income_data: pd.DataFrame) -> None:
    """繪製全產業受僱人員報酬變化趨勢圖"""

    # 為避免 x（年別）與 y（產業資料列數）長度不一致，改用每個產業對應的年別作為 x
    # 擷取數字型的年（例如：'98年' -> 98, '100年' -> 100）以便排序與設定 xticks
    income_data["year"] = (
        income_data["年別"].astype(str).str[:-1].astype(int)
    )

    plt.figure(figsize=(14, 7))

    # 以 1.受僱人員報酬[NT] 做為 y 軸
    all_years: list = sorted(income_data["year"].unique())

    markers: list[str] = ["o", "^", "s", "D", "v", "*", "X", "<", ">"]
    for idx, ind in enumerate(income_data["行業"].unique()):
        ind_data: pd.DataFrame = income_data[income_data["行業"] == ind].copy()
        ind_data.sort_values("year", inplace=True)

        y: pd.Series = pd.to_numeric(ind_data["1.受僱人員報酬[NT]"], errors="coerce")
        x: pd.Series = ind_data["year"]

        # 若某產業全為缺值則跳過
        valid_mask: pd.Series[bool] = ~y.isna()
        if valid_mask.sum() == 0:
            continue

        # 轉換成千元以符合 Y 軸標籤 (千元)
        y_k: pd.Series = y / 1000.0

        plt.plot(
            x[valid_mask],
            y_k[valid_mask],
            label=ind,
            marker=markers[idx % len(markers)],
            markersize=4,
            linewidth=1.5,
        )

    plt.xlabel("民國年", fontsize=12)
    plt.ylabel("受僱人員報酬 (千元)", fontsize=12)
    plt.title("臺北市全產業受僱人員報酬變化趨勢圖", fontsize=14, pad=15)

    # 用整理過的數字年作為 xticks
    plt.xticks(all_years, rotation=45, ha="right")

    # 調整圖例：放在圖表外右側
    plt.legend(
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        fontsize=9,
        ncol=1,
        frameon=True,
        shadow=True,
    )
    plt.grid(True, alpha=0.3, linestyle="--")

    # 調整子圖位置，給Y軸標籤和圖例留出更多空間
    plt.subplots_adjust(left=0.08, right=0.8, top=0.85, bottom=0.1)
    plt.show()

plot3_industry_income_trends(income_data)

# # 圖四：產業別所得差距（長條圖）
def plot4_income_gap_by_industry(income_data: pd.DataFrame) -> None:
    """繪製產業別所得差距長條圖"""
    
    # 取最新年度資料
    latest_year: int = income_data["year"].max()
    latest_data: pd.DataFrame = income_data[income_data["year"] == latest_year]
    # 移除受僱人員報酬缺值，避免繪圖時出現高度為 0 的長條
    latest_data = latest_data.dropna(subset=["1.受僱人員報酬[NT]"])
    latest_data = latest_data.copy()
    lastest_income_k: pd.Series = latest_data["1.受僱人員報酬[NT]"] / 1000

    plt.figure(figsize=(12, 6))
    plt.bar(
        latest_data["行業"],
        lastest_income_k,
        color="skyblue",
    )
    plt.xlabel("行業", fontsize=12)
    plt.ylabel("受僱人員報酬 (千元)", fontsize=12)
    plt.title(f"臺北市各行業所得差距（{latest_year}年）", fontsize=14)
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

plot4_income_gap_by_industry(income_data)

# 圖五：青年就業比例 vs 整體失業率
# 雙軸折線圖（使用年平均失業率，與高中職畢業生就業比例比較）
def plot5_graduates_employment_vs_unemployment(graduates_data, labor_force_data: pd.DataFrame) -> None:
    """繪製青年就業比例 vs 整體失業率雙軸圖"""
    
    total_graduates: pd.Series = graduates_data["總計[人]"]
    graduates_employment_percentage: pd.Series = graduates_data["就業/合計[人]"] / total_graduates * 100
    
    plt.figure(figsize=(14, 6))
    # 計算年（數字）欄位方便合併
    labor_force_data_year = labor_force_data.copy()
    labor_force_data_year["year"] = labor_force_data_year["統計期"].str.extract(r"(\d+)")[0].astype(int)
    # 年平均失業率
    unemployment_yearly = (
        labor_force_data_year.groupby("year")["失業率[%]"].apply(lambda s: s.astype(float).mean()).reset_index()
    )
    # 畢業生就業比例（對應學年度）
    graduates_pct_df = pd.DataFrame({"year": graduates_data["學年度"], "graduates_employment_pct": graduates_employment_percentage.values})
    # 合併資料（只保留雙方皆有的年份）
    merged = pd.merge(unemployment_yearly, graduates_pct_df, on="year", how="inner").sort_values("year")
    
    # 畫雙軸圖
    ax1 = plt.gca()
    ax1.plot(merged["year"], merged["失業率[%]"], label="整體失業率（年平均）", marker="o", color="red")
    ax1.set_xlabel("民國年")
    ax1.set_ylabel("失業率 (%)", color="red")
    ax1.set_ylim(merged["失業率[%]"].min() - 0.5, merged["失業率[%]"].max() + 0.5)
    ax1.tick_params(axis="y", labelcolor="red")
    ax1.set_xticks(merged["year"])
    ax1.set_xticklabels(labels=merged["year"], rotation=45, ha="right")
    ax1.grid(True, alpha=0.3)
    
    ax2 = ax1.twinx()
    ax2.plot(merged["year"], merged["graduates_employment_pct"], label="高中職畢業生就業比例", marker="s", color="blue")
    ax2.set_ylabel("畢業生就業比例 (%)", color="blue")
    ax2.set_ylim(max(0, merged["graduates_employment_pct"].min() - 5), min(100, merged["graduates_employment_pct"].max() + 5))
    ax2.tick_params(axis="y", labelcolor="blue")
    
    # 合併圖例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
    plt.title("高中職畢業生就業比例 vs 整體失業率（年平均）")
    plt.tight_layout()
    plt.show()

plot5_graduates_employment_vs_unemployment(
    graduates_data, 
    labor_force_data
)

# 圖六：高中職畢業生就業產業別占比變化趨勢圖
def plot6_graduates_employment_industry_trends(graduates_data: pd.DataFrame) -> None:
    """繪製高中職畢業生就業產業別占比變化趨勢圖"""
    
    academic_years: pd.Series = graduates_data["學年度"]
    total_employed: pd.Series = graduates_data["就業/合計[人]"]
    
    農林漁牧業: pd.Series = (
        graduates_data["就業/農林漁牧狩獵業[人]"] +
        graduates_data["就業/農林漁牧業[人]"]
    )
    礦業及土石採取業: pd.Series = graduates_data["就業/礦業及土石採取業[人]"]
    製造業或營造業: pd.Series = (
        graduates_data["就業/製造業或營造業[人]"] +
        graduates_data["就業/製造業營建工程業[人]"]
    )
    水電燃氣業: pd.Series = (
        graduates_data["就業/水電燃氣業[人]"] + 
        graduates_data["就業/用水電力燃氣供應及污染整治業[人]"]
    )
    批發零售及餐飲業及金融保險不動產及租賃住宿業: pd.Series = (
        graduates_data["就業/批發零售及餐飲業[人]"] +
        graduates_data["就業/批發及零售業[人]"] +
        graduates_data["就業/金融保險不動產及租賃業[人]"] +
        graduates_data["就業/金融保險及不動產業[人]"]+
        graduates_data["就業/住宿及餐飲業[人]"]
    )
    運輸倉儲出版影音通信業: pd.Series = (
        graduates_data["就業/運輸倉儲通信業[人]"] +
        graduates_data["就業/運輸倉儲出版影音及資通訊業[人]"]
    )
    其它服務業: pd.Series = (
        graduates_data["就業/社會及個人服務業[人]"] + 
        graduates_data["就業/專業科學及技術服務業[人]"] +
        graduates_data["就業/藝術娛樂及休閒服務業[人]"]
    )
    其它: pd.Series = (
        graduates_data["就業/其他[人]"] +
        graduates_data["就業/公共行政及國防[人]"]
    )
    
    plt.figure(figsize=(12, 6))
    plt.plot(academic_years, 農林漁牧業 / total_employed * 100, label="農林漁牧業", marker="o")
    plt.plot(academic_years, 礦業及土石採取業 / total_employed * 100, label="礦業及土石採取業", marker="^")
    plt.plot(academic_years, 製造業或營造業 / total_employed * 100, label="製造業或營造業", marker="s")
    plt.plot(academic_years, 水電燃氣業 / total_employed * 100, label="水電燃氣業", marker="D")
    plt.plot(academic_years, 批發零售及餐飲業及金融保險不動產及租賃住宿業 / total_employed * 100, label="批發零售及餐飲業及金融保險不動產及租賃業", marker="v")
    plt.plot(academic_years, 運輸倉儲出版影音通信業 / total_employed * 100, label="運輸倉儲出版影音通信業", marker="*")
    plt.plot(academic_years, 其它服務業 / total_employed * 100, label="其它服務業", marker="X")
    plt.plot(academic_years, 其它 / total_employed * 100, label="其它", marker="<")
    plt.xlabel("學年度")
    plt.xticks(range(min(academic_years), max(academic_years) + 1, 2), rotation=45)
    plt.ylabel("百分比(%)")
    plt.title("臺北市高中職畢業生就業產業別占比變化趨勢圖")
    plt.legend()
    plt.show()

plot6_graduates_employment_industry_trends(graduates_data)