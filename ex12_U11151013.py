# %% U11151013 賴廷榛 ex12 作業一 2025/12/16
import requests
import pandas as pd 

res = requests.get("https://apiservice.mol.gov.tw/OdService/download/A17000000J-030190-Zee",
                   verify=False)
data = pd.DataFrame(res.json())
print(data[data["課程名稱"].str.upper().str.contains("AI")])
# %%
