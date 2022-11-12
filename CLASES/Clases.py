from math import pi
class Circulo():

    def __init__(self,radio,num):
        self.radio=radio
        self.num=num

    def area(self):
        
        return (pi * pow(self.radio,2))*self.num
         
    def perimetro(self):
        
        return (pi *(2*self.radio))*self.num

    
class NoCero(Exception):
    def __init__(self, radio, message="Ni la superficie ni el perimetro pueden ser 0"):
        self.radio=radio
        self.message=message
        super().__init__(self.message)

c=Circulo(2,0)
if c.radio <= 0 or c.num <=0:
    raise NoCero(c)
else:
    print(f"El area del circulo es:{c.area():.2f} cm\xb2.")
    print(f"El perimetro del circulo es:{c.perimetro():.2f}")
    