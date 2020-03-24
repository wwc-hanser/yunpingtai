import requests
import jaon
def get_translate_date(word-None):
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
Form_data = ()
requests.get(url)
response=requests.get(url)

print(response.text)