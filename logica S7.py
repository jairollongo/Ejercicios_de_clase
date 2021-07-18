class Ejercicios:
    def __init__(self):
        pass
        
    def parImpar(self,numero):
        if numero % 2 == 0:
            print("{} es Par".format(numero))
        else:
            print("{} es Impar".format(numero))
            
    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if num % i == 0:
                acu=acu+i
        if numero == acu:
            print("{} es Perfecto".format(numero))
        else:
            print("{} no es Perfecto".format(numero))
                      
ejer = Ejercicios()
num = int(input("Ingrese numero: "))
print("llamada 1")
ejer.perfecto(num)
input()
lista = [2,7,4,9,5,3,10]
print("llamada 2")
for num in lista:
    ejer.perfecto(num)
input()
print("llamada 3")
ejer.perfecto(23)
