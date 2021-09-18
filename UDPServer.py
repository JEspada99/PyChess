import sys
import socket

class UDPServer():
    # Local variables
    ip = "127.0.0.1" # for the moment, later will be global ip
    port = 20001
    bufferSize = 1024
    
    # Constructor
    def __init__(self):
        # Create a datagram socket
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Bind to address and ip
        UDPServerSocket.bind((self.ip, self.port))

        # Listening
        while(True):
            message, address = self.attend_requests(UDPServerSocket)
            self.response(UDPServerSocket, str.encode("hola desde el servidor"), address)

    # Function for attending requests
    def attend_requests(self, UDPServerSocket):
        bytesAddressPair = UDPServerSocket.recvfrom(self.bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        print(clientMsg)
        return message, address

    def response(self, UDPServerSocket, bytesToSend, address):
        UDPServerSocket.sendto(bytesToSend, address)