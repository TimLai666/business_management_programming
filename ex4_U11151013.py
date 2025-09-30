# # U11151013 賴廷榛 ex4 作業一 2025/09/30
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

# # U11151013 賴廷榛 ex4 作業二 2025/09/30
# year: int = int(input("請輸入一個年度："))
# is_leap: bool = False
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     is_leap = True
# print(f"{year}是閏年" if is_leap else f"{year}是平年")

# # U11151013 賴廷榛 ex4 作業三 2025/09/30
# weight: float = float(input("請問包裹重量為多少公斤？"))
# cost: int = -1
# if weight <= 5:
#     cost = 50
# elif weight <= 10:
#     cost = 70
# elif weight <= 15:
#     cost = 90
# elif weight <= 20:
#     cost = 110
# print(f"重量{weight}公斤，"+(f"所需郵資為{cost}元" if cost != -1 else "超過20公斤無法寄送"))

# U11151013 賴廷榛 ex4 作業四 2025/09/30
delivery_method: str = input("請問包裹配送方式(1.宅配 2.i郵箱取貨)？")
if not delivery_method in {"1", "2"}:
    print("包裹配送方式必須輸入1或2！")
    exit(1)

cost: int = -1
package_weight: float = float(input("請問包裹重量為多少公斤？"))
if delivery_method == "1":
    if package_weight <= 5:
        cost = 70
    elif package_weight <= 10:
        cost = 90
    elif package_weight <= 15:
        cost = 110
    elif package_weight <= 20:
        cost = 130
else:
    if package_weight <= 5:
        cost = 48
    elif package_weight <= 10:
        cost = 68
    elif package_weight <= 15:
        cost = 88
    elif package_weight <= 20:
        cost = 113
print(f"{"宅配" if delivery_method == "1" else "i郵箱取貨"}重量{package_weight}公斤，" +
      (f"所需郵資為{cost}元" if cost != -1 else "超過20公斤無法寄送"))
