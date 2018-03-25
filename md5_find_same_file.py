import os
import hashlib
import threading
import queue
import time
import random
import threadpool




def get_hash(path):
    file = open(path, 'rb').read()
    md5 = hashlib.md5(file).hexdigest()
    print(path,md5)


def get_queue(path):
    dui_lie = []
    file_stream = os.walk(path,True)
    for dirs in file_stream:
        prepath = dirs[0]
        for k in dirs[2]:
            if '.JPG' in k:
                filename = k
                p = prepath + '/' + filename
                dui_lie.append(p)
    return dui_lie



if __name__ == '__main__':
    duilie = get_queue('/Volumes/qifei/照片汇总')
    pool2 = threadpool.ThreadPool(100)
    for n in threadpool.makeRequests(get_hash,duilie):
        pool2.putRequest(n)
    pool2.wait()


