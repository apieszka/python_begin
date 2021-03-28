# 1. Napisz program, który wypisze co drugi znak podanego ciągu.

ciag = input("podaj ciąg znaków, aby zakończyć kliknij ENTER: ")
for i in range((len(ciag)-1)):
    if i%2 == 0:
        print(ciag[i], end=' ')
print(ciag[::2])
# 2. Korzystając z biblioteki random napisz program, który wypisze na
# ekran losowy znak z podanego przez użytkownika ciągu.

import random
num = random.randint(0,len(ciag)-1)
print(" ")
print(ciag[num])
print(num)

# 1. Napisz program, który zamieni w podanym ciągu każdy znak
# duży na mały i na odwrót.

# s1 = "same male litery"
# s2 = "Jakas duza litera"
# s3 = "Zn@k specjalny"
# s4 = "1 cyfra i litery"
# print(s1.islower())
# print(s2.isupper())

for i in range((len(ciag))):
    if ciag[i].islower() == True:
        print(ciag[i].upper(), end = '')
    else:
        print(ciag[i].lower(), end = '')

# ct = "DUZE LITERY male litery"
# ct_nowy =""

# for znak in ct:
#     if znak.isupper


# 2. Napisz program, który usunie z podanego tekstu wszystkie znaki
# interpunkcyjne. Podpowiedź: użyj pętli, to skróci kod.

for i in range((len(ciag))):
    if ciag[i].isalnum() == True:
        ciag.replace(ciag[i], ' ')
print(" ")
print(ciag)

