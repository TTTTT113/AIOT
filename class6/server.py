#########################匯入模組#########################
import socket

#########################函式與類別定義#########################

#########################宣告與設定#########################
Host = "localhost"  # IP
Port = 54088  # Port  , 可自行更改但需與客戶端相同
server_socket = socket.socket()  # 建立socket物件
server_socket.bind((Host, Port))  # 綁定IP與Port
server_socket.listen(5)  # 最連接數量,超過則拒絕連接
print(f"server: {Host}, port: {Port}  start")
client, addr = server_socket.accept()  # 等待客戶端連接
print(f"client address: {addr[0]} port: {addr[1]} connected")
#########################主程式#########################
while True:
    msg = client.recv(128).decode()  # 接收客戶端訊息
    print(f"Receive Message: {msg}")
    reply = ""

    if msg == "Hi":
        reply = "Hello"
        client.send(reply.encode("utf8"))  # 傳送訊息給客戶端
    elif msg == "Bye":
        client.send(b"quit")  # 傳送訊息給客戶端
        break
    else:
        reply = "What?"
        client.send(reply.encode("utf8"))  # 傳送訊息給客戶端


client.close()  # 關閉連接
server_socket.close()  # 關閉伺服器
