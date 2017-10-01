import sys    
from Crypto.Cipher import AES   
from Crypto.Util import Counter 
from Crypto import Random  
BLOCKSIZE=AES.block_size  
    
def strxor(a, b):    
    """ xor two strings of different lengths """     
    if len(a) > len(b):    
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])    
    else:    
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])    
    
def strplus_one(s):     
    """plus one to input string and return a string. Used to increase iv."""     
    length=len(s)    
    s_plus=ord(s[length-1])+1    
    if s_plus<256:    
        return s[:length-1]+chr(s_plus)    
    else:    
        return strplus_one(s[:length-1])+chr(0)    
       
def decry_in_CTR(key,ciphertext):
    """decryption in CTR mode"""
    iv = ciphertext[:BLOCKSIZE]
    message = ciphertext[BLOCKSIZE:]
    c = Counter.new(BLOCKSIZE*8,initial_value=long(iv.encode('hex'),16))
    obj = AES.new(key,AES.MODE_CTR,counter=c)
    return obj.decrypt(message)
    
def decry_in_ECB(key,ciphertext):  
    """decryption in ECB mode"""    
    cipher = AES.new(key, AES.MODE_ECB)    
    iv = ciphertext[:BLOCKSIZE]    
    ret=''    
    for idx in range(1,len(ciphertext)/BLOCKSIZE):    
        iv_enc=cipher.encrypt(iv)    #xor counter and key
        message=strxor(ciphertext[idx*BLOCKSIZE:(idx+1)*BLOCKSIZE],iv_enc)    
        iv=strplus_one(iv)   #counter +1 
        ret+=message    
    if len(ciphertext)%BLOCKSIZE==0:    
        return ret    
    else:    
        iv_enc=cipher.encrypt(iv)    
        message=strxor(ciphertext[(len(ciphertext)/BLOCKSIZE)*BLOCKSIZE:],iv_enc)    
        ret+=message    
        return ret 
if __name__ == '__main__':   
    key='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')    
    msg1='69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.decode('hex')    
    msg2='770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.decode('hex')    
    print 'plainchiper1:    '+decry_in_ECB(key,msg1)    
    print 'plainchiper2:    '+decry_in_ECB(key,msg2) 