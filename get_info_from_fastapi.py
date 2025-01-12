import requests
import json
import pandas as pd

url1 = 'https://calcsi.azurewebsites.net/smr/read/all' # 1.標準報酬月額表
url2 = 'https://calcsi.azurewebsites.net/hpr/read/all' # 2.都道府県別健康保険料率・介護保険料率表
url3 = 'https://calcsi.azurewebsites.net/wr/read/all'  # 3.厚生年金保険料率表

urls = [url1, url2, url3]

for i, url in enumerate(urls, start=1):
    response = requests.get(url)
    data_json = response.json()
    
    # JSON → DataFrame
    df = pd.DataFrame(data_json)
    
    print(f"=== DataFrame for URL{i} ===")
    print(df)
    print()  # 改行
