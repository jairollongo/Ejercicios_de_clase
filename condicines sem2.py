class Condicion:
    
    def __init__(self,num1=6,num2=5):
        self.numero1=num1
        self.numero2=num2
        numero=self.numero1+self.numero2
        self.numero3=numero
        
    def usoIf(self):
        # if ... elif ... else ...: permiten la ejecución de uno o varios bloques
        # de sentencias al cumplimiento de una o varias condiciones
        if self.numero1 == self.numero2:
            print("numero1={}=numero2={}: son iguales" .format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1 y numero3 son iguales")
        else:
            print("numero diferentes")
        print("fin if")
              
# print("instancia de la clase")
# cond2= Condicion()
# print(cond2.numero3)
# cond2.usoIf()
cond1= Condicion(20,20)
cond1.usoIf()
print("Gracias por su visita")