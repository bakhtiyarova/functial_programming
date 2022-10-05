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
        if str[i].isupper():
            en+=chr((ord(str[i])+ord(newkey[i]))%26+65)
        if str[i].islower():
            en+=chr((ord(str[i])+ord(newkey[i]))%26+97)
        if str[i].isdigit():
            en+="0"
  return en
str=input()
key=input()
is1=Vigenere(str,key)
is2=(Vigenere(str,key)).upper()
print(is2)
s=input()
print(is2.count(s))
print(is2.replace('G','a'))
