import random
import datetime
import math
'''
5. Задача

import random
n=random.randint(10,20)
print('Длина массива = ', n)
mas_a=[ ]
for i in range (n):
    mas_a.append(random.randint(10,20))
print(mas_a)

count = 0
for i in range (1,n-1):
    if mas_a[i]>mas_a[i-1] and mas_a[i]>mas_a[i+1]:
        count+=1
        print(str(count)+'.', mas_a[i-1], mas_a[i], mas_a[i+1])
'''
'''
6. Задача

import random
#a=int(input('введите количество чисел в массиве: '))
n=random.randint(10,20)
print('Длина массива: ', n)
a=[ ]
for i in range (n):
    a.append(random.randint(10,20))
print(a)

max_a=a[0]
for i in range (n):
    if max_a <a[i]:
        max_a=a[i]
#print(max_a)
for i in range (n):
    if max_a == a[i]:
        print('['+str(i)+']', max_a)
'''

import datetime
print('функции дат и времени:\n')
now_date = datetime.date.today()
now_time = datetime.datetime.now()
print('сегодня: ', now_date)
print('сейчас: ', now_time)

cur_year = now_date.year
cur_month = now_date.month
cur_day = now_date.day
#ny_2016 = datetime.date(2016,4,1)
print('\nГод:\t ', cur_year)
print('Месяц:\t ', cur_month)
print('День:\t ', cur_day, '\n')
#print('Создали дату, 1 апреля 2016 года: ', ny_2016)
