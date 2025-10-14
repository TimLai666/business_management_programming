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
        break

if has_digit and has_alpha:
    print(f"此字串{input_str}符合規定")
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
