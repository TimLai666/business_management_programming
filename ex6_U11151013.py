import random

# U11151013 賴廷榛 ex6 作業一 2025/10/14
input_str: str = input("請輸入一個字串：")
if input_str.isdigit():
    print(f"此字串{input_str}符合規定")
else:
    print("輸入的字串包含非數字的字元")

# U11151013 賴廷榛 ex6 作業二 2025/10/14
has_digit: bool = False
has_alpha: bool = False
input_str: str = input("請輸入一個包含英文字與數字的密碼:")

for char in input_str:
    if char.isdigit():
        has_digit = True
    elif char.isalpha():
        has_alpha = True
    if has_digit and has_alpha:
        print(f"此字串{input_str}符合規定")
        break
else:
    print("輸入的字串沒有同時包含數字與英文字")

# U11151013 賴廷榛 ex6 作業三 2025/10/14
input_int_m: int = int(input("請輸入一個整數:"))
max_n: int = 0
min_n: int = 0
for i in range(1, input_int_m + 1):
    factorial: int = 1
    for j in range(1, i + 1):
        factorial *= j
    if factorial < input_int_m:
        max_n = i
    elif min_n == 0:
        min_n = i
        break
print(f"{max_n}!<{input_int_m}")
print(f"{min_n}!>={input_int_m}")

# U11151013 賴廷榛 ex6 作業四 2025/10/14
mora_dict: dict[int, str] = {0: "剪刀", 1: "石頭", 2: "布"}
while True:
    mora_random: int = random.randint(0, 2)
    # 海象運算子順便把輸入存到input_mora變數
    while (input_mora := int(input("請出拳：[0]剪刀[1]石頭[2]布:"))) not in mora_dict:
        print("出拳只能出0,1,2三個整數")
    if input_mora == mora_random:
        print(f"你出{mora_dict[input_mora]}，電腦出{mora_dict[mora_random]}，平手")
    elif (input_mora == 0 and mora_random == 1) or (input_mora == 1 and mora_random == 2) or (input_mora == 2 and mora_random == 0):
        print(f"你出{mora_dict[input_mora]}，電腦出{mora_dict[mora_random]}，電腦贏")
    else:
        print(f"你出{mora_dict[input_mora]}，電腦出{mora_dict[mora_random]}，你贏了")
        print("遊戲結束")
        break
