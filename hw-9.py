#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
num_1 =int(input('Введите первое число (числа не долдны повторяться): '))
num_2 = int(input('Введите второе число (числа не долдны повторяться): '))
num_3 = int(input('Введите третье число (числа не долдны повторяться): '))
num_list = [num_1, num_2,num_3]
num_list.sort()
if num_1 != num_2 and num_2 != num_3:
    print(num_list[1])
else:
    print('По условию все числа должны быть разными')

