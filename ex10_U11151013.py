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

data["總計"] = [data.iloc[i,1:13].sum() for i in range(len(data))]
data["月平均"] = data["總計"] / 12
print(data)
data.to_csv("109年台北市各行政區出生總人數.csv", sep=",", index=False,encoding='big5')
# %%
