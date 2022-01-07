import requests

# url地址
url = "https://v.qq.com/x/cover/mzc00200prv7r23/g0041dk7if6.html"

# 请求url
response = requests.get(url).text
print(response)
