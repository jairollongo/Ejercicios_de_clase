class Ciclo:
    
    def __init__(self,numero=8):
        self.numero=numero
        self.numero2=0
        
    def usoWhile(self):
        # ciclo repetitivo que se ejeuta mientras la condicion se cumpla(verdadero),
        # es decir sale por falso
        car = input("ingrese vocal")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car = input("ingrese vocal").lower()
        print("Felicitacion su vocal es:{}".format(car))
            
    
      
ciclo1 = Ciclo()
ciclo1.usoWhile()
print("fin de uso de ciclo")
