import exifread
import os
import threadpool

def Get_Pic_Time(filename):
    FIELD = 'EXIF DateTimeOriginal'
    try:
        fd = open(filename,'rb')
    except:
        print("这张照片%s可能有点问题."%filename)
    tags = exifread.process_file(fd)
    if FIELD in tags:
        print(filename,"的拍照时间是：",tags[FIELD])
    else:
        print("这张照片%s没有时间属性"%filename)
    fd.close()
def get_image_list(main_path):
    gg = os.walk(main_path, True)
    x = []
    for dirs in gg:
        path = dirs[0]
        for filename in dirs[2]:
            if '.JPG' in filename:
                abfile = path + '/' + filename
                x.append(abfile)
    return x
if __name__ == '__main__':
    x = get_image_list('/Volumes/qifei/照片汇总')
    pool = threadpool.ThreadPool(1000)
    for y in threadpool.makeRequests(Get_Pic_Time,x):
        pool.putRequest(y)
    pool.wait()
