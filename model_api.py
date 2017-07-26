#-*-coding:utf-8-*-

import requests

url = 'http://10.172.150.35:8087/reco'

#files = {'file':open('./res/bg.jpg', 'rb')}

#res = requests.post(url, files=files)
#print (res.text)

def predict(data):
    files = {'file':data}
    res = requests.post(url, files=files)
    return res.text
