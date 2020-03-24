import requests

url="http://www.cntour.cn"

requests.get(url)
response=requests.get(url)

print(response.text)
