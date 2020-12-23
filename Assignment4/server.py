import socket
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from licensing.models import *
from licensing.methods import Key, Helpers, Message, Product, Customer
import hashlib 

#Generate private and public keys
random_generator = Random.new().read
keys = RSA.generate(1024, random_generator)
decryptor = PKCS1_OAEP.new(keys)
public_key = keys.publickey()

# Our 1 variable database
message = "Ramesh 2344567890 GJ05-1234" #Data stored in database
result = hashlib.sha256(message.encode()) #Data stored in database


# encryptor = PKCS1_OAEP.new(public_key)

# message = "This is my license"
# encrypted = encryptor.encrypt(message.encode('utf-8'))
# decrypted = decryptor.decrypt(encrypted)
# print(str(decrypted, encoding='utf8'))

#Declartion
mysocket = socket.socket()
host = socket.gethostbyname(socket.getfqdn())
port = 8080
encrypt_str = "encrypted_message="

print("host = " + host)

#Prevent socket.error: [Errno 98] Address already in use
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mysocket.bind((host, port))

mysocket.listen(5)

c, addr = mysocket.accept()
#Wait until data is received.
################ 1st Recv ###################
temp = c.recv(1024)
data = str(temp, encoding='utf8')
data = data.replace("\r\n", '') #remove new line character
c.send(public_key.exportKey())
print("Public key sent to client.")

################ 2nd Recv ###################
temp = c.recv(1024)
decrypted = decryptor.decrypt(temp)
hash1 =  str(decrypted, encoding='utf8')
hash2 =  result.hexdigest()

if hash1 == hash2:
    c.send(bytes("Server: This person has valid license", encoding='utf8'))
else:
    c.send(bytes("Server: Invalid : Catch him/her", encoding='utf8'))


################ 3rd Recv ###################
temp = c.recv(1024)

# while True:

#     #Wait until data is received.
#     temp = c.recv(1024)
#     data = str(temp, encoding='utf8')
#     data = data.replace("\r\n", '') #remove new line character

#     if data == "Client: OK":
#         #c.send(bytes("public_key=" + str(public_key.exportKey(), encoding='utf8') + "\n", encoding='utf8'))
#         # c.send(bytes("public_key=" + str(public_key, encoding='utf8') + "\n", encoding='utf8'))
#         c.send(public_key.exportKey())
#         print(public_key.export_key())
#         print("Public key sent to client.")

#     elif encrypt_str in data: #Reveive encrypted message and decrypt it.
#         #data = data.replace(encrypt_str, '')
#         #print("Received:\nEncrypted message = "+str(data))
#         print(data)
#         decrypted = decryptor.decrypt(temp)
#         c.send(bytes("Server: OK", encoding='utf8'))
#         print("Decrypted message = " + decrypted)

#     elif data == "Quit": break

#Server to stop
c.send(bytes("Server stopped\n", encoding='utf8'))
print("Server stopped")
c.close()