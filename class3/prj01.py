#########################匯入模組#########################
from machine import Pin, ADC

# 把可以控制腳位和讀類比的東西帶進來，板子會用到它們
from time import sleep

# 用來讓程式暫停一下，不會一直跑很快
import mcu

# 引入自己寫的 mcu 幫手，裡面有跟板子有關的功能

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
# 建立一個可以控制腳位的東西，方便後面用
light_sensor = ADC(0)
# 把 ADC0 當光感測器來讀，讀到的數字代表亮度
#########################主程式#########################
while True:
    light_sensor_reading = light_sensor.read()
    print(f"value = {light_sensor_reading},{round(light_sensor_reading *100/1024)}%")
    sleep(1)
