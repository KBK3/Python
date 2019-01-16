'''
s=input('Ввведите слово=')
b=input=len(s)
print('Длинна слова:',b)
print(s[0:b:2])
print(s[0:len(s):2])
for i in range(0,len(s)):
    print(i, s[i])
'''
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

