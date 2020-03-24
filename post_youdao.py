import

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_date={
    'i':'我你都是',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'alt: 15848494721139
    'sign': 'cf7cc6afcf52e84f8a352863cac07ff1',
    'ts': '1584849472113',
    'bv': '42160534cfa82a6884077598362bbc9d',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web'
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_date)
print(response.text)