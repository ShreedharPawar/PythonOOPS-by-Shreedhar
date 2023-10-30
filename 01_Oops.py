class Person:
    name ="shreedhar"
    occupation="Software Developer"
    network=10000
    def info(self):
        print(self.name," is a ",self.occupation," who earns ",self.network," $")

a=Person()
print(a.name," is a ",a.occupation," who earns ",a.network," $")
b=Person()
b.name="Ramcharan"
b.occupation="Actor"
b.network=12000
b.info()