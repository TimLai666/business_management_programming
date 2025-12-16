# %% U11151013 賴廷榛 ex12 作業一 2025/12/16
import requests
import pandas as pd 

res = requests.get(
    url="https://apiservice.mol.gov.tw/OdService/download/A17000000J-030190-Zee",
    verify=False)
data = pd.DataFrame(res.json())
print(data[data["課程名稱"].str.upper().str.contains("AI")])

# %% U11151013 賴廷榛 ex12 作業二 2025/12/16
import requests
import pandas as pd 
res = requests.get(
    url="https://openapi.twse.com.tw/v1/opendata/t187ap14_L",
    verify=False,
)

data = pd.DataFrame(res.json())
data["基本每股盈餘(元)"]= pd.to_numeric(data["基本每股盈餘(元)"], errors='coerce')
print(data[data["基本每股盈餘(元)"]==data["基本每股盈餘(元)"].max()])
print(data[data["基本每股盈餘(元)"]==data["基本每股盈餘(元)"].max()]["基本每股盈餘(元)"].values[0])
# %%
