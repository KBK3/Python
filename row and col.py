'''
#Прямоугольник
row=int(input('Количество строк='))
col=int(input('Количество столбцов='))
for i in range(row):
    print ('i=', i)
    
    for j in range(col):
        print(' * ', end = " ")
    print()
'''
'''

#1Треугольник
row=int(input('Количество строк='))
for i in range(row):
    for j in range(row):
        print(' * ', end = " ")
        if i==j:
            break
    print()
'''
'''
#2
row=int(input('Количество строк='))
for i in range(row):
    for j in range(i+1):
        print(' * ', end = " ")
    print()
'''
'''
#Наоборот
row=int(input('Количество строк='))
for i in range(row):
    row=row-1
    for j in range(row+1):
        print(' 1 ', end = " ")
    print()
'''
row=int(input('Количество строк='))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()
        
            
            
    
  
