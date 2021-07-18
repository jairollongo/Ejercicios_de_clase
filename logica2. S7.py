
class ejercicios:
    def __init__(self,datos):
        self.__lista=datos
        self.nom= ""

    def parimpar(self,numero):
        if numero % 2 == 0:
            print("{} es par".format(numero))
        else:
            print("{} es inpar".format(numero))

    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+1
        if numero == acu:
                print("{} es perfecto".format(numero))
        else:
                print("{} no es perfecto".format(numero))
    
    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+i
        return acu

    def divisores(self,num):
        cont=1
        divisores=[]
        while cont< num:
            rec= num % cont
            if rec==0:
                divisores.append(cont)
            cont=cont+1
        print(divisores)

class Programacion(ejercicios):
    def __init__(self,valor):
        super().__init__(valor)
        self.dato=valor


    def divisores(self,num):
        super().parImpar(num)
        divisores=[]
        for cont in range(1,num):
            rec= num % cont
            if rec==0:
                divisores.append(cont)
        return divisores

prog1= Programacion(20)
print(prog1.divisores(4))

