#########################匯入模組#########################
from machine import Pin
from time import sleep
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
Red = Pin(gpio.D5, Pin.OUT)
Green = Pin(gpio.D6, Pin.OUT)
Blue = Pin(gpio.D7, Pin.OUT)

Red.value(0)  # (1)
Green.value(0)  # (1)
Blue.value(0)  # (1)
#########################主程式#########################
while True:
    Green.value(1)  # (0)
    sleep(1)
    Red.value(1)  # (1)
    sleep(1)
    Green.value(0)  # (0)
    sleep(1)
    Red.value(0)  # (1)
