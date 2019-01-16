#циклы
# 6/12/18
'''
a=10
while a:
    a = int(input('Задайте значение переменной ='))
    if a==0:
        print('Вы вышли т.к а=0')
'''
#2
import random
'''
a=random.randint(1,10)
print('Кол-во рандомных чисел', a)
b=1
c=0
summa=0
while b<=a:
    number=random.randint(10,25)
    print(str(b)+'.\t', number)
    b=b+1
    summa=summa+number
    if number%2==1:
        c=c+1
print('Нечетные числа =', c)
print('Сумма всех чисел =', summa)
'''
#3
'''
a=random.randint(-10,10)
while a!=0:
    if a<0:
        print('Сгенерировались отицательные число =', a)
        break
    a=random.randint(-10,10)
    print('a= ', a)
else:
    print('Встретилось число равное нулю', a)
'''
#4
print('Загадай число от 1 до 100')
x=random.randint(1,100)
print(x)
k=y=0
while y!=x:
    y=input('Число=')
    if y==" ":
        print("Жаль");
        break
    y=int(y)
    k+=1 #k=k+1
    if abs(x-y)<5:
        print('Жарко')
    if abs(x-y)<10:
        print('Тепло')
    if abs(x-y)<20:
        print('Холодно')
    if abs(x-y)<30:
        print('Мороз')
    if y == x:
        print('Количество попыток=', k,',загаданное число =', x)
    elif k == 8:
        print('Игра закончена')

    
    
     
        
    
