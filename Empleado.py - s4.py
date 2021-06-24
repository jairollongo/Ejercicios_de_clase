from cargo import Cargo

class Empleado:
    secuencia=0
    def __init__(self,nomb="",sue="",carg=None):
        
        self.codigo=self.generarCodigo()
        self.nombre=nomb
        self.sueldo=sue
        self.cargoEmp=carg
        
    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia
    
    def mostrar(self):
        print("Codigo:{} Nombre:{} Cargo({}):".format(self.codigo,self.nombre,self.cargo.Emp.codigo,self.cargoEmp.descr))
        
cargo1 = Cargo("Docente")    
emp1 = Empleado("Jairo",2000,cargo1)
emp1.mostrar()
emp2 = Empleado("David",1500,cargo1)
emp2.mostrar()           