#########################匯入模組#########################
from machine import Pin, ADC, PWM
from time import sleep
import mcu

gpio = mcu.gpio()
Red = Pin(gpio.D5, Pin.OUT)
Green = Pin(gpio.D6, Pin.OUT)
Blue = Pin(gpio.D7, Pin.OUT)

Red.value(0)
Green.value(0)
Blue.value(0)

#########################函式與類別定義#########################

#########################宣告與設定#########################
frquency = 1000
duty_cycle = 0

gpio = mcu.gpio()
light_sensor = ADC(0)
Red = PWM(Pin(gpio.D5), freq=1000, duty=0)
Green = PWM(Pin(gpio.D6), freq=1000, duty=0)
Blue = PWM(Pin(gpio.D7), freq=1000, duty=0)
#########################主程式#########################
while True:
    duty_cycle = light_sensor.read()
    print(duty_cycle)
    sleep(0.5)

    Red.duty(duty_cycle)
    Green.duty(duty_cycle)
    Blue.duty(duty_cycle)
