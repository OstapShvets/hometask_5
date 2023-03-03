######## 1а ######
#my_str = "Слава Україні!"
#for index,symbol in enumerate(my_str):
  #   if index == 2:
 #         print(symbol)

######1b########
#my_str = "Слава Україні!"
#for index, symbol in enumerate(my_str):
#     if index == 12:
#          print(symbol)

############1c############
#my_str = "Слава Україні!"
#for symbol in range(5):
  #  print(my_str[symbol])

#############1d№№№№№№№№№№
#my_str = "Слава Україні!"
#for symbol in range(12):
  #  print(my_str[symbol])

  #########1e###############
#my_str = "Слава Україні!"
#for i in range(0, len(my_str), 2):
 #   print(my_str[i])


 ##############1F№№№№№№№№№
#my_str = "Слава Україні!"
#for i in range(1, len(my_str), 2):
   # print(my_str[i])
##########1g############
#my_str = "Слава Україні!"
#for i in range(len(my_str)-1, -1, -1):
 #   print(my_str[i])
#########1h###############
#my_str = "Слава Україні!"
#for i in range(len(my_str)-1, -1, -2):
 #   print(my_str[i])

##########1i############
#my_str = "Слава Україні!"
#for i in range(len(my_str)):
  #  print(i)


##Дано рядок, що складається зі слів, розділених пробілами. Визначте, скільки у ній слів. Використовуйте для вирішення
#завдання функцію `count`#########
#str_1 = "Україна завтра переможе"
#final = str_1.count(' ')
#print(final + 1)


##Користувач вводить окремо рядок `s` та один символ `ch`. Необхідно здійснити пошук у рядку `s` всіх символів `ch`.
#Для вирішення можна використовувати тільки функцію `find` (rfind), оператори `if` та `for` (while).


s = input("Ведіть рядок: ")
ch = input("Ведіть один символ: ")
for i in range(len(s)):
    if s[i] == ch:
        print("Знайдено на місці:", i)


