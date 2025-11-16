class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SDD3 = 10
        self._SDD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SDD3(self):
        return self._SDD3

    @property
    def SDD2(self):
        return self._SDD2


import network


class wifi:
    def __init__(self, ssid=None, password=None):
        """
        初始化 WiFi 模組
        ssid: WiFi 名稱
        password: WiFi 密碼
        """
        self.sta = network.WLAN(network.STA_IF)  # 建立 WLAN 物件，設定為站台模式
        self.ap = network.WLAN(network.AP_IF)  # 建立 WLAN 物件，設定為存取點模式
        self.ssid = ssid
        self.password = password
        self.ap_active = False  # 關閉 AP 模式
        self.sta_active = False  # 開啟 STA 模式
        self.ip = None

    def setup(self, ap_active=False, sta_active=True):
        """
        設定 WiFi 模組
        ap_active: 是否開啟 AP 模式
        sta_active: 是否開啟 STA 模式

        使用方法:
        wi.setup(ap_active =True|False, sta_active =True|False)

        """
        self.ap.active(ap_active)
        self.ap_active = ap_active
        self.sta.active(sta_active)
        self.sta_active = sta_active

    def scan(self):
        """
        搜尋 WiFi
        返回: WIFI 列表
        使用方法:
        Wi.scan()
        """
        if self.sta_active:
            wifi_list = self.sta.scan()
            print("Scan result:")
            for i in range(len(wifi_list)):
                print(wifi_list[i][0])
        else:
            print("SAT 模式未啟用")

    def connect(self, ssid=None, password=None) -> bool:
        """
        連接 WiFi
        ssid: WiFi 名稱
        password: WiFi 密碼

        使用方法:
        wi.connect("WIFI_name ", "WIFI_password")
        或在初始化時有設定過就可以不用再設定
        wi.connect()
        """

        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password

        if not self.sta_active:
            print("STA 模式未啟用")
            return False

        if ssid is None or password is None:
            print("WIFI 名稱或密碼未設定")
            return False

        if self.sta_active:
            self.sta.connect(ssid, password)  # 連接 WIFI
            while not (self.sta.isconnected()):  # 等待連接成功
                pass
            self.ip = self.sta.ifconfig()[0]  # 取得ip
            print("connet successfully", self.sta.ifconfig())
            return True
