#-*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import matplotlib.pyplot as plt

#한국어폰트
import matplotlib.font_manager as fm

from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv('NAVER_CLIENT_ID')
client_secret = os.getenv('NAVER_CLIENT_SECRET')

url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2023-11-30\",\"endDate\":\"2024-01-10\",\"timeUnit\":\"week\",\"keywordGroups\":[{\"groupName\":\"비트코인\",\"keywords\":[\"비트코인\",\"비트코인 가격\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    data = json.loads(response_body.decode('utf-8'))
    

    # 데이터 분리
    dates = [item['period'] for item in data['results'][0]['data']]
    ratios = [item['ratio'] for item in data['results'][0]['data']]

    # 그래프 생성
    plt.rc('font', family="font.ttf")
    plt.plot(dates, ratios)
    plt.xlabel('date')
    plt.ylabel('search rate')
    plt.title('Bitcoin Inganjipyo')
    plt.show()

else:
    print("Error Code:" + str(rescode))