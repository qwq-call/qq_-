import pyautogui
import time
pyautogui.FAILSAFE =True

mytime=0
# mytime1=mytime

time_first=time.time()

f=open('time.txt',"r")
last_time=f.read()
print(last_time)
f.close()

f2 = open('time.txt', "w")
f2.write(str(time_first))
f2.close()




myvalue=time_first
time_second=0

def mouseClick(clickTimes, lOrR, img, reTry):
    global mytime
    global time_first
    global time_second
    if reTry == 1:
        while True:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("单击左键",img)
                print('点赞成功')
                mytime+=1
                time_second =0
                time_first=time.time()

                break
                    
            else:
                scroll = -480
                pyautogui.scroll(int(scroll))
                print("未找到匹配图片,0.1秒后重s试") 
                # time.sleep(0.05)
                time_second= int(time.time()  -time_first )
                print(time_second)
                break

img = "4.png"
reTry = 1

# mytime=1

# while mytime>0:
while 1==1:
    if time_second<7:
        mouseClick(1, "left", img, reTry)
        time.sleep(0.02)
    else:
        break
now=time.time()
print('本次共点赞说说',mytime,"个,用时：",int(now-myvalue)-10,"秒")
print('距离上次点赞过了：',(time_first-int(float(last_time)))/60/60,"小时")
