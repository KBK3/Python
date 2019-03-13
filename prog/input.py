'''
A=open('input.txt', 'r')
a=[line.strip() for line in A.readlines()]
print(a)
A.close()
'''
'''
A=open('input.txt', 'r')
mass=[ ]
for line in A.readlines():
    line=line.strip()
    mass.append(line)
    print(line)
A.close()
#1
'''
'''
B=open('output.txt', 'w')
for line in mass:
    print(line,file=B)
B.close()
'''
'''
#2
A=open('input.txt', 'r')
B=open('output.txt', 'w')
for line in A.readlines():
    line=line.strip()
    print(line,file=B)
A.close()
B.close()
'''
'''
#3
A=open('input.txt', 'r')
B=open('output.txt', 'w')
for line in A.readlines():
    line=line.strip()
    print(line+'\t ', line,file=B)
A.close()
B.close()
'''

import random
tehete_arv = int(input("Sisestage tehete arv: "))
for i in range(tehete_arv):
    a = random.randint(0,10)
    b = random.randint(0,10)
    tehe = random.randint(1,4)
    oige_vastus = 0
    avaldis = ""
    if tehe == 1: #liitmine
        oige_vastus = a + b
        avaldis = str(a) + " + " + str(b) + " = "
    elif tehe == 2: #lahutamine
        oige_vastus = a - b
        avaldis = str(a) + " - " + str(b) + " = "
    elif tehe == 3: #korrutamine
        oige_vastus = a * b
        avaldis = str(a) + " * " + str(b) + " = "
    elif tehe == 4: #jagamine
        oige_vastus = round(a / b, 2) #ümardame 2 komakohani
        avaldis = "" #iga tsükli samm kustutatakse eelmine väärtus
    if tehe == 1: #liitmine
        oige_vastus = a + b
        avaldis = str(a) + " + " + str(b) + " = "
        f1 = open("tehted.txt", "a")
        f1.write(avaldis + "\n") #lisame lõppu reavahetuse(\n)
        f1.close()
        f2 = open("vastused.txt", "a")
        f2.write(avaldis + str(oige_vastus) + "\n")
        f2.close()
