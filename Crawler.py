# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 19:15:45 2017

@author: 小铭同学
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import itchat
from threading import Timer 


def printHello(): 
      #打开的商品页
      http = urlopen("https://detail.tmall.com/item.htm?id=559781316255&price=999.5&price=999.5&sourceType=item&sourceType=item&sourceType=item&sourceType=item&suid=fbba44ed-fe34-43c2-a0df-3fbb04121443&suid=fbba44ed-fe34-43c2-a0df-3fbb04121443&ut_sk=1.WR7Z3Z8Sj/wDAHwYTPmotHYy_21646297_1513174518728.Copy.1&ut_sk=1.WR7Z3Z8Sj/wDAHwYTPmotHYy_21646297_1513174518728.Copy.1&un=79f8f6c1ebb989b37818d8ca87f7ee9a&un=79f8f6c1ebb989b37818d8ca87f7ee9a&share_crt_v=1&share_crt_v=1&cpp=1&cpp=1&shareurl=true&shareurl=true&spm=a313p.22.19y.84041617823&spm=a313p.22.19y.84041617823&short_name=h.yFKnmp&short_name=h.yFKnmp&_tbScancodeApproach_=scan&_tbScancodeApproach_=scan&app=firefox&app=firefox")
      bsObj = BeautifulSoup(http,"lxml")
      pid=bsObj.find('body')
      pi=pid.find('span',text="165/88A/XS")#尺码标签
      #print(pi)
      if pi!=None:
            itchat.send('165/88A/XS有货啦','你的微信号或者文件传输助手名称')
      else:
            print("程序正在执行")
      t = Timer(30, printHello)#设定每隔30s访问一次网页 
      t.start() 
  
if __name__ == "__main__":
      itchat.auto_login(True)
      printHello()
      itchat.run()
