# U11151013 賴廷榛 ex3 作業一 2025/09/23
nums: list[float] = []
for i in range(3):
    num: float = float(input(f"數字{i + 1}？"))
    nums.append(num)
nums.sort()
print(nums)
