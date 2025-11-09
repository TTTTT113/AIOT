# PC執行
#########################匯入模組#########################
import socket

#########################函式與類別定義#########################

#########################宣告與設定#########################
client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 54088))  # 連接伺服器

#########################主程式#########################
while True:
    msg = input("Input Message")
    client_socket.send(msg.encode("utf8"))  # 傳送訊息給伺服器
    reply = client_socket.recv(128).decode("utf8")  # 接收伺服器回應
    if reply == "quit":
        print("Disconnected")
        client_socket.close()
        break
    print(reply)
