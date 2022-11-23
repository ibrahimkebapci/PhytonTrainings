# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 08:00:11 2022

@author: ibrah
"""
mesaj = "Merhaba dünya"
#print(mesaj[2:5])
nes="deneme"
print(nes[1:4])
# Dizinin 4 numaralıindeksi dahil değil
atama=nes[:3]
print(atama)
print(len(atama))
Boyut=atama[len(atama)-1:len(atama)]
print(Boyut)

print(atama.upper())
print(atama.lower())

print(mesaj.replace("ü","u"))
print(mesaj)

turkce="şimşek"
print(turkce.replace("ş","s"))
print(turkce)

print(turkce.replace("i","u"))

bilgi="ibrahim;KEBAPÇI;21;İSTANBUL".strip()
print("Soyad = "+bilgi.split(";")[0])

bilgi_tekrar="Bu Bir Deneme Yazısıdır".strip()
print("İstenen yazı = "+bilgi_tekrar.split(" ")[2])

bilgi_tekrar2="deneme yazziz".strip()
print("deneme"+ bilgi_tekrar2.split(" ")[1])