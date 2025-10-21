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

# U11151013 賴廷榛 ex7 作業五 2025/10/21


def check_id(id_number: str) -> bool:
    if len(id_number) != 10:
        return False

    if not id_number[0].isalpha() or not id_number[1:].isdigit():
        return False

    alph_dict: dict[str, int] = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 34,
        "J": 18,
        "K": 19,
        "M": 21,
        "N": 22,
        "O": 35,
        "P": 23,
        "Q": 24,
        "T": 27,
        "U": 28,
        "V": 29,
        "W": 32,
        "X": 30,
        "Z": 33
    }

    if id_number[0].upper() not in alph_dict:
        return False

    if id_number[1] not in "12":
        return False

    weights: list[int] = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    total: int = alph_dict[id_number[0].upper()]//10 * weights[0]
    total += alph_dict[id_number[0].upper()] % 10 * weights[1]
    for char, w in zip(id_number[1:], weights[2:]):
        total += int(char) * w

    if total % 10 != 0:
        return False

    return True


while id_number := input("輸入身分證字號(按Enter結束)："):
    if check_id(id_number):
        print("身分證字號正確")
    else:
        print("身分證字號格式錯誤")

print("驗證結束！")
