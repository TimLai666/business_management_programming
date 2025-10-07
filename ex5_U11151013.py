# U11151013 賴廷榛 ex5 作業一 2025/10/07
input_int: int = int(input("請輸入一個整數？"))

sum_to_n: int = 0
for i in range(1, input_int + 1):
    sum_to_n += i
print(f"1+2+...+{input_int} = {sum_to_n}")

sum_of_squares: int = 0
for i in range(1, input_int + 1):
    sum_of_squares += i * i
print(f"1^2+2^2+...+{input_int}^2 = {sum_of_squares}")

factorial: int = 1
for i in range(1, input_int + 1):
    factorial *= i
print(f"{input_int}! = {factorial}")

# U11151013 賴廷榛 ex5 作業二 2025/10/07
input_m: int = int(input("請輸入第一個整數M："))
input_n: int = int(input("請輸入第二個整數N："))
num_multiples_of_m_or_n: int = 0
for i in range(1, 1001):
    if i % input_m == 0 or i % input_n == 0:
        num_multiples_of_m_or_n += 1
print(f"1到1000之間是{input_m}或{input_n}的倍數的數字共有{num_multiples_of_m_or_n}個")
