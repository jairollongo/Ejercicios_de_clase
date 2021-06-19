""" num=30
nombre="jairo"
print(num,type(num))
print(nombre,type(nombre))

def mensaje(msg):
    print(msg)
    
mensaje("Mi primer programa en Python")
mensaje("Mi segundo programa en Python") """

class Sintaxis:
    instancia=0 # atributo de clase
    
     # _init_ Metodoconstructor que se ejecuta cuando se instancia la clase cuo objetivo es creando
     # e inicializar los atributos de la clase. Self es un objetivo que representa la case creada
    def __init__(self,dato="llamando al constructor2"):
        self.frase=dato # atributo de instancia
        Sintaxis.instancia = Sintaxis.instancia+1
        
    
    def usoVariables(self):
        edad, _peso = 21, 80
        nombres = 'Jairo Llongo'
        car = nombres[0]
        Tipo_sexo = 'M'
        Civil = True
        # tuplas = () son colecciones de datos de cualquier tipo inmutables
        usuario=()
        usuario=('dllongo', '1234', 'llongo@gmail.com')
        #print(usuario[2], nombres [7])
        #usuario [3]="Castillo"
        #usu = usuario [2]
        # # listas = [] colecciones mutables
        materias = []
        materias = ['Estructura de datos', 'PHP', 'POO']
        aux=materias[1]
        materias[1]="Python"
        materias.append("Go")
        #print(materias,aux, materias[1] )
        # diccionario = {} selecciones de objetos clave:valor tipo json
        docente={}
        docente = {'nombre': 'Jairo', 'edad': 21, 'activo': True}
        edad = docente['edad']
        docente['edad']=22
        docente['carrera']='IS'
        #print(docente,edad,docente['edad'])
        # print(usuario,usuario[0],usuario[0:2],usuario[-1])
        # print(nombres,nombres[0],nombres[0:2],nombres[-1])
        print(materias,materias[2:],materias[:1],materias[::],materias[-2:])
        
        # # presentacion con format
        # print("""Mi nombre es {}, tengo {}
        #       años""".format(nombres, edad))
                       
# print("Sintaxis antes de instancia: {}".format(Sintaxis.instancia))        
ejer1 = Sintaxis() # Instancia la clase sintaxis  y crea el objeto ejer1(copia de la clase)
# print("Sintaxis de ejer1 es: {}".format(Sintaxis.instancia))
# ejer2 = Sintaxis("instancia2")
# print(ejer1.frase) 
# print("Sintaxis de ejer2 es: {}".format(Sintaxis.instancia))
# print("Sintaxis nuevamente de ejer1 es: {}".format(Sintaxis.instancia))
# print(ejer2.frase)
ejer1.usoVariables()

       
