import socket
from Crypto.PublicKey import RSA
import Crypto
from Crypto.Cipher import PKCS1_OAEP
from licensing.models import *
from licensing.methods import Key, Helpers, Message, Product, Customer 
import hashlib 

server = socket.socket()
host = "127.0.1.1"
port = 8080

server.connect((host, port))

#Tell server that connection is OK
s = bytes('Client: OK', encoding = 'utf8')
server.sendall(s)

#Receive public key string from server
temp = server.recv(1024)
key = RSA.import_key(temp)
encryptor = PKCS1_OAEP.new(key)

#Encrypt message and send to server
message = "Ramesh 234456789 GJ05-1234" #Data taken from scanner
result = hashlib.sha256(message.encode())
encrypted = encryptor.encrypt(result.hexdigest().encode('utf-8'))
server.sendall(encrypted)

#Server's response
temp = server.recv(1024)
server_response = str(temp, encoding='utf8')

server_response = server_response.replace("\r\n", '')
print(server_response)

#Tell server to finish connection
server.sendall(bytes("Quit", encoding='utf8'))
lastwords = server.recv(1024) #Quit server response
print(str(lastwords, encoding='utf8'))
server.close()
