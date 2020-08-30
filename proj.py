#import random
# import os.path

def encrypter(text,usrName):
    file=open("user/"+usrName + ".txt")
    temp=file.readlines()  
    char=temp[0]
    enc_char=temp[1]
    file.close()
    ch=[]
    encod=[]
    for i in char :
        ch.append(i)
        
    temp1 = int(0); temp2 = int(4)
    for _ in range(0,int(len(enc_char)/4)):
        encod.append(enc_char[temp1:temp2]); temp1 = temp2; temp2 = temp2 + 4               
    
                   
    enc=""
    for i in text:
        if i in ch:
            enc=enc+(str(encod[(ch.index(i))]))
    return enc

def decrypter(usrname,q):
    file=open("user/"+usrname + ".txt")
    temp=file.readlines()  
    aa=temp[0]
    bb=temp[1]
    file.close() 
    a=[]
    b=[]
    for i in aa :
        a.append(i)
            
    temp1 = int(0); temp2 = int(4)
    for _ in range(0,int(len(bb)/4)):
        b.append(bb[temp1:temp2]); temp1 = temp2; temp2 = temp2 + 4 

    dec = ""; temp1 = int(0); temp2 = int(4)
    for _ in range(0,int(len(q)/4)):
        dec = str(dec + a[(b.index(q[temp1:temp2]))]); temp1 = temp2; temp2 = temp2 + 4
    return dec


def appnd (usrname,text):
    file=open("user/"+usrname + ".txt" , "a")
    file.write("\n" + text)
    file.close()


# encrypter("facebook :  password","gg")
# char="""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=+_/,./<>?;':"}[]{ |"""
# usrName=input("enter the usr name")
# password=input("enter the password")
# conf_password=input("please confirm your password")
# if os.path.isfile(usrName + ".txt"):
#     print("user name already exist try another one")
# else:
#     if password == conf_password:
#         usrfile=open(usrName + ".txt" , "a")
#         usrfile.write(char + "\n")
#         for _ in char:
#             for _ in range(0,4):
#                 usrfile.write(str(random.randint(0,9)))
#         usrfile.close()
#         appnd(usrName,encrypter(password,usrName))        


# lusername=input("enter the user name")
# lpassword=input("enter your password")
# if os.path.isfile(lusername + ".txt"):
#     lfile=open(lusername + ".txt","r")
#     if lfile.readlines()[2] == encrypter(lpassword,lusername):
#         print("acces granted")
#     else :
#         print("please enter a valid password")
#     lfile.close()    
# else:
#     print("the user doesnt exist please create one")            
