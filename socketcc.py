# encoding:utf-8
import socket


class SocketClient:

    def __init__(self, port, encode):
        self.HOST = 'localhost'
        self.BUFSIZ = 1024
        self.PORT = port
        self.ENCODE = encode
        self.ADDR = (self.HOST, port)
        self.tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpCliSock.connect(self.ADDR)

    def sendMsg(self, msg):
        self.tcpCliSock.sendall(msg.encode(self.ENCODE))
        result = self.tcpCliSock.recv(self.BUFSIZ)
        return result

    def closeSocket(self):
        self.tcpCliSock.close()


if __name__ == '__main__':
    socket = SocketClient(1091, 'gbk')
    tclFile = 'SMOP_GEOLOGY:m800_创建目录.tbc'
    msg = 'RCTL\n' \
          + 'TCLSCRIPTBEGIN\n' \
          + 'set status [ SclFunction \"RECALL ANY FILE\" {file= \"' \
          + tclFile \
          + '\"}]' \
          + 'TCLSCRIPTEND\n'
    result = socket.sendMsg(msg)
    print(result.decode(socket.ENCODE))
    socket.closeSocket()
