import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter

fm.fontManager.addfont("TaipeiSansTCBeta-Regular.ttf")
matplotlib.rc("font", family="Taipei Sans TC Beta")

def prepare_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """準備並清理資料"""
      
    # 讀取中學畢業生出路資料
    graduates_data_1: pd.DataFrame = pd.read_csv(
        "臺北市中等學校畢業生出路(57學年度至102學年度)時間數列統計資料.csv",
        encoding="utf-8",
    )
    print(f"""臺北市中等學校畢業生出路(57學年度至102學年度)
    {graduates_data_1.head()}
    """)

    graduates_data_2: pd.DataFrame = pd.read_csv(
        "臺北市中等學校畢業生出路(103學年度以後).csv",
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
    graduates_data_1_only_senior_high.drop(columns=["學制別"], inplace=True)
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
    print(f"""臺北市中等學校畢業生出路(全)
    {graduates_data_full}
    """)
    
    # 讀取每人所得資料
    income_data: pd.DataFrame = pd.read_csv(
        "臺北市所得收入者每人所得－行業別按年別.csv", encoding="big5"
    )
    income_data.replace("-", np.nan, inplace=True)
    income_data.dropna(subset=["[三]可支配所得[NT]"], inplace=True)
    print(f"""臺北市所得收入者每人所得－行業別按年別
    {income_data.head()}
    """)
    
    # 讀取勞動力資料
    labor_force_data: pd.DataFrame = pd.read_csv(
        "臺北市勞動力及就業按半年別時間數列統計資料.csv", encoding="utf-8"
    )
    print(f"""臺北市勞動力及就業按半年別時間數列統計資料
    {labor_force_data.head()}
    """)


    return graduates_data_full, income_data, labor_force_data



graduates_data, income_data, labor_force_data = prepare_data()



# 圖一：畢業生出路（升學 vs 就業 vs 其他）長期趨勢圖
def plot_graduates_trends(graduates_data: pd.DataFrame) -> None:
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

plot_graduates_trends(graduates_data)

# 圖二：勞動力（參與率、就業率、失業率）變動圖
def plot_labor_force_trends(labor_force_data: pd.DataFrame) -> None:
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

plot_labor_force_trends(labor_force_data)


# 圖三：全產業可支配所得變化趨勢圖
def plot_industry_income_trends(income_data: pd.DataFrame) -> None:
    """繪製全產業可支配所得變化趨勢圖"""
    # FIXME
    def thousands_formatter(x, pos):
        """將數值格式化為千元單位"""
        return f"{int(x / 1000)}"


    time_periods: pd.Series = income_data["年別"]
    industry: pd.Series = income_data["行業"]
    disposable_income: pd.Series = income_data["[三]可支配所得[NT]"].apply(pd.to_numeric)

    fig, ax = plt.subplots(figsize=(16, 8))
    for ind in industry.unique():
        ind_data = income_data[income_data["行業"] == ind]
        ax.plot(
            ind_data["年別"],
            ind_data["[三]可支配所得[NT]"],
            label=ind,
            marker="o",
            markersize=4,
            linewidth=1.5,
        )

    ax.set_xlabel("年別", fontsize=12)
    ax.set_ylabel("可支配所得 (千元)", fontsize=12)
    ax.set_title("臺北市全產業可支配所得變化趨勢圖", fontsize=14, pad=15)
    plt.xticks(rotation=45, ha="right")
    ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    # 調整圖例：放在圖表外右側
    ax.legend(
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        fontsize=9,
        ncol=1,
        frameon=True,
        shadow=True,
    )
    ax.grid(True, alpha=0.3, linestyle="--")

    # 調整子圖位置，給Y軸標籤和圖例留出更多空間
    plt.subplots_adjust(left=0.08, right=0.85, top=0.95, bottom=0.1)
    plt.show()

plot_industry_income_trends(income_data)

# # 圖四：產業別所得差距（箱型圖或長條圖）
# # FIXME
# # ---
# # 產業別可支配所得差距分析：
# # 1) 箱型圖 (各產業跨年度分布)
# # 2) 長條圖 (比較最早、中間、最近三個年度的產業薪資)

# # 清理資料並轉成數值
# plot_income_df = income_data.copy()
# plot_income_df["年別"] = plot_income_df["年別"].astype(str)
# plot_income_df["[三]可支配所得[NT]"] = pd.to_numeric(
#     plot_income_df["[三]可支配所得[NT]"], errors="coerce"
# )
# plot_income_df.dropna(subset=["[三]可支配所得[NT]"], inplace=True)

# # 選擇前 N 個平均可支配所得最高的產業，避免圖形過於擁擠
# top_n = 8
# industry_means = (
#     plot_income_df.groupby("行業")["[三]可支配所得[NT]"].mean().sort_values(ascending=False)
# )
# top_industries = industry_means.head(top_n).index.tolist()
# print(f"選取前 {top_n} 名產業進行繪圖：{top_industries}")

# # 箱型圖：每個產業跨年度的分布（反映產業內的年度差異）
# plt.figure(figsize=(12, 6))
# boxplot_data = [
#     plot_income_df[plot_income_df["行業"] == ind]["[三]可支配所得[NT]"].values
#     for ind in top_industries
# ]
# plt.boxplot(boxplot_data, labels=top_industries, showmeans=True)
# plt.ylabel("可支配所得 (千元)")
# plt.title(f"箱型圖：前 {top_n} 行業可支配所得分布（跨年度）")
# plt.xticks(rotation=45, ha="right")
# ax = plt.gca()
# ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
# plt.tight_layout()
# plt.show()

# # 長條圖：選三個代表性年度（最早、中位、最近）進行橫向年度比較
# years_sorted = sorted(plot_income_df["年別"].unique(), key=lambda x: int(x))
# selected_years = [years_sorted[0], years_sorted[len(years_sorted) // 2], years_sorted[-1]]
# print(f"選取年度進行比較：{selected_years}")

# bar_df = plot_income_df[
#     (plot_income_df["行業"].isin(top_industries)) & (plot_income_df["年別"].isin(selected_years))
# ]
# pivot = bar_df.pivot_table(
#     index="行業", columns="年別", values="[三]可支配所得[NT]"
# )
# # 確保順序固定為 top_industries
# pivot = pivot.reindex(top_industries)

# pivot.plot(kind="bar", figsize=(14, 7))
# plt.ylabel("可支配所得 (千元)")
# plt.title("比較：不同年度（最早、中位、最近）各產業可支配所得")
# plt.xticks(rotation=45, ha="right")
# ax = plt.gca()
# ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
# plt.legend(title="年別")
# plt.tight_layout()
# plt.show()

# # 額外提示：若希望比較所有年度或指定其他產業，可調整 top_n 或 selected_years 參數。


# 圖五：青年就業比例 vs 整體失業率
# 雙軸折線圖（使用年平均失業率，與高中職畢業生就業比例比較）
def plot_graduates_employment_vs_unemployment(graduates_data, labor_force_data: pd.DataFrame) -> None:
    """繪製青年就業比例 vs 整體失業率雙軸圖"""
    
    total_graduates: pd.Series = graduates_data["總計[人]"]
    graduates_employment_percentage: pd.Series = graduates_data["就業/合計[人]"] / total_graduates * 100
    
    plt.figure(figsize=(14, 6))
    # 計算年（數字）欄位方便合併
    labor_force_data_year = labor_force_data.copy()
    labor_force_data_year["year"] = labor_force_data_year["統計期"].str.extract(r"(\d{2,3})").astype(int)
    # 年平均失業率
    unemployment_yearly = (
        labor_force_data_year.groupby("year")["失業率[%]"].apply(lambda s: s.astype(float).mean()).reset_index()
    )
    # 畢業生就業比例（對應學年度）
    # todo: 學年度使與年度的合併這樣好嗎？
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

plot_graduates_employment_vs_unemployment(
    graduates_data, 
    labor_force_data
)