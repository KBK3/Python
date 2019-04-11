#1
class Cat():
    name=""
    color=""
    weight=0
    def meow(self):
        print( "Meow says",self.name)
cat1=Cat()
cat2=Cat()

cat1.name="Marsik"
cat1.color="black"
cat1.weight=5

cat2.name="Barsik"
cat2.color="white"
cat2.weight=7

cat1.meow()
cat2.meow()
#2
class Address():
    name=""
    line1=""
    line2=""
    city=""
    region=""
    zip=""
    def printAddress(self):
        print(self.name)
        if(len(self.line1)>0):
            print(self.line1)
        if(len(self.line2)>0):
            print(self.line2)
        print(self.city+", "+self.region+" "+self.zip)
print()
res=Address()
res.name="Andrei Andreev"
res.line1="ulica kakajato 23"
res.line2="ulica kakajato 2"
res.city="Kohtla"
res.region="Ida-Virumaa"
res.zip="15324"
res.printAddress()

