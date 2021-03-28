#szyfr Cezara - ROT3

#moje rozwiązanie dla jednej litery

key = 3
# pwd = "z"
# asci = ord(pwd)   #przejście na kod ascii
# asci2 = (asci) - ord('a') #przejście z zakresu {97...x} na zakres {0....x-97}
# asci3 = (asci2) + key       #rotacja według ustalonego klucza (ROT3) (+3)
# asci4 = (asci3) % 26      #operacja modulo aby na końcu zapętlić rotację 
# asci5 = (asci4) + ord('a')
# print(chr(asci5))

#rozwiązanie Grzeszczuka dla jednej litery

# ciphertext = chr(((ord(pwd) - ord('a') + key)%26 + ord('a'))) 
# print(ciphertext)

#rozwiązanie dla dowolnego szyfru

pwd = input("Podaj hasło : ")

ciphertext = ""
for i in pwd:
    if i != chr(32):
        j = chr(((ord(i) - ord('a') + key)%26 + ord('a'))) 
        ciphertext += j
    else:
        ciphertext += i
print(ciphertext)


#zadanie domowe 
#szyfr Gransfelda-Vigenera (dłuższy klucz,  kolejne litery mają inną wartość klucza)

key2 = [3,4,8,7]
ciphertext2 = ""
for i in range(0, len(pwd),1):
    if (i % 4) == 0:
        if pwd[i] != ' ':
            j = chr(((ord(pwd[i]) - ord('a') + key2[0])%26 + ord('a'))) 
            ciphertext2 += j
        else:
            ciphertext2 += pwd[i]
    elif (i % 4) == 1:
        if pwd[i] != ' ':
            j = chr(((ord(pwd[i]) - ord('a') + key2[1])%26 + ord('a'))) 
            ciphertext2 += j
        else:
            ciphertext2 += pwd[i]
    elif (i % 4) == 2:
        if pwd[i] != ' ':
            j = chr(((ord(pwd[i]) - ord('a') + key2[2])%26 + ord('a'))) 
            ciphertext2 += j
        else:
            ciphertext2 += pwd[i]
    elif (i % 4) == 3:
        if pwd[i] != ' ':
            j = chr(((ord(pwd[i]) - ord('a') + key2[3])%26 + ord('a'))) 
            ciphertext2 += j
        else:
            ciphertext2 += pwd[i]
print(ciphertext2)