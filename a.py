import requests
from os import system
# from requests import async
import json



import requests

cookies = {
    'hl_guest_id': '697af01ea4f1889f122455e6d832c111',
    'language': 'uk',
    'city_id': '70',
    'region': '1',
    'region_mode': '1',
    'hluniqueid': 'c86a734f881ab21ef84e5e753d4fb870',
    'hluniqueid_ctl': 'c3425d9245892c6d4fb12eb39fed197b',
    'hl_sid': 'f3cf66c53e97b06d1a15c1875af947de',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8,uk;q=0.7,la;q=0.6,pt;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'hl_guest_id=697af01ea4f1889f122455e6d832c111; language=uk; city_id=70; region=1; region_mode=1; hluniqueid=c86a734f881ab21ef84e5e753d4fb870; hluniqueid_ctl=c3425d9245892c6d4fb12eb39fed197b; hl_sid=f3cf66c53e97b06d1a15c1875af947de',
    'dnt': '1',
    'origin': 'https://hotline.ua',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://hotline.ua/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

search = '9705475-06'

json_data = {
    'jsonrpc': '2.0',
    'method': 'search.search',
    'params': {
        'q': search,
        'lang': 'uk',
        'section_id': None,
        'entity': 'full',
    },
    'id': 1,
}

response = requests.post('https://hotline.ua/svc/search/api/json-rpc', cookies=cookies, headers=headers, json=json_data)


res = response.json().get('result')[0].get('url')
# print(response.jsonrpc)
print("GOOD =======" + "https://hotline.ua/ua/" + res)

# "https://hotline.ua/ua/"



with open('search.json', 'w', encoding="utf-8") as f:
    f.write("https://hotline.ua/ua/" + res)


#system calls a command from terminal
system("python main.py")







