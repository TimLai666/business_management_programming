# # U11151013 賴廷榛 ex3 作業一 2025/09/23
# nums: list[float] = []
# for i in range(3):
#     num: float = float(input(f"數字{i + 1}？"))
#     nums.append(num)
# nums.sort()
# print(nums)

# # U11151013 賴廷榛 ex3 作業二 2025/09/23
# text: str = input("輸入一段文字？")
# chars: set[str] = set(text)
# for ch_to_remove in ["，", "。"]:
#     chars.remove(ch_to_remove)
# print(chars)

# # U11151013 賴廷榛 ex3 作業三 2025/09/23
# translate_dict: dict[str, str] = {
#     "dog": "狗",
#     "fish": "魚",
#     "cat": "貓",
#     "bird": "鳥",
# }
# print(translate_dict.keys())
# eng_word: str = input("請輸入一個英文單字？")
# print(translate_dict.get(eng_word, "找不到這個生字！"))

# U11151013 賴廷榛 ex3 作業四 2025/09/23
menu: dict[str, float] = {}
print("請輸入3種餐點的價目表來建立菜單")
for i in range(3):
    food_name: str = input(f"第{i + 1}種餐點？")
    food_price: float = float(input(f"第{i + 1}種餐點的價格？"))
    menu[food_name] = food_price
print()
food_to_search: str = input("請輸入想查詢的餐點名稱？")
print(menu.get(food_to_search, "價目表中沒有這個餐點！"))
