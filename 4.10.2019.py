class Address():
    name=""
    line1=""
    line2=""
    city=""
    region=""
    zip=""
homeAddress=Address()
homeAddress.name="Andrei Andreev"
homeAddress.line1="ulica kakajato 23"
homeAddress.line2="ulica kakajato 2"
homeAddress.city="Kohtla"
homeAddress.region="Ida-Virumaa"
homeAddress.zip="15324"
vacationAddress=Address()
vacationAddress.name="Evgeni Batikov"
vacationAddress.line1="Parna20"
vacationAddress.line2="ulica randomnaja"
vacationAddress.city="Valga"
vacationAddress.region="Valgamaa"
vacationAddress.zip="30156"
def printAddress(address):
    print(address.name)
    if(len(address.line1)>0):
        print(address.line1)
    if(len(address.line2)>0):
        print(address.line2)
    print(address.city+", "+address.region+" "+address.zip)
print()
printAddress(homeAddress)
print()
printAddress(vacationAddress)
#1
class Dog():
    age=""
    name=""
    weight =0
myDog=Dog()
myDog.age="3"
myDog.name="Bobik"
myDog.weight="10kg"
#2
class Person():
    name=""
    cellPhone=""
    email=""
#3
class Bird():
    color=""
    name=""
    breed=""
#4
class Character():
    x= 0
    y= 0
    name=""
    strengh=""
#5
#Нет обращения к классу у обьекта name и money
#6
#Не заданы атрибуты name

    
