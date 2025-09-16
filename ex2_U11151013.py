# U11151013 賴廷榛 作業一 溫度轉換器 2025-09-16
celsius_temperature: float = float(input("請輸入攝氏溫度："))
fahrenheit_temperature: float = celsius_temperature * (9 / 5) + 32
print(f"華氏溫度為{fahrenheit_temperature:.2f} 度")  # 印出小數點後兩位

# U11151013 賴廷榛 作業二 分組器 2025-09-16
seat_number: int = int(input("請輸入座號："))
group: int = (seat_number // 6) + (
    1 if seat_number % 6 != 0 else 0)  # 如果有餘數就加一
print(f"您分配到第{group}組")

# U11151013 賴廷榛 作業三 採購費用 2025-09-16
num_drinks: int = int(input("請輸入飲料瓶數："))
num_dozens: int = num_drinks // 12
num_individual: int = num_drinks % 12
total_cost: int = (num_dozens * 300) + (num_individual * 30)
print(f"您需要買{num_dozens}打加上{num_individual}瓶飲料，總共{total_cost}元")

# U11151013 賴廷榛 回文判斷 2025-09-16
text: str = input("請輸入一個字串？")
reversed_text: str = text[::-1]
is_palindrome: bool = text == reversed_text
print(f"迴文判斷結果為{is_palindrome}")

# U11151013 賴廷榛 作業五 網域判斷 2025-09-16
email: str = input("請輸入一個e-mail？")
domain: str = email.split('@')[-1]
print(f"這個e-mail的網域為{domain}")
