import requests
from bs4 import BeautifulSoup
import os
import re
import threading
import queue
class MyThreading(threading.Thread):

    def __init__(self,input,filename,fn):
        threading.Thread.__init__(self)
        self.jobq = input
        self.filename = filename
        self.fn = fn

    def run(self):
        while True:
            if self.jobq.qsize() > 0:
                self.dojob(self.jobq.get(),self.filename,self.fn)
            else:
                break

    def dojob(self,job,filename,fn):
        Download_pic(job,filename,fn)

def Download_pic(url,filename,fn):
    pic = requests.get(url)
    file_name = filename + '/' + str(fn) + '.jpg'
    print("开始下载第%s张图片"%fn)
    fp = open(file_name,'wb')
    fp.write(pic.content)
    fp.close()

if __name__ == '__main__':
    resp = requests.get("http://w3.afulyu.pw/pw/thread.php?fid=15&page=3")
    resp.encoding = 'utf-8'
    bs = BeautifulSoup(resp.text,'lxml')
    h3 = bs.find_all('h3')
    for x in h3:
        folder_name = x.text
        print(folder_name)
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        url = x.find('a')
        short_url_link = url['href']
        url_link = 'http://w3.afulyu.pw/pw/' + short_url_link
        res = requests.get(url_link)
        res.encoding = 'utf-8'
        bs1 = BeautifulSoup(res.text,'lxml')
        di = bs1.find_all('div',{'class':'tpc_content'})
        di1 = str(di)
        reg = r'src="(.*?)"/'
        img_url = re.findall(reg,di1)
        q = queue.Queue()
        for img_url in img_url:
            q.put(img_url)
        num = q.qsize()
        for j in range(num):
            MyThreading(q,folder_name,j).start()