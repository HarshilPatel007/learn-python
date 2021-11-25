
class Smartphone():

    def __init__(self, name, varient, color, price):

        self.smartphone_name = name
        self.smartphone_varient = varient
        self.smartphone_color = color
        self.smartphone_price = price

    def smartphone_details(self):
        print("Smartphone name : ", self.smartphone_name)
        print("Smartphone varient : ", self.smartphone_varient)
        print("Smartphone color : ", self.smartphone_color)
        print("Smartphone price : ", self.smartphone_price)


x = Smartphone("SAMSUNG M11", "4GB RAM - 64GB ROM", "silver", 15000)

m11 = x.smartphone_details()
m11

vivo_u10 = Smartphone("Vivo U10", "4GB RAM - 64GB ROM", "black", 11000)
vivo_u10.smartphone_details()
