# U11151013 賴廷榛 作業一 溫度轉換器 2025-09-16
celsius_temperature: float = float(input("請輸入攝氏溫度："))
fahrenheit_temperature: float = celsius_temperature * (9 / 5) + 32
print(f"華氏溫度為{fahrenheit_temperature:.2f} 度")  # 印出小數點後兩位

# U11151013 賴廷榛 作業二 分組器 2025-09-16
seat_number: int = int(input("請輸入座號："))
group: int = (seat_number // 6) + (
    1 if seat_number % 6 != 0 else 0)  # 如果有餘數就加一
print(f"您分配到第{group}組")
