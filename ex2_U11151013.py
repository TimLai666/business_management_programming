# U11151013 賴廷榛 作業一 溫度轉換器 2025-09-16
celsius_temperature: float = float(input("請輸入攝氏溫度："))
fahrenheit_temperature: float = celsius_temperature * (9 / 5) + 32
print(f"華氏溫度為{fahrenheit_temperature:.2f} 度")
