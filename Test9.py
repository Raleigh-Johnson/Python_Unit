
# Parent Class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unkown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nspecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg
    
#Child Class 1 
    class Dog(Organism):
        name = "Loki"
        species = "Canine"
        legs = 4
        arms = 0
        origin = "Earth"

    def ingenuity(self):
        msg = "\nWill do many tricks for only a little bit of food."
        return msg
    
#Child Class 2 
class Human(Organism):
    name = "Jeff"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"

    def bit(self):
        msg = "\nCan make a mean BLT"
        return msg

#Child Class 3
    class bacterium(Organism):
        name = 'X'
        species = 'Bacteria'
        legs = 0
        arms = 0
        dna = "Sequence C"
        origin = "Mars"

        def replication(self):
            msg = "\nThe cells begin to divide and multiply into two seperate cells, repeating the process indefinantly"


if __name__ == "__main__":
    human = Human()
    print(human.imformation())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bit())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
