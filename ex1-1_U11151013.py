# U11151013 賴廷榛
# 使用型別註解所以要3.10以上才能跑
name: str = input("請問貴姓大名？")
age: int = int(input(f"""{name} 您好：
請問今年貴庚？"""))
print(f"恭喜您，再過{60-age}年就60大壽了！")
