import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print("倒计时还剩下: ", seconds, " 秒")
        time.sleep(1)
        seconds -= 1
    print("时间到！")

focus_timer(25) # 设置专注时间为25分钟
