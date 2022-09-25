def Key(str,key):
    newkey=""
    if(len(str)%len(key)==0):
        newkey=key*int(len(str)/len(key))
    else:
        ostat=len(str)%len(key)
        newkey=key*int(len(str)/len(key))
    for i in range(ostat):
      newkey+=key[i]
    return newkey
def Xor_encrypt(str,key):
  newkey=Key(str,key)
  en=""
  for i in range(len(str)):
    en+=chr(ord(str[i])^ord(newkey[i]))
  return en
def Xor_decrypt(str,key):
  de=""
  newkey=Key(str,key)
  for i in range(len(str)):
    de+=chr(ord(newkey[i])^ord(str[i]))
  return de
str=input()
key=input()
str2=Xor_encrypt(str,key)
print(Xor_encrypt(str2,key))
print(Xor_decrypt(str2,key))