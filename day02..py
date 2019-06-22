import urllib.request
url='http:www.17k.com/chapter/2933095/36699279.html'
request=urllib.request.Request(url)
request=urllib.request.urlopen(request)
HTML = response.read(),decode('utf8')
with open('c:/users/Administrator/Desktop/day02.txt','w',encoding='utf8')as f:
    f.write('HTML')