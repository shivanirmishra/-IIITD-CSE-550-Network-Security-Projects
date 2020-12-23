#For finding two pair of public and private keys
from decimal import Decimal 
  
def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b) 
p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
no = int(input('Enter the value of text = ')) 
n = p*q 
t = (p-1)*(q-1) 
  
for e in range(2,t): 
    if gcd(e,t)== 1: 
        break
  
  
for i in range(1,10): 
    x = 1 + i*t 
    if x % e == 0: 
        d = int(x/e)
        break
        
ctt = Decimal(0) 
ctt =pow(no,e) 
ct = ctt % n 
  
dtt = Decimal(0) 
dtt = pow(ct,d) 
dt = dtt % n 

print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))

# pip install pycryptodome==3.4.3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import new as Random
from base64 import b64encode
from base64 import b64decode

class RSA_Cipher:
  def generate_key(self,key_length,e):
    self.key = RSA.generate(1024, randfunc=None, e=e)
    
  def encrypt(self,data):
    plaintext = b64encode(data.encode())
    rsa_encryption_cipher = PKCS1_v1_5.new(self.key)
    ciphertext = rsa_encryption_cipher.encrypt(plaintext)
    return b64encode(ciphertext).decode()

  def decrypt(self,data):
    ciphertext = b64decode(data.encode())
    rsa_decryption_cipher = PKCS1_v1_5.new(self.key)
    plaintext = rsa_decryption_cipher.decrypt(ciphertext,16)
    return b64decode(plaintext).decode()

cipher = RSA_Cipher()
cipher.generate_key(1024,11) #key length can be 1024, 2048 or 4096
x = cipher.encrypt("hello1") #automatically uses generated key
cipher.decrypt(x)

x = str(cipher.key.d)
len(x)

n = 131939528478437619165840658070149683757698513827170431669663383410737523568598181912292018034476806307598177114557979571234162845103802890620476988277297403377664378115452715380727540432884860515970096545819897245504547938184278157229446878218764261537243490064445190009164089426265660638032548354605532090859
e = 5
key = RSA.construct((n,e))
key



class Certificate:
  def __init__(self,id,PUC,T,DUR,info): 
      self.id = id
      self.PUC = PUC
      self.T = T
      self.DUR = DUR
      self.info = info

class CertificateAuthority: 
    # default constructor 
  def __init__(self): 
      self.PUCA = 11
      self.PRCA = 1068979152726487340235228087549571268947044207102768460854422701603306140281295237312668786032435097063940604741619954196390287439929433136975264819601667963142871811076598912280804057828199484052169439718281643639036014337802141424912000199501139018528583848403046661359287315872820549969341563948714324767
      self.PUA = 5
      self.PUB = 7
  
  #request is from A(1) or B(2)
  def receive_request(self,personAorB):
    if personAorB == 1:
      print("request received from A.")
    elif personAorB == 2:
      print("request received from B.")
  
  def return_certificate(self,x):
    if x == 1:
      return Certificate(1,7,0,60,1234567890)
    if x == 2:
      return Certificate(1,5,0,60,1234567890)
  
  #methods for printing data members 
  def print_hr(self): 
      print(self.hour)

class personA:
  def __init__(self): 
      self.id = 1
      self.PUA = 5
      self.PRA = 39581858543531285749752197421044905127309554148151129500899015023221257070579454573687605410343041892279453134367393871370248853531140867186143096483189214120938738093171394650974537721936013091386327324156328130210453188237593917643541995182220876047160282406495832812122171726652613444842383502184017763105

  def get_PUA(self): 
      return(self.PUA)

  def get_PRA(self): 
      return(self.PRA)


class personB:
  def __init__(self): 
      self.id = 2
      self.PUB = 7
      self.PRB = 637234978511810843076679979622453228270787326485169227653026820860554578013207625203070661389604561049760325967070964915335136342404505982288331990959163081699048333065718925356920148784510739442464502264684257423784925744714888941087638796592773041935060981871813387856875278781734811693343081317457795043
      
  def get_PUB(self): 
      return(self.PUB)
  
  def get_PRB(self): 
      return(self.PRB)
  
# creating object of the classes
A = personA() 
B = personB()
CA = CertificateAuthority()

#At the starting of program 
#Certificate Authority knows about PUA(Public key of A) and PUB(Public key of B)
print("1. Send message A to B:")
print("2. Send message B to A:")
choice = int(input("Enter your choice"))

if(choice == 1):
    #To send message from A to B, A need public key of B which will be requested from CA
    CA.receive_request(1)
    #Get back certificate from CA, which contains B's public key
    certificate = CA.return_certificate(1)

    cipher = RSA_Cipher()
    cipher.generate_key(1024,certificate.PUC) #key length can be 1024, 2048 or 4096
    messagetoB = cipher.encrypt("hello1") #automatically uses generated key
    print(cipher.decrypt(messagetoB))

elif(choice == 2):
    #To send message from B to A, B need public key of A which will be requested from CA
    CA.receive_request(2)
    #Get back certificate from CA, which contains B's public key
    certificate = CA.return_certificate(2)

    cipher = RSA_Cipher()
    cipher.generate_key(1024,certificate.PUC) #key length can be 1024, 2048 or 4096
    messagetoA = cipher.encrypt("hello2") #automatically uses generated key
    print(cipher.decrypt(messagetoA))


from decimal import Decimal 
  
def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b) 
p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
no = int(input('Enter the value of text = ')) 
n = p*q 
t = (p-1)*(q-1) 
  
for e in range(2,t): 
    if gcd(e,t)== 1: 
        break
  
  
for i in range(1,10): 
    x = 1 + i*t 
    if x % e == 0: 
        d = int(x/e) 
        break
ctt = Decimal(0) 
ctt =pow(no,e) 
ct = ctt % n 
  
dtt = Decimal(0) 
dtt = pow(ct,d) 
dt = dtt % n 

print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))