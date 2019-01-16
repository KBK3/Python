import random
count=0
print('Тренируем сложение')
for i in range(5):
        a=random.randint(0,10)
        b=random.randint(0,15)
        print(a ,'+', b, end =" = ")
        c=int(input(' '))
        if c == a+b:
            count +=1
            print('Твои результаты =',count)
       
    
        
        
    
