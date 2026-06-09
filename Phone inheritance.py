class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
        
    def buy(self):
        print("Buying Phone")
        
class SmartPhone(Phone):
    pass

a=SmartPhone(40000,'Samsung',50)
