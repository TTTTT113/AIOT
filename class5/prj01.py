#########################匯入模組#########################
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)
wi.scan()
wi.connect("Singular_AI", "Singular#1234")

if wi.connect("singular_AI", "Singular#1234"):
    print(f"IP={wi.ip}")
#########################主程式#########################
