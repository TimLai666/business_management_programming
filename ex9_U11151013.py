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

# %% U11151013 賴廷榛 ex9 作業三 2025/11/4
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
accidents_num: dict[str, int] = {'{:0>2d}'.format(i): 0 for i in range(1, 13)}
for row in rows:
    accidents_num[row[1]] += 1

print(accidents_num)

# %% U11151013 賴廷榛 ex9 作業四 2025/11/4
try:
    a: int = int(input("請輸入第一個整數："))
    b: int = int(input("請輸入第二個整數："))
    r = a + b
    print("總和為", r)
except:
    print("發生輸入非整數的錯誤!")
    
# %% U11151013 賴廷榛 ex9 作業五 2025/11/4
while True:
    try:
        a: int = int(input("請輸入第一個整數："))
    except:
        print("發生輸入非整數的錯誤!")
    else:
        break
while True:
    try:
        b: int = int(input("請輸入第二個整數："))
    except:
        print("發生輸入非整數的錯誤!")
    else:
        break
r = a + b
print("總和為", r)

# %% U11151013 賴廷榛 ex9 作業六 2025/11/4
try:
    x1: int = int(input("請輸入第一個整數："))
    x2: int = int(input("請輸入第二個整數："))
except:
    print("發生輸入非整數的錯誤!")
else:
    try:
        remainder: int = x1 % x2
        print(f"{x1}除以{x2}的餘數為{remainder}")
    except:
        print("發生 integer division or modulo by zero 的錯誤")
finally:
    print("程式執行結束")
# %%
