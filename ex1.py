'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''

m=int(input('Введите количество элементов первого множества:  '))
n=int(input('Введите количество элементов второго множества:  '))
from random import randint
a = [randint(-10,11) for i in range(0,m)]
b = [randint(-10,11) for i in range(0,n)]
print(f'Первое множество:{a}')
print(f'Второе множество:{b}')
join_list=a+b
join_list.sort()
print(f'Объединенный упорядоченный список: {join_list}')
final_list=[]
for i in range(len(join_list)):
    if join_list[i]!=join_list[i-1]:
        final_list.append(join_list[i])
print(f'Объединенный упорядоченный список с уникальными элементами: {join_list}')


