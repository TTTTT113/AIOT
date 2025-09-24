#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep

# 下面這幾行是在準備好我們要用的東西。
# machine 裡的 Pin 可以控制腳位，PWM 可以做類似開關很快的開關來控制亮度。
# time 裡的 sleep 可以讓程式暫停一下，像是等一會兒再做下一步。

#########################函式與類別定義#########################
# 如果想把功能包成函式或類別，會放在這裡。這個小程式現在不用，所以空著。
#########################宣告與設定#########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
delay_time = 0.002
# frequency 是 PWM 每秒震動的速度，數字越大閃得越快，對我們來說可以想成閃爍的速度。
# duty_cycle 是亮度，數字 0 表示關、1023 表示最亮，就像調光的刻度。
# led 變數是把腳位 2 設定成可以調亮度的模式，接上一個 LED 或線圈就能看到變化。
# delay_time 是每次改變亮度後停一下的時間，數字越小變化越快，看起來越流暢。

#########################主程式#########################
while True:
    for duty_cycle in range(1023, -1, -1):
        led.duty(duty_cycle)
        sleep(delay_time)
    # 這個迴圈會從最亮慢慢變到最暗，每次把亮度設定給 LED，然後等一下。
    for duty_cycle in range(1024):
        led.duty(duty_cycle)
        sleep(delay_time)
    # 這個迴圈會從最暗慢慢變到最亮，兩個迴圈合起來就是呼吸燈的效果。
