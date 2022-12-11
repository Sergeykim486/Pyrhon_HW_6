# Из домашнего заданий 2 задача 2
# старое решение
# print('Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.'
#       '\nПример:'
#       '\n- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)')
# 
# num = int(input('Введите значение целого числа "N" ->  '))
# List1 = []
# for i in range(num):
#     temp = 1
#     for j in range(i+1):
#         temp = temp * (j+1)
#     List1.insert(i, temp)
# print(List1)

def mult(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

num = int(input('Введите значение целого числа "N" ->  '))
print([mult(i) for i in range(1, num+1)])