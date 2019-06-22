import urllib.request
def search(我真棒)
param = urllibparse.urlencode({'wd':'我真棒'},enconding='unf8')
url='http://www.baidu.com/s?+param'
response=urllib.request.urlopen(url)
HTML = response.read(),decode('utf8')
print(HTML)