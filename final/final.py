import pandas as pd

graduates_data: pd.DataFrame = pd.read_csv(
    "臺北市中等學校畢業生出路(57學年度至102學年度)時間數列統計資料.csv",
    encoding="utf-8",
)

print(graduates_data.head())

income_data: pd.DataFrame = pd.read_csv(
    "臺北市所得收入者每人所得－行業別按年別.csv",
    encoding="big5")

print(income_data.head())