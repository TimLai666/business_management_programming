# %% U11151013 賴廷榛 ex9 作業一 2025/11/4
name: str = input("請輸入姓名：")
city: str = input("請輸入居住縣市：")
phone: str = input("請輸入電話：")
with open("report.txt", "w", encoding="utf-8") as file:
    file.write(f"姓名：{name}\n")
    file.write(f"居住縣市：{city}\n")
    file.write(f"電話：{phone}\n")

# %% U11151013 賴廷榛 ex9 作業二 2025/11/4
import csv
fields: list = []
rows: list = []
with open("105_traffic.csv", "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(f"共有{len(rows)}筆資料")
print(fields)
print("前五筆資料如下：")
for row in rows[:5]:
    print(row)
print("1~12月各月份發生車禍的次數如下：")
month_count: list = []
for month in range(1, 13):
    count: int = sum(1 for row in rows if int(row[1]) == month)
    month_count.append(count)

print(month_count)
# %%
