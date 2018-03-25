import socketserver


#def rev(sock,addr):
#    while True:
#        rev_msg = sock.recv(1024).decode('utf-8')
#        if rev_msg == 'exit':
#            sock.close()
#            break
 #    print(addr,'发来消息:',rev_msg)
  #       send_msg = input("请输入要发送的字符:")
   #     sock.send(send_msg.encode('utf-8'))
    #    if send_msg == 'exit':
     #       sock.close()
      #      break

#sk = socket.socket()
#sk.bind(('192.168.3.190',10000))
#sk.listen(2)

class My_server(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).decode('utf-8')
            if self.data == 'exit':
                break
            print(self.data)
            feedback_msg = input('输入要传输的字符:')
            self.request.sendall(feedback_msg.encode('utf-8'))
        self.request.close()

host = '192.168.3.190'
port = 10000
server = socketserver.ThreadingTCPServer((host,port),My_server)
server.serve_forever()




