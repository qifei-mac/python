import threading
import socket

def rev(sock):
    while True:
        send_msg = input("请输入要发送的字符:")
        sock.send(send_msg.encode('utf-8'))
        if send_msg == 'exit':
            break
        rev_msg = sock.recv(1024).decode('utf-8')
        if rev_msg == 'exit':
            break
        print(rev_msg)
    sock.close()


sk = socket.socket()
sk.connect(('192.168.3.190',10000))
recv_threading = threading.Thread(target=rev,args=(sk,))
recv_threading.start()
