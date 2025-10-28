# U11151013 賴廷榛 ex8 作業一 2025/10/28
def f(n: int) -> int:
    if n == 0:
        return n
    return n*(n-1)+f(n-1)


n: int = int(input("請輸入一個整數？"))
print(f"1*2+2*3+...+{n-1}*{n}={f(n)}")
