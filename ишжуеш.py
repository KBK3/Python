#В городе N проезд в трамвае осуществляется по бумажным отрывным билетам. Каждую
#неделю трамвайное депо заказывает в местной типографии рулон билетов с номерами от
#000001 до 999999. «Счастливым» считается билетик у которого сумма первых трёх цифр номера
#равна сумме последних трёх цифр, как, например, в билетах с номерами 003102 или 567576.
#Трамвайное депо решило подарить сувенир обладателю каждого счастливого билета и теперь
#раздумывает, как много сувениров потребуется. С помощью программы подсчитайте сколько
#счастливых билетов в одном рулоне?

'''
print('Счастливые билеты')
count=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        if i+j+k==l+m+n:
                            count +=1
print('Количество билетов',count-1)
'''
'''
print('Техника с несчастливым числом')
count=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    if i==4 or j== 4 or k==4 or  l==4 or m==4:
                            count +=1
                            print(i,j,k,l,m)
                    elif i==1 and j==3 or j==1 and k==3 or k==1 and l==3 or l==1 and m==3:
                            count +=1
                            print(i,j,k,l,m)
print('Количество', count)       
'''                        
print('Часы')
count=0
for a in range(0,3):
    for b in range(0,4):
        for c in range(0,6):
            for d in range(0,10):
                    if a==d and c==b:
                        count+=1
                        print(a,c,':',c,d)
print('Кол-во',count)
                    



