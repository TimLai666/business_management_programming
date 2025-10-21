import random

# U11151013 賴廷榛 ex7 作業一 2025/10/21
dice_sum: int = 0
dice_count: int = 0
while input("按任意鍵再按[ENTER]鍵擲骰子，直接按[ENTER]鍵可以結束:"):
    dice: int = random.randint(1, 6)
    print(f"你擲的骰子點數為：{dice}")
    dice_sum += dice
    dice_count += 1
print(f"遊戲結束！總次數：{dice_count} 總點數：{dice_sum}")


# U11151013 賴廷榛 ex7 作業二 2025/10/21
lotto_numbers: list[int] = random.sample(range(1, 50), 7)
special_number: int = lotto_numbers[-1]
print(f"""本期大樂透號碼依序抽出：{lotto_numbers}
本期大樂透中獎號碼為：{", ".join(str(n) for n in sorted(lotto_numbers[:-1]))}
本期大樂透特別號為：{special_number}
""")


# U11151013 賴廷榛 ex7 作業三 2025/10/21


def isprime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num: int = int(input("請輸入一個整數："))
print(f"{num}" + ("是" if isprime(num) else "不是") + "質數")


# U11151013 賴廷榛 ex7 作業四 2025/10/21
def prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    if n <= 1:
        return factors

    if n % 2 == 0:
        factors.append(2)

    # 只找奇數
    for i in range(3, n + 1, 2):
        if n % i != 0:
            continue
        for j in range(2, int(i**0.5) + 1):
            if i != j and i % j == 0:
                break
        else:
            factors.append(i)
    return factors


n: int = int(input("請輸入一個整數："))
print(prime_factors(n))
