# dictionary = {"pomarańcza": "orange", "czarny" : "black", "niebieski":"blue"}


# while True:
#     słowo = input("Podaj słowo po polsku ")
#     if słowo == "q":
#             break
#     try:
#         print("tłumaczenie:", dictionary[słowo])
#     except KeyError:
#         tłumaczenie = input("nie znam tego słowa, podaj jego tłumaczenie: ")
#         if tłumaczenie == "q":
#             break
#         dictionary[słowo] = tłumaczenie
    
# dictionary2 = {}
# while True:
#     słowo2 = input("Podaj słowo :")
#     if słowo2 != "q":
#         break
#     dictionary2[słowo2] = len(słowo2)
#     print(dictionary2[słowo2])

import random
def losujznak():
    return chr(random.randint(97,120))

a = losujznak()
print(a)