import requests

headers = {
 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
w = response.text
lines = w.split('\r\n')
for url in lines:
    try:
        response = requests.get(url,timeout=2)
        content = response.content
        conten2 = str(content)
        if '\\x' in conten2:
            print(conten2)
    except Exception as q:
        print(q)
        with open('%s,jpg','wb') as f:
            f.write(w.content)
         
         
import  requests
url='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
w = requests.get('http://www.copyright-free-pictures.org.uk/animals/big-cats/white-tiger.jpg')
with open('%s.jpg','wb') as f:
         f.write(w.content)
