import requests
import pandas as pd

# URLリスト
url1 = 'https://calcsi.azurewebsites.net/smr/read/all'  # 1.標準報酬月額表
url2 = 'https://calcsi.azurewebsites.net/hpr/read/all'  # 2.都道府県別健康保険料率・介護保険料率表
url3 = 'https://calcsi.azurewebsites.net/wr/read/all'   # 3.厚生年金保険料率表

# ラベルリスト
labels = [
    "標準報酬月額表", 
    "都道府県別健康保険料率・介護保険料率表", 
    "厚生年金保険料率表"
]

# URLとラベルのペアをzipでまとめる
urls = [url1, url2, url3]

for label, url in zip(labels, urls):
    response = requests.get(url)
    data_json = response.json()      # API応答をJSONに変換
    df = pd.DataFrame(data_json)     # JSONをDataFrameに変換
    
    df.to_csv(f'{label}.csv', encoding='utf-8_sig')
    
    # print(f"=== {label} ===")
    # print(df.head())  # 先頭数行だけ表示（行数が多い場合）
    # print()           # 改行

