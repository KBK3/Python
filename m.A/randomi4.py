import random
#1
'''
a = random.randint(-9999999999,10)
print(a)
a = random.randint(-1000,10)
print(a)
a = random.randint(0,10)
print(a)
'''
#2
'''
b = random.randrange(40,15,56)
print(b)
b = random.randrange(10,6,28)
print(b)
b = random.randrange(10,5,24)
print(b)
'''
#3
'''
c = random.random()
print(c)
c = random.random()
print(c)
c = random.random()
print(c)
'''

#6. ЗАДАЧА «СКОЛЬКО СОВПАДАЕТ ЧИСЕЛ»
#Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна
#вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа
#различны)
'''
import random
a=random.randint(0,10)
print(a)
b=random.randint(0,10)
print(b)
c=random.randint(0,10)
print(c)
if a==b==c:
    print('Совпали 3 числа')
elif a==b or b==c:
    print('Совпали 2 числа')
else:
    print('Не совпали')
'''

