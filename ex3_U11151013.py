# U11151013 賴廷榛 ex3 作業一 2025/09/23
nums: list[float] = []
for i in range(3):
    num: float = float(input(f"數字{i + 1}？"))
    nums.append(num)
nums.sort()
print(nums)

# U11151013 賴廷榛 ex3 作業二 2025/09/23
text: str = input("輸入一段文字？")
chars: set[str] = set(text)
for ch_to_remove in ["，", "。"]:
    chars.remove(ch_to_remove)
print(chars)

# U11151013 賴廷榛 ex3 作業三 2025/09/23
translate_dict: dict[str, str] = {
    "dog": "狗",
    "fish": "魚",
    "cat": "貓",
    "bird": "鳥",
}
print(translate_dict.keys())
eng_word: str = input("請輸入一個英文單字？")
print(translate_dict.get(eng_word, "找不到這個生字！"))

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

# U11151013 賴廷榛 ex3 作業五 2025/09/23
dept_dict: dict[str, str] = {}
print("請輸入請輸入3個科系的科系代碼")
for i in range(3):
    dept_name: str = input(f"第{i + 1}個科系？")
    dept_code: str = input(f"第{i + 1}個科系的代碼？")
    dept_dict[dept_code] = dept_name
print()
student_id: str = input("請輸入想查詢的學號？")
student_dept_code: str = student_id[4:6]
student_dept: str | None = dept_dict.get(student_dept_code, None)
print(f"此學號的科系為{student_dept}" if student_dept else "名單中沒有這個學號的科系代碼！")

# U11151013 賴廷榛 ex3 作業六 2025/09/23
Asia: list[str] = ["IBM", "Google", "Acer", "Asus", "Hitachi"]
Euro: list[str] = ["Philip", "HP", "Simens", "IBM", "Google"]
America: list[str] = ["HP", "Microsoft", "Google", "IBM"]
print(f"Asia、Euro、America分別有{len(Asia)}、{len(Euro)}、{len(America)}個客戶")
all_customers: set[str] = set(Asia + Euro + America)
print(f"全球總共有{len(all_customers)}個客戶：{all_customers}")
print(f"依名稱排序清單：{sorted(all_customers)}")
