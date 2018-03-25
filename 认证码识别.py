from PIL import Image
import pytesseract
import requests
import random
import os
import time



headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'}



def GetCode(url):
    im = Image.open(url)
    img = im.convert('RGB')

    pix = img.load()  # 转换为像素
    for x in range(img.size[0]):  # 处理上下黑边框，size[0]即图片长度
        pix[x, 0] = pix[x, img.size[1] - 1] = (255, 255, 255, 255)
    for y in range(img.size[1]):  # 处理左右黑边框，size[1]即图片高度
        pix[0, y] = pix[img.size[0] - 1, y] = (255, 255, 255, 255)
#img.save('/Users/qifei/Desktop/last.jpg')

    for y in range(img.size[1]):  # 二值化处理，这个阈值为R=140，G=140，B=140
        for x in range(img.size[0]):
            if pix[x, y][0] < 140 or pix[x, y][1] < 140 or pix[x, y][2] < 140:
                pix[x, y] = (0, 0, 0, 255)
            else:
                pix[x, y] = (255, 255, 255, 255)

    code = pytesseract.image_to_string(img)
    return code

#imageurl = '/Users/qifei/Desktop/15.jpg'
#code = GetCode(url)
#print(code)


def GetImage(url,imageurl,session):
    timeout = random.choice(range(8, 18))
    while True:
        try:
            rep = session.get(url, headers=headers, timeout=timeout)
            #return rep
            with open(imageurl,'wb') as f:
                f.write(rep.content)
            break
        except Exception as e:
            # print("3:",e)
            time.sleep(random.choice(range(8, 15)))
            print("reconnected %s" % url)

def SendMessage(code,telnumber,session):
    data = {'username' :telnumber,'employeeMobile' :telnumber,'challenge' :code}
    r = session.post('http://rzsc.sc.gov.cn/createMessageAuthCode',headers=headers,data=data)
    mess = (r.content.decode('utf-8'))
    return mess



tel = '18144358783'
session = requests.session()
url = 'http://rzsc.sc.gov.cn/ObtainRandomImg.do'
imageurl = '/Users/qifei/Desktop/100.jpg'
GetImage(url,imageurl,session)
code = GetCode(imageurl)
message = SendMessage(code,tel,session)

while True:
    if "challengeIsWrong" in message:
        print(message)
        GetImage(url, imageurl, session)
        code = GetCode(imageurl)
        SendMessage(code, tel, session)
        message = SendMessage(code, tel, session)
    else:
        print(code)
        shijian = time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))
        with open('/home/qifei/zidonghua/send-record.txt','wb') as f:
            f.write(shijian)
        break