import random

# czy liczba jest parzysta?

# num = int(input("please, type the number to check "))

# if (num % 2) == 0:
#     print(num, "is an even number") #liczba parzysta
# else:
#     print(num, "is an odd number")  #liczba nieparzysta

# #zgadywanka liczbowa

# losowa = random.randint(0,10)
# #print(losowa) #sprawdzenie czy program działa
# num2 = int(input("type the number in range from 0 to 10 "))

# while num2 != losowa:
#     if num2 > losowa:
#         print("The number is too big")
#         num2 = int(input("type the number in range from 0 to 10 "))
#     else:
#         print("The number is too small")
#         num2 = int(input("type the number in range from 0 to 10 "))

# print("Congratulations, you guessed the number! ")


# #pierwiastekk
# num3 = int(input("type the number"))
# if num3>=0:
#     y = num3**(1/2)
#     print("The result is ", y)
# else:
#     print("Wrong number! Can't do the calculation")

#Korzystając z pętli napisz program, który wypisze kwadraty
#pierwszych 100 liczb naturalnych.

# for i in range(0,100,1):
#     print(i**2, end = ' ')

# Napisz program, który pozwala obliczyć średnią arytmetyczną
# ocen: oceny są wpisywane tak długo, dopóki użytkownik nie wpisze wartości -1. Podpowiedź: nie konwertuj wartości podanej przez
# użytkownika za pomocą funkcji int, tylko float.
# średnia = 0
# ocena = 0
# licznik = 0
# suma = 0

# while ocena != -1:
#     ocena = float(input("Podaj ocenę. Aby zakończyć podaj -1 :"))
#     if ocena != -1:
#         licznik += 1
#         suma = suma + ocena 
#     if ocena < -1:
#         print("Co to za głupoty, nieznane działanie")
#     if ocena == -1:
#         średnia = suma/licznik
#         break

# print("twoja średnia wynosi", średnia)

#zadania podsumowujące

#zadanie 1
# Napisz program, który wypisze lata przestępnych w podanym
# przez użytkownika zakresie.

# year1 = int(input("Podaj poczatkowy rok przedziału"))
# year2 = int(input("Podaj końcowy rok przedziału"))
# przestepne = False
# print("Lata przestepne w podanym przez ciebie przedziale:")
# for year in range(year1, year2):
#     if year%4 == 0 and year%100 != 0:
#         print(year, end = ' ')
#         przestepne = True
#     elif year%400 == 0:
#         print(year, end = ' ')
#         przestepne = True
# if przestepne == False:
#     print("Brak lat przestępnych w podanym przedziale!")
    
    
#zadanie 2
# Napisz odwróconą zgadywankę. Użytkownik wpisuje liczbę z
# zakresu 0, 100, a program ma za zadanie zwrócić informację po ilu
# próbach liczba została odgadnięta za pomocą losowania

# number = int(input("type number from 0 to 100: "))
# licznik = 1
# losowa = random.randint(0,100)
# while losowa != number:
#     losowa = random.randint(0,100)
#     licznik += 1
# print("Drawn correct number after", licznik, "tries")

#zadanie 3
# Zmodyfikuj program z poprzedniego zadania tak, aby przeprowadzał kilka gier i wyliczał średnią liczbę prób. Dla oszczędzenia
# sobie pracy możesz zautomatyzować użytkownika np. zakładając,
# że w każdej grze wybrał tę samą liczbę

# number = int(input("type number from 0 to 100: "))
# games = int(input("type number of games from 0 to 10: "))
# licznik = 1
# losowa = random.randint(0,100)
# time = 0
# suma = 0
# while time != games:
#     while losowa != number:
#         losowa = random.randint(0,100)
#         licznik += 1
#     suma = suma+licznik
#     time +=1

# średnia = suma/games
# print("Average number of tries to draw correct number is", średnia)

# a = 0
# b = 0
# for i in range(100):
#     if i == 0 or i==1 :
#         print(1, end = ' ')
#         a = 1
#         b = 1
#     else:
#         c = a+b
#         a = b
#         b = c
#         print(c, end = ' ')