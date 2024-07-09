print('Цикл While.')

my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

list_cap = len(my_list)
#print (list_cap)

i=0
while i < list_cap:
    if (my_list[i] >= 0):
        if (my_list[i] > 0): # нули не печатаем, но из цикла не выходим. 
            print(my_list[i] )
        i += 1
    elif (my_list[i] < 0):
            print('Найдено отрицательное')
            break

