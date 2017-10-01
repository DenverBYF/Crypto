import sys    
from Crypto.Cipher import AES       
BLOCKSIZE=AES.block_size  
def strxor(a, b):       
    """ xor two strings"""    
    if len(a) > len(b):    
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])    
    else:    
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])    
       
    
def decry_in_ECB(key,ciphertext):   
    """decryption in ECB mode"""  
    cipher = AES.new(key, AES.MODE_ECB)    
    iv = ciphertext[:BLOCKSIZE]   #Get iv 
    ret=''    
    for idx in range(1,len(ciphertext)/BLOCKSIZE):    
        message=strxor(cipher.decrypt(ciphertext[idx*BLOCKSIZE:(idx+1)*BLOCKSIZE]),iv)    
        iv=ciphertext[idx*BLOCKSIZE:(idx+1)*BLOCKSIZE]   #refresh iv 
        ret+=message       
    return ret[:-ord(ret[-1])] # abandon padding  



def decry_in_CBC(key,ciphertext):
    """decryption in CBC mode"""
    iv=ciphertext[:BLOCKSIZE]  #Get iv
    message=ciphertext[BLOCKSIZE:]
    obj=AES.new(key,AES.MODE_CBC,iv)
    ret=obj.decrypt(message)
    return ret[:-ord(ret[-1])]

def main():
    key='140b41b22a29beb4061bda66b6747e14'.decode('hex')    
    msg1='4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.decode('hex')    
    msg2='5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.decode('hex')    
    print 'plainchiper1:   '+decry_in_ECB(key,msg1)    
    print 'plainchiper2:   '+decry_in_ECB(key,msg2)  

if __name__ == '__main__':
    main()


  
