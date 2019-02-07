'''
s=input('Ввведите слово=')
b=input=len(s)
print('Длинна слова:',b)
print(s[0:b:2])
print(s[0:len(s):2])
for i in range(0,len(s)):
    print(i, s[i])
'''
'''
#1
stroka=input('Задайте строку симолов=')
print('1.',stroka[2])
print('2.',stroka[-2])
print('3.',stroka[0:5])
print('4.',stroka[:-2])
print('5.',stroka[::2])
print('6.',stroka[1::2])
print('7.',stroka[::-1])
print('8.',stroka[-1::-2])
print('9.',len(stroka))
'''
'''
S = input('What is your name?')
print('Hi,',S.capitalize())
'''
'''
#2
S =input('=')
#S = " Cat Monkey Crocodile Deep Mountain Zombie Quartz "
S = S.strip()
print(S)
f = S.count(' ')
f += 1
print(f)
'''
'''
S = ('Ливерпуль')
print(S)
print(len(S))
dl1 = len(S) // 2 + len(S) % 2
r1 = S[:dl1]
print(r1)
r2 = S[dl1:]
print(r2)
print('Результат:', r2+r1)
print('*'*15)
S1 = ('энфилд')
print(S1)
print(len(S1))
dl2 = len(S1) // 2
z1 = S1[:dl2]
print(z1)
z2 = S1[dl2:]
print(z2)
print('Рез:', z2+z1)
'''
'''
#4
a = 'Dark Souls'
b = a.find(' ')
print(a)
print(a[b+1:] + a[b] + a[:b])
'''
'''
#5
a=input('Enter name:')
#a= 'dsfsdgfdgtfdgfdg'
if a.count('f') == 1:
    print(a.find('f'))
elif a.count('f') >1:
    print(a.find('f'), a.rfind('f'))
'''
'''
#6
a=input('=')
b=a.count('f')
if b== 1 :
    print('-1')
elif b == 0:
    print('-2')
elif b >2:
    c = a.find('f')
    c2 = a.find('f')
    d= a.find('f', c+1)
    print(d)
'''
'''
#7
a='haaaaaaaaaaahjui'
#a=input(':')
b=a[:(a.find('h'))]
c=a[(a.rfind('h')) + 1:]
print(b+' '+c)
'''
#8
a = 'hgyyyyyyyyyh'
b=a[:a.find('h') + 1]
c=a[a.rfind('h') - 1:a.find('h'):-1]
d=a[a.rfind('h'):]
print(b+c+d)


