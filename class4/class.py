#########################匯入模組#########################
import network

#########################函式與類別定義#########################
#########################宣告與設定#########################
wlan = network.WLAN(network.STA_IF)  # 建立 WLAN 物件，設定為站台模式
ap = network.WLAN(network.AP_IF)  # 建立 WLAN 物件，設定為存取點模式
ap.active(False)  # 關閉 AP 模式
wlan.active(True)  # 開啟 STA 模式              # 啟用存取點模式
# 搜尋 WIFI
wifi_list = wlan.scan()
print("Scan result:")
for i in range(len(wifi_list)):
    print(wifi_list[i])

wlSSID = "Singular_AI"
wlPWD = "Singular#1234"
wlan.connect(wlSSID, wlPWD)  # 連接 WIFI
while not wlan.isconnected():  # 等待連接成功
    pass
print("connet successfully", wlan.ifconfig())

#########################主程式#########################
while True:
    pass
