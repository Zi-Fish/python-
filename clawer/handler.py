import urllib.request
url = ' https://www.baidu.com '
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'
}
request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(handler)
# (3) 调用open方法
response = opener.open(request)
content = response.read().decode('utf-8')

print(content)
