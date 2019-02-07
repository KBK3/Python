n= ' '
while not n.isdigit() or int(n)<=1:
    n=input('Введите любое натуральное число =')
n=int(n)
print(n, end=' ')
while n!=1:
    if n%2==0:
        n=n/2
        print(int(n),end= ' ')
    elif n%2!=0:
        n=(n*3+1)/2
        print(int(n) ,end= ' ')
