import pandas as pd

# 讀取中學畢業生出路資料
graduates_data_1: pd.DataFrame = pd.read_csv(
    "臺北市中等學校畢業生出路(57學年度至102學年度)時間數列統計資料.csv",
    encoding="utf-8",)
print(graduates_data_1.columns.values, "\n")

graduates_data_2: pd.DataFrame = pd.read_csv(
    "臺北市中等學校畢業生出路(103學年度以後).csv",
    encoding="utf-8",)
print(graduates_data_2.columns.values, "\n")

# 讀取每人所得資料
income_data: pd.DataFrame = pd.read_csv(
    "臺北市所得收入者每人所得－行業別按年別.csv",
    encoding="big5")
print(income_data.columns.values, "\n")

# 讀取勞動力資料
labor_force_data: pd.DataFrame = pd.read_csv(
    "臺北市勞動力及就業按半年別時間數列統計資料.csv",
    encoding="utf-8")
print(labor_force_data.columns.values, "\n")