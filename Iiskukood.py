#isik 2/27/2019
isik = ''
while not isik.isdigit() or int(isik[0]) != 3 and int(isik[0]) != 4 and int(isik[0]) != 5 and int(isik[0]) != 6 or int(len(isik)!=11):
       isik = input('Введите свой личный код = ')
if int(isik[0]) == 3 or int(isik[0]) == 4:
       date = '19'
       if int(isik[0]) == 3:
              print('Пол = Мужской')
       elif int(isik[0]) == 4:
              print('Пол = Женский')
       d = isik[5:7]
       m = isik[3:5]
       y = date+isik[1:3]
       print('Дата = ',str(d)+'/'+str(m)+'/'+str(y))
elif int(isik[0]) == 5 or int(isik[0]) == 6:
       date = '20'
       if int(isik[0]) == 5:
              print('Пол = Мужской')
       elif int(isik[0]) == 6:
              print('Пол = Женский')       
       d = isik[5:7]
       m = isik[3:5]
       y = date+isik[1:3]
       print('Дата = ',str(d)+'/'+str(m)+'/'+str(y))
              
