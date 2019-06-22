import requests
url = 'http://www.baidu.com/s?'
def baidu(wds):
       count = 1
       for wd in wds:
            response = requests.get(url,params ={'wd':wd})
            path='res%d.txt'%count
            with open(path,mode='w',encoding='utf8') as f:
                f.write(response.text)
            count += 1
if __name__=="__main__":
        wds=('lixian','wangqian','lianxiaojiao')
        baidu(wds)
for w in url:
    if'hrep'in w:
       response2=w.split('"http"')
       print(response2[0])