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

# %% U11151013 賴廷榛 ex11 作業二 2025/12/9
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
fm.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
matplotlib.rc('font', family='Taipei Sans TC Beta')

# 讀入資料集檔案
df = pd.read_csv('109年台北市出生人數.csv',encoding='big5')
print(df)
# 用matplotlib中的 bar()函數畫長條圖
datax = list(df['行政區']) # datax = df['行政區'] 也可以
datay = list(df['一月'])

#用datax, datay化長條圖，標記為一月
plt.bar(datax, datay, label='一月', color='blue')

# 設定標頭
plt.title('109年台北市各行政區一月出生人口數')

# 設定 x 軸標頭
plt.xlabel('行政區')

# 設定 y 軸標頭
plt.ylabel('出生人口數')

# 設定右上角說明圖示字體
plt.legend()

#x軸標題轉45度
plt.xticks(rotation=45) 
# 顯示圖表
plt.show()
#旋轉X軸標籤方向

# %%
