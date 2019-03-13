import random
#Пузырьковая сортировка
a=10
mas_a= [ ]
for i in range (a):
    mas_a.append(random.randint(5,20))
print(mas_a)
#============================
for i in range(a):
    for j in range(a-1):
        print('i= ',i,'j= ',j,)
        if mas_a[j] > mas_a[j+1]:
            temp=mas_a[j]
            mas_a[j]-mas_a[j+1]
            mas_a[j+1]-temp
print (mas_a)
