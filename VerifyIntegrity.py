#!/usr/bin/python3
import sys
import hashlib

encryptionType = sys.argv[1]
filePath = sys.argv[2]
algorithmCorrectValue = sys.argv[3]

if len(sys.argv) == 4:  
    try:  
        fileOpen = open(filePath,'rb')
        if encryptionType.lower() == 'md5':  
            algorithmValue = hashlib.md5(fileOpen.read()).hexdigest()
        elif encryptionType.lower() == 'sha1':  
            algorithmValue = hashlib.sha1(fileOpen.read()).hexdigest()  
        elif encryptionType.lower() == 'sha256':  
            algorithmValue = hashlib.sha256(fileOpen.read()).hexdigest()  
        elif encryptionType.lower() == 'sha512':  
            algorithmValue = hashlib.sha512(fileOpen.read()).hexdigest()  
        else:  
            print ('[-]Please input a correct encryption algorithm type.'  )
        fileOpen.close()
    except:  
        print ('[-]Please input a correct filename.')
    if algorithmCorrectValue == algorithmValue:
        print("校验通过，文件安全。")
    else:
        print("校验未通过，危险文件！")
else:  
    print ('[*]Usage: VerifyIntegrity.py [md5|sha1|sha256|sha512] [FilePath] [AlgorithmCorrectValue]')