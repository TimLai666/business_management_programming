# %% U11151013 賴廷榛 ex10 作業一 2025/12/2
import pandas as pd

student: dict[str, list] = {
    "姓名":["Tom", "Alice", "John","Cathy"],
    "身高":[181, 165, 176, 154],
    "體重":[101, 54, 72, 42]
}
data: pd.DataFrame = pd.DataFrame(student)

data["戶籍"] = ["高雄", "台南", "台北", "台中"]
data["BMI"] = data["體重"] / ((data["身高"] / 100) ** 2)

# (1)所有學生的資料
print("所有學生資料")
print(data)
print()

# (2)所有學生資料依照體重由大到小排序
print("所有學生資料依照體重由大到小排序")
print(data.sort_values(by="體重", ascending=False))
print()

# (3)平均身高與平均體重
print(f"平均身高：{data['身高'].mean():.2f} cm")
print(f"平均體重：{data['體重'].mean():.2f} kg")
print()

# (4)列出過重者(BMI>=24.0)
print("過重者(BMI>=24.0)")
print(data[data["BMI"] >= 24.0])
print()

# (5)列出過輕者(BMI<18.5)
print("過輕者(BMI<18.5):")
print(data[data["BMI"] < 18.5])
print()

# %% U11151013 賴廷榛 ex10 作業二 2025/12/2
import pandas as pd
data: pd.DataFrame = pd.read_csv("109年台北市出生人數.csv", encoding="big5")

data["總計"] = data.sum(axis=1, numeric_only=True)
data["月平均"] = data.iloc[:,:-1].mean(axis=1, numeric_only=True)
print(data)
data.to_csv("109年台北市各行政區出生總人數.csv", sep=",", index=False,encoding='big5')
print()

print("總人數前五名")
top5: pd.DataFrame=data.sort_values(by="總計", ascending=False).head(5)
print(top5)
top5.to_csv("109年台北市各行政區出生總人數前5名.csv", sep=",", index=False,encoding='big5')

# %% U11151013 賴廷榛 ex10 作業三 2025/12/2
import pandas as pd
data: pd.DataFrame = pd.read_csv("aqx_p_02.csv", encoding="utf-8")
print("檢查缺失值的狀況")
print(data.isna().sum())
print()

print(f"偵測時間 {data["datacreationdate"].min()}")
print(f"總共有 {data.shape[0]} 筆資料")
print(f"總共有 {data.isna().any(axis=1).sum()} 筆資料不全")
print()

data.dropna(inplace=True)

print(f"有 {data['site'].nunique()} 個偵測站")
print(f"空氣品質最差的地方PM2.5值為 {data["pm25"].max()}")
worst = data[data["pm25"] == data["pm25"].max()]
print(f"{worst["county"].iat[0]}{worst["site"].iat[0]}")
print(f"空氣品質最好的地方PM2.5值為 {data["pm25"].min()}")
best = data[data["pm25"] == data["pm25"].min()]
print(f"{best["county"].iat[0]}{best["site"].iat[0]}")
# %%
