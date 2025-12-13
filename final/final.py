import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib

fm.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
matplotlib.rc('font', family='Taipei Sans TC Beta')

# 讀取中學畢業生出路資料
graduates_data_1: pd.DataFrame = pd.read_csv(
    "臺北市中等學校畢業生出路(57學年度至102學年度)時間數列統計資料.csv",
    encoding="utf-8",)
print(f"""臺北市中等學校畢業生出路(57學年度至102學年度)
{graduates_data_1.head()}
""")

graduates_data_2: pd.DataFrame = pd.read_csv(
    "臺北市中等學校畢業生出路(103學年度以後).csv",
    encoding="utf-8",)
print(f"""臺北市中等學校畢業生出路(103學年度以後)
{graduates_data_2.head()}
""")

graduates_data_1_only_senior_high: pd.DataFrame = graduates_data_1[
    (graduates_data_1["學制別"] == "高中(職)") | (graduates_data_1["學制別"] == "高級中學")|(graduates_data_1["學制別"] == "高級職業學校")]
graduates_data_1_only_senior_high.drop(columns=["學制別"], inplace=True)
graduates_data_1_only_senior_high = graduates_data_1_only_senior_high.groupby("統計期").sum(numeric_only=True).reset_index()
print(f"""臺北市中等學校畢業生出路(57學年度至102學年度) - 只含高中職
{graduates_data_1_only_senior_high}
""")

graduates_data_full: pd.DataFrame = pd.concat(
    [graduates_data_1_only_senior_high, graduates_data_2])
print(f"""臺北市中等學校畢業生出路(全)
{graduates_data_full}
""")

# 讀取每人所得資料
income_data: pd.DataFrame = pd.read_csv(
    "臺北市所得收入者每人所得－行業別按年別.csv",
    encoding="big5")
print(f"""臺北市所得收入者每人所得－行業別按年別
{income_data.head()}
""")

# 讀取勞動力資料
labor_force_data: pd.DataFrame = pd.read_csv(
    "臺北市勞動力及就業按半年別時間數列統計資料.csv",
    encoding="utf-8")
print(f"""臺北市勞動力及就業按半年別時間數列統計資料
{labor_force_data.head()}
""")

# 圖一：畢業生出路（升學 vs 就業 vs 其他）長期趨勢圖
academic_years: pd.Series = graduates_data_full["統計期"]
further_education: pd.Series = graduates_data_full["升學/合計[人]"]
employment: pd.Series = graduates_data_full["就業/合計[人]"]
others: pd.Series = graduates_data_full["其他[人]"]+graduates_data_full["閒居[人]"]
plt.figure(figsize=(12, 6))
plt.plot(academic_years, further_education, label="升學", marker='o')
plt.plot(academic_years, employment, label="就業", marker='o')
plt.plot(academic_years, others, label="其他", marker='o')
plt.xlabel("學年度")
plt.ylabel("人數")
plt.title("臺北市中等學校畢業生出路趨勢圖")
plt.legend()
plt.show()
