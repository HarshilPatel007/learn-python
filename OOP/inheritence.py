
class GrandFather():

    def grandfathers_property(self):
        print("one 3 stroy building")


class Father(GrandFather): 

    def fathers_property(self):
        print("2 bigha land")


class Son(Father):

    def sons_property(self):
        print("one business shop")


class Uncle(GrandFather):

    def uncles_property(self):
        print("one factory")

class CousinBother(Uncle):
    
    def cousin_property(self):
        print("one multinational company")


grandpa = GrandFather()
print("\nGrandFather has :")
grandpa.grandfathers_property()

father = Father()
print("\nFather has :")
father.fathers_property()
father.grandfathers_property()

son = Son()
print("\nSon has :")
son.sons_property()
son.fathers_property()
son.grandfathers_property()

uncle = Uncle()
print("\nUncle has :")
uncle.uncles_property()
uncle.grandfathers_property()
# uncle.sons_property()

cousin = CousinBother()
print("\nCousin brother has :")
cousin.cousin_property()
cousin.uncles_property()
cousin.grandfathers_property()
# cousin.fathers_property()
# cousin.sons_property()
