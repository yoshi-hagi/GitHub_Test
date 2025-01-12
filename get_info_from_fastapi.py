import requests
import os
import csv
import json

url1 = 'https://calcsi.azurewebsites.net/smr/read/all' # 1.標準報酬月額表
url2 = 'https://calcsi.azurewebsites.net/hpr/read/all' # 2.都道府県別健康保険料率・介護保険料率表
url3 = 'https://calcsi.azurewebsites.net/wr/read/all'  # 3.厚生年金保険料率表
# URLを上記の内から選択してください
url = url1 
    
response = requests.get(url)
api_json = response.json()

# JSONデータを表示
print(api_json)
    
# # jsonをcsvに変換
# output_folder = '/path/to/your/folder' # 出力フォルダのパスに変更してください
# output_file_path = os.path.join(output_folder, 'output.csv')
    
# with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file)
#     if isinstance(api_json, list):
#         keys = api_json[0].keys()
#         writer.writerow(keys)
#         for row in api_json:
#             writer.writerow(row.values())
#     elif isinstance(api_json, dict):
#         writer.writerow(api_json.keys())
#         writer.writerow(api_json.values())