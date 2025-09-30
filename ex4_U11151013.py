# # U11051001 賴廷榛 ex4 作業一 2025/09/30
# side_lengths: list[float] = []
# for i in range(3):
#     length: float = float(input(f"請輸入三角形邊長{i + 1}的長度？"))
#     side_lengths.append(length)

# for i in range(3):
#     if side_lengths[i] + side_lengths[(i + 1) % 3] <= side_lengths[(i + 2) % 3]:
#         print("無法構成三角形")
#         break
# else:
#     # 如果for迴圈沒有被break，則執行else
#     print("可構成三角形")

# U11051001 賴廷榛 ex4 作業二 2025/09/30
year: int = int(input("請輸入一個年度："))
is_leap: bool = False
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    is_leap = True
print(f"{year}是閏年" if is_leap else f"{year}是平年")

# U11051001 賴廷榛 ex4 作業三 2025/09/30
