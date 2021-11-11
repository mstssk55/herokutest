# import os
# ADDLESS = os.environ['token']
# print("アドレス:", ADDLESS)

# if os.environ["test"]:
#     print("あ")
# else:
#     print("い")


import json

str = {
    "東京":{
        "population": 1300,
        "capital": "大阪"
    },
    "北海道":{
        "population": 538,
        "capital": "札幌市"
    },
    "沖縄":{
        "population": 143,
        "capital": "那覇市"
    }
}

with open('test.json', 'w') as f:
    json.dump(str, f, ensure_ascii=False)