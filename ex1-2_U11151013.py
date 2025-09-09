# U11151013 賴廷榛

name: str = input("請問貴姓大名？")
age: int = int(input(f"""{name} 您好：
請問今年貴庚？"""))
height: float = float(input("請問身高幾公分？"))
weight: float = float(input("請問體重幾公斤？"))
bmi: float = weight / ((height / 100) ** 2)
print(f"""

恭喜您，再過{60-age}年就60大壽了！
目前身高{height:.1f}公分
體重{weight:.1f}公斤
BMI為：{bmi:.2f}""")
