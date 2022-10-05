#Vigenere
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
def Vigenere(str,key):
  en=""
  newkey=Key(str,key)
  for i in range(len(str)):
    en+=chr((ord(str[i])+ord(newkey[i]))%26+65)
  return en
str=input()
key=input()
print(Vigenere(str,key))