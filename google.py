from pytrends.request import TrendReq
pytrends = TrendReq(hl='ko-KR', tz=540)

keywords = ["비트코인"]
pytrends.build_payload(kw_list=keywords, timeframe='2023-01-01 2024-01-01', geo="KR")

df = pytrends.interest_over_time()
df.plot()


#계속 429 에러 뜸