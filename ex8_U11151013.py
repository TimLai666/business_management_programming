from typing import Callable

# U11151013 賴廷榛 ex8 作業一 2025/10/28


def f(n: int) -> int:
    if n == 0:
        return n
    return n*(n-1)+f(n-1)


n: int = int(input("請輸入一個整數？"))
print(f"1*2+2*3+...+{n-1}*{n}={f(n)}")


# U11151013 賴廷榛 ex8 作業二 2025/10/28
f2: Callable[[list[int]], list[int]] = lambda l: [
    e for e in l if 0 <= e <= 300]
print(f2([-2, 10, 156, 320]))
print(f2([-2, -9, 123, 16, 250, 1000]))


# U11151013 賴廷榛 ex8 作業三 2025/10/28
factors: Callable[[int], list[int]] = lambda num: [
    i for i in range(1, num+1) if num % i == 0]
print(factors(100))
print(factors(34))


# U11151013 賴廷榛 ex8 作業四 2025/10/28
while input_nums := input("兩個數字，以空格隔開："):
    a, b = map(int, input_nums.split())
    armstrong_numbers: list[int] = (lambda x, y: [i for i in range(
        x, y+1) if i == sum(
            int(digit)**len(str(i)) for digit in str(i))])(a, b)
    print(" ".join(map(str, armstrong_numbers))
          if armstrong_numbers else "找不到阿姆斯壯數!")
