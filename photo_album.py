'''
实验名称：相册
版本：v1.0
日期：2022.5
作者：CaptainJackey
说明：相册幻灯片。图片尺寸240*240，需要使用PS导出JPG方式生成。
      JPG文件放到 /data/picture/ui2/ 目录下。
'''

#导入相关模块
import time,os,gc
from libs import global_var
import network
from libs.urllib import urequest
import machine
import ubinascii

#import urequests

########################
# 构建1.5寸LCD对象并初始化
########################
d = global_var.LCD

#定义常用颜色
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
ser_url='http://47.94.206.116'
ser_port=8000
app_version ='1.0'
picture_list = []
picture_num = 0

def request_download1(IMAGE_URL,outfilename):
    r = urequest.get(IMAGE_URL)
    with open(outfilename, 'wb') as f:
        f.write(r.content)
def request_download(IMAGE_URL,outfilename,filesize):
    r = urequest.urlopen(IMAGE_URL)
    #text=None
    try:
        text=r.read(filesize)
    except Exception as e:
        print(e.args)
            
    with open(outfilename, 'wb') as f:
        f.write(text)          
    f.close()    
def download_pic():
    #回收内存
    gc.collect()    
    #获取本机ID
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    #print(sta_if.ifconfig())
    mymac=ubinascii.hexlify(machine.unique_id()).decode()

    #print(mymac)
    #向服务器发送请求
    #url='http://192.168.1.11:5000/getpic/'+str(mymac)
    url='http://47.94.206.116:8000/getpic/'+str(mymac)
    #print(url)
    r = urequest.urlopen(url)
    #获取待下载文件链接
    text = r.read(800).decode('UTF-8')
    print(text)

    single_url=text
    #设定下载到本地的文件名：固定为001
    filename='001'
    request_download(single_url,'./data/picture/photo_album/'+filename+'.jpeg',40000)
def detect_refresh():
    pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
def download_refresh():
    pass
#显示图片
def UI_Display(datetime):
    
    global picture_num,picture_list
    
    gc.collect()
    if global_var.UI_Change: #首次画表盘
        
        global_var.UI_Change = 0        
        #d.fill(BLACK) #清屏
        
        picture_list = os.listdir("/data/picture/photo_album/") #获取所有图片信息
        #d.Picture(0,0,"/data/picture/photo_album/"+picture_list[0])
        #print(picture_list[0])
    #相册照片刷新新时间10秒
    if datetime[6]%10 == 0:
        picture_num = picture_num + 1
        if picture_num == len(picture_list):
    
            picture_num =0
            
        try:
            download_pic()
            d.Picture(0,0,"/data/picture/photo_album/"+picture_list[0])
        except:
            print('download error')
            d.Picture(0,0,"/data/picture/photo_album/"+picture_list[picture_num])
        
        
 

if __name__ == '__main__':
    
    
    #request_download('http://192.168.1.11:5000/2022102421585058S.png','./data/picture/photo_album/'+'001'+'.jpeg',110000)
    #d.Picture(0,0,"/data/picture/photo_album/001.jpeg")
    UI_Display([0,1,2,3,4,6,60])
        

        
        
        
