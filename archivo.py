class Texto:
    def __init__(self,nombreArchivo):
        self.archivo=nombreArchivo
        
    def leer(self):
        with open(self.achivo, 'r', encoding="UTF-8") as file:
            lista=[]
            for linea in file:
                line = linea[:-1].split(self.separador)
                print(linea[:-1])

    def escribir(self,datos,modo):
        with open(self.archivo, modo, encoding="UTF-8") as file:
            for dato in datos:
                file.write(dato+"\n")

arch1  = Texto("estudiantes.txt")
arch1.escribir(["jairo","david","llongo","castillo"],"a")
arch1.leer()

