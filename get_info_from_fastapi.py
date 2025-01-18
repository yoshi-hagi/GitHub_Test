import requests
import pandas as pd
import os
from datetime import datetime

# URLリスト
url1 = 'https://calcsi.azurewebsites.net/smr/read/all'  # 1.標準報酬月額表
url2 = 'https://calcsi.azurewebsites.net/hpr/read/all'  # 2.都道府県別健康保険料率・介護保険料率表
url3 = 'https://calcsi.azurewebsites.net/wr/read/all'   # 3.厚生年金保険料率表

# ラベルリスト
labels = [
    "Standardized Monthly Amount of Remuneration", 
    "Health Insurance Rate and Long-Term Care Insurance Rate by prefecture", 
    "Employees' Pension Insurance Rate"
]

# URLとラベルのペアをzipでまとめる
urls = [url1, url2, url3]

for label, url in zip(labels, urls):
    response = requests.get(url)
    data_json = response.json()      # API応答をJSONに変換
    df = pd.DataFrame(data_json)     # JSONをDataFrameに変換
    
    df.to_csv(os.path.join(os.getcwd(), 'Datafiles', f'{label}.csv'), encoding='utf-8_sig')

# 作成日時を記載したtxtファイルを生成
title_date = datetime.now().strftime("%Y-%m-%d-%H-%M")
path = os.path.join(os.getcwd(), 'Datafiles', f'{title_date}_gen.txt')

s = f'This Data is generated at {title_date}'

with open(path, mode="x") as f:
    f.write(s)