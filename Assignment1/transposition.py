import string
import random
import zlib 
from itertools import permutations

#encrypt message
def encryptMessage(plaintext, key): 
    matrix = []
    len_pt = len(plaintext) #length of plaintext
    len_key = len(key) #length of key
    C = len_key #declaring the Coloumn size
    R = int(len_pt / len_key) #Declaring the Row size
    rem = len_pt % len_key #remainder after
    if(rem > 0 ): #if remainder is not 0 then we will add one more 1
        R = R + 1
    
    i = C - rem #number of padding/ dummy bits required
    
    #adding the padding/dummy bits
    while(i!=0):
        plaintext = plaintext + '-'
        i = i-1
    
    #converting to matrix
    temp = 0
    for i in range(R):         
        a =[]
        for j in range(C):     
            a.append(plaintext[temp])
            temp = temp + 1
        matrix.append(a)
        
    cipher = ""
   
    key2 = []
    k = 1
    for i in range(len(key)):
        for j in range(len(key)): 
            if key[j]==str(k):
                key2.append(j)
                k=k+1
    for j in key2:
        for i in range(R):
            cipher = cipher + matrix[i][j]
    return cipher
    
#decrypt message    
def decryptMessage(cipher,key): 
    
    len_cipher = len(cipher) #length of plaintext
    len_key = len(key) #length of key
    C = len_key #declaring the Coloumn size
    R = int(len_cipher / len_key) #Declaring the Row size
    rem = len_cipher % len_key #remainder after
    
    if(rem > 0 ): #if remainder is not 0 then we will add one more 1
        R = R + 1
    
    key2 = []
    k = 1
    for i in range(len(key)):
        for j in range(len(key)): 
            if key[j]==str(k):
                key2.append(j)
                k=k+1
    
    #making empty matrix
    mat = []
    for i in range(R):          
        new = []
        for j in range(C):     
            new.append('0')
        mat.append(new)
       
    temp = 0
    #filling matrix
    for j in key2:
        for i in range(R):
            if temp<len_cipher:
                mat[i][j] = cipher[temp]
            temp = temp + 1
        
    temp = ""   #will contain plaintext
    for i in range(R):
        for j in range(C):
            if(mat[i][j]!='-'):
                temp = temp + mat[i][j]
        
    return temp
 
#Generate a CRC checksum for error detection 
def checkValidity(rt_plaintext):  
    list1 = rt_plaintext.split(sep="~")
    if(len(list1)==1):
        return 0
    else:
        rt_plaintext_bytes = bytes(list1[0], 'ascii')
        rt_checksum = zlib.crc32(rt_plaintext_bytes) 
        rt_checksum = str(rt_checksum)
        if(rt_checksum == list1[1]):
            return 1
        else:
            return 0

#Generate all permutation
def allPermutations(str):
    permutations_list = []
    character_sequences = permutations(str)

    for sequence in character_sequences:
        string_permutation = "".join(sequence)
        permutations_list.append(string_permutation)
    
    return permutations_list
        
#brute force attack for list of ciphertext
def brute_force_attack(list_of_ciphertext):
    
    for cipher in list_of_ciphertext:
        temp_key="" #refers to key from "1" to "12345678"
        
        for k in range(1,8+1):
            temp_key = temp_key + str(k) #key will grow from "1" to "12345678"
            permutations_list = allPermutations(temp_key) #to find all permuations of that possible key
        
            for current_key in permutations_list:
                rt_plaintext = decryptMessage(cipher,current_key)
                valid = checkValidity(rt_plaintext)
                
                if(valid == 1 ):
                    print("Cipher: "+ cipher + "  Key: " + current_key)
                    break
    
#main function
list_of_plaintext = ["Love is not like pizza",
                     "Don't step on the broken glass",
                     "The dog ran very fast",
                     "The boy had a party",
                     "The boy had a party",
                     "The sun is very bright",
                     "The violin had a bow",
                     "The kid ran two laps",
                     "The dad went to work",
                     "The boy hit golf balls"]

list_of_ciphertext = []
ciphertext=""
#key = input("Enter key : ")
key = "43125"

#appending CRC checksum to all plaintexts after ~(tild) symbol
for i in range(len(list_of_plaintext)):
    plaintext = list_of_plaintext[i]
    plaintext_bytes = bytes(plaintext, 'ascii')
    checksum = zlib.crc32(plaintext_bytes) 
    checksum = str(checksum)
    plaintext = plaintext + '~' + checksum
    list_of_plaintext[i] = plaintext

print("Original Plaintext : \n")
print(*list_of_plaintext, sep = "\n")
print("\n")

print("Key used for encryption is : " + key)
#Generating a list of ciphertexts
for plaintext in list_of_plaintext:
    cipher = encryptMessage(plaintext, key)
    list_of_ciphertext.append(cipher)

print("Ciphertext after Encryption : \n")
print(*list_of_ciphertext, sep = "\n")
print("\n")

#Decrypting all ciphertexts in plaintexts
list_of_rt_plaintext = []
for cipher in list_of_ciphertext:
    rt_plaintext = decryptMessage(cipher,key)
    list_of_rt_plaintext.append(rt_plaintext)

print("Plaintext after Decryption : \n")
print(*list_of_rt_plaintext, sep = "\n")
print("\n")

valid = checkValidity(rt_plaintext)
#print(valid)

#starting brute force attack
print("Ciphertext which is given as input and Key after bruteforce : \n")
brute_force_attack(list_of_ciphertext)

print("The generated key is same as we used in encryption algorithm")
