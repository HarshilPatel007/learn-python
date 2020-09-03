
class Smartphone():

    def set_price(self, price):
        self.smartphone_price = price

    def get_price(self):
        return self.smartphone_price


x = Smartphone()

x.set_price(11000)
y = x.get_price()
print(y)
