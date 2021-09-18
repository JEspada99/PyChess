import sys
import socket

class UDPClient():
    # Local variables
    serverAddress = ("127.0.0.1", 20001)
    bufferSize = 1024

    def __init__(self):
        # Create a UDP socket at client side
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def sendAndReceive_msg(self, msg):
        # Send to server using created UDP socket
        self.UDPClientSocket.sendto(str.encode(msg), self.serverAddress)

        # Receive server msg
        msgFromServer = self.UDPClientSocket.recvfrom(self.bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0])
        print(msg)

