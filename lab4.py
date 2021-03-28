# listaslow = ["ala", "ma", "kota", "a", "ola", "ma", "psa"]

# for slowo in listaslow:
#     print(slowo[0].upper(), slowo[1:], sep ="")
    
# Napisz program, który sprawdza, czy w ustalonej liście nazwisk
# znajduje się to podane przez użytkownika

nazwiska = ["Pieszka", "Pieszka", "Makuch", 'Oleksy']
szukana  = input("Jakiego nazwiska szukasz? : ")

licznik = 0
for nazwa in nazwiska:
    if nazwa == szukana:
        licznik += 1

if licznik == 0:
    print("nie ma takiego nazwiska w bazie")
elif licznik > 1 :
    print("Znalezniono", licznik, "nazwiska w bazie")
else:
    print("Znalezniono", licznik, "nazwisko w bazie")


# Napisz program, który podaje długości poszczególnych słów w
# tekście wpisanym przez użytkownika