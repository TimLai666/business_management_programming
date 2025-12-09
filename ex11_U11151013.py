# %% U11151013 賴廷榛 ex11 作業一 2025/12/9
import matplotlib.pyplot as plt

years: list[int] = [2015,2016,2017,2018,2019]
city1: list[int] = [128,150,199,180,150]
city2: list[int] = [120,145,180,170,120]

yLocators: range = range(50, 251, 25)
plt.xlabel("Year")
plt.xticks(years)
plt.ylabel("Million")
plt.yticks(yLocators)
plt.plot(years, city1, marker='s', label="Taipei", linewidth=2.0, color="red", markersize=12, linestyle="-.")
plt.plot(years, city2, marker='*', label="Taichung", linewidth=2.0, color="green", markersize=12, linestyle="--")
plt.title("Sales Report")
plt.legend()
plt.grid(color="blue", linewidth=1, alpha=0.5)
plt.show()
# %%
