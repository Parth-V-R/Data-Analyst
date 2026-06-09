class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
        
class SmartPhone(Phone):
    def __init__(self,os,ram):
        print("Inside SmartPhone Constructor")
        self.os=os
        self.ram=ram        
        
s=SmartPhone('Android',8)        
