class Lista:
    def __init__(self,tamanio=3):
        self.lista = []
        self.longitud = 0
        self.size = tamanio
        
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud+= 1
        else:
            print("Lista completa")
            
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]
        
    def obtenerEliminado(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else: 
            eliminado = self.lista[pos]
            #self.lista = self.lista[:pos] + self.lista[pos+1:]
            listaAux = []
            for ind in range(pos):
                listaAux += [self.lista[ind]]
            for indice in range(pos+1,self.longitud):
                listaAux += [self.lista[indice]] 
            self.longitud -=1
            self.lista = listaAux
            return (self.lista,eliminado)
        
    def mostrar(self):
        print("{:3} {}".format("Lista","Posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:6}] {:3}".format(ele,pos))
            
               
lista1 = Lista()
lista1.append("Jairo")
lista1.append("21")
lista1.append(True)
lista1.mostrar()
posicion = int(input("Ingrese posicion para obtener el valor del elemento "))
resp =lista1.obtenerEliminado(posicion)
if resp == None:
    print("Posicion no valida, verifique la lista ")
else:
    print("El elemento de la posicion:{} es:{}".format(posicion,resp))
        
              