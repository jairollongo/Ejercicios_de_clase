class Cargo:
    secuencia=0
    def __init__(self,des="Sin cargo"):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion=des

if __name__ == "__main__":
    
    cargo1 = Cargo("Docente")
    print("Ejecutando desde el archivo cargo1.py")
    print("cargo1",cargo1.codigo,cargo1.descripcion)
    
    cargo2 = Cargo("Estudiante")
    print("cargo2",cargo2.codigo,cargo2.descripcion)
    
    cargo3 = Cargo("Master")
    print("cargo3",cargo3.codigo,cargo3.descripcion)    
    print(Cargo.secuencia)

