import random
tehete_arv = int(input("Sisestage tehete arv: "))
f1 = open("tehted.txt", "w")
f2 = open("vastused.txt", "w")
for i in range(tehete_arv):
    a = random.randint(0,10)
    b = random.randint(0,10)
    tehe = random.randint(1,4)
    oige_vastus = 0
    avaldis = " "
    if tehe == 1: #liitmine
        oige_vastus = a + b
        avaldis = str(a) + " + " + str(b) + " = "
    elif tehe == 2: #lahutamine
        while a<b:
            a = random.randint(0,10)
        while a%b>0:
            a = random.randint(0,10)
            b = random.randint(0,10)
        oige_vastus = a - b
        avaldis = str(a) + " - " + str(b) + " = "
    elif tehe == 3: #korrutamine
        oige_vastus = a * b
        avaldis = str(a) + " * " + str(b) + " = "
    elif tehe == 4: #jagamine
        while b==0:
             b = random.randint(0,10)
        oige_vastus = round(a / b, 2) #ümardame 2 komakohani
        avaldis = str(a) + " / " + str(b) + " = "
    f1.write(avaldis + "\n") #kirjutame avaldise faili „tehted.txt“
    f2.write(avaldis + str(oige_vastus) + "\n") #kirjutame avaldise ja vastuse
        #faili „vastused.txt“

f1.close() #sulgeme faili „tehted.txt“
f2.close() #sulgeme faili „vastused.txt“
