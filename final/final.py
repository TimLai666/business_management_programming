import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter

fm.fontManager.addfont("TaipeiSansTCBeta-Regular.ttf")
matplotlib.rc("font", family="Taipei Sans TC Beta")

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

# 圖一：畢業生出路（升學 vs 就業 vs 其他）長期趨勢圖
academic_years: pd.Series = graduates_data_full["學年度"]
total_graduates: pd.Series = graduates_data_full["總計[人]"]
further_education: pd.Series = (
    graduates_data_full["升學/合計[人]"] / total_graduates * 100
)
employment: pd.Series = graduates_data_full["就業/合計[人]"] / total_graduates * 100
others: pd.Series = (
    (graduates_data_full["其他[人]"] + graduates_data_full["閒居[人]"])
    / total_graduates
    * 100
)
plt.figure(figsize=(12, 6))
plt.plot(academic_years, further_education, label="升學", marker="o")
plt.plot(academic_years, employment, label="就業", marker="^")
plt.plot(academic_years, others, label="其他", marker="s")
plt.xlabel("學年度")
plt.xticks(range(min(academic_years), max(academic_years) + 1, 2), rotation=45)
plt.ylabel("百分比(%)")
plt.title("臺北市高中職畢業生出路趨勢圖")
plt.legend()
plt.show()

# 圖二：勞動力（參與率、就業率、失業率）變動圖
time_periods: pd.Series = labor_force_data["統計期"]
labor_participation_rate: pd.Series = labor_force_data["勞動力參與率[%]"]
unemployment_rate: pd.Series = labor_force_data["失業率[%]"]
plt.figure(figsize=(14, 6))
plt.suptitle("臺北市勞動力變動圖", fontsize=14, y=0.98)

plt.subplot(1, 2, 1)
plt.plot(time_periods, labor_participation_rate, label="勞動參與率", marker="o")
plt.ylabel("百分比(%)")
plt.xlabel("統計期")
plt.ylim(50, 60)  # 設定Y軸範圍更貼近數據
# 只顯示部分X軸標籤，避免重疊
x_ticks = range(0, len(time_periods), max(1, len(time_periods) // 10))
plt.xticks(x_ticks, [time_periods.iloc[i] for i in x_ticks], rotation=45, ha="right")
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(time_periods, unemployment_rate, label="失業率", marker="^")
plt.ylabel("百分比(%)")
plt.xlabel("統計期")
plt.ylim(3, 6.5)  # 設定Y軸範圍更貼近數據
# 只顯示部分X軸標籤，避免重疊
plt.xticks(x_ticks, [time_periods.iloc[i] for i in x_ticks], rotation=45, ha="right")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# 圖三：全產業可支配所得變化趨勢圖
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
