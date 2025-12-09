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

# %% U11151013 賴廷榛 ex11 作業三 2025/12/9
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
#將字型檔設定字型
myfont = FontProperties(fname=r'NotoSansCJK-Regular.ttc')
# 讀入資料集檔案
df = pd.read_csv('109年台北市出生人數.csv',encoding='big5')
#建立繪圖所需資料
labels = list(df['行政區'])
data_1 = list(df["一月"])
data_2 = list(df["七月"])

#設定繪圖參數
width = 0.4 # the width of the bars
x = np.arange(len(labels)) # the label locations np.arange(len(labels))產生一個數列 0,1,2,....len(labels)-1
plt.bar([i-0.5*width for i in x], data_1, width=width, label='一月', color='skyblue') #一月、七月資料併排
plt.bar([i+0.5*width for i in x], data_2, width=width, label='七月', color='orange')
plt.xticks([i for i in x], labels, rotation=45, fontproperties=myfont)

# 設定標頭和字體
plt.title('109年1月與7月台北市各行政區出生人口數',fontproperties=myfont)
# 設定 x 軸標頭和字體
plt.xlabel('行政區',fontproperties=myfont)
# 設定 y 軸標頭和字體
plt.ylabel('出生人口數數', fontproperties=myfont)
# 設定右上角說明圖示字體
plt.legend(prop=myfont)
plt.show() # 顯示圖表

# %% U11151013 賴廷榛 ex11 作業四 2025/12/9
import requests
from bs4 import BeautifulSoup

url="https://www.twse.com.tw/rwd/zh/afterTrading/FMSRFK?date=20210101&stockNo=2330&response=html"
content = requests.get(url, verify=False).text
sp = BeautifulSoup(content, "html.parser")
datas = sp.select("table")[0]
title=datas.find("div").text.replace(" ","") #網頁標題中空格換成空字串，用來當圖表標題
rows = datas.select("tbody tr")

months: list[int] = []
high: list[float] = []
low: list[float] = []
for row in rows:
    cols = row.select("td")
    months.append(int(cols[1].text)) #月份
    high.append(float(cols[2].text)) #最高價
    low.append(float(cols[3].text)) #最低價
plt.plot(months, high, linewidth=2.0,label="最高價")
plt.plot(months, low, linewidth=2.0,label="最低價")
plt.legend()
plt.title(title) #圖表標題
plt.xlabel("月份")
plt.ylabel("金額")
plt.show()
# %%
