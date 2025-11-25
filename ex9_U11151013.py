# %% U11151013 賴廷榛 ex9 作業一 2025/11/4
name: str = input("請輸入姓名：")
city: str = input("請輸入居住縣市：")
phone: str = input("請輸入電話：")
with open("report.txt", "w", encoding="utf-8") as file:
    file.write(f"姓名：{name}\n")
    file.write(f"居住縣市：{city}\n")
    file.write(f"電話：{phone}\n")

# %%
