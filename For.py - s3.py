class For:
    def __init__(self):
        pass
  
  
    def usoFor(self):
        # ciclo repetitivo de incrementos o decremetos se ejecuta por verdadero
        nombre = "Jairo"
        datos=["Jairo",21,True]
        # pos     0    1   2
        numeros=(2,5.6,4,1)
        docente = {'nombre': 'Jairo', 'edad': 21, 'fac': 'faci'}
        listaNotas = [(60,80),(40,80),(100,80)]
        listaAlumnos=[{"nombre":"Jairo","final":140},{"nombre":"David","final":120},{"nombre":"Josue","final":180}]
        # range([inicio=0],limite,[inc/dec=1]). Genera un rango de valores dede un valor infinito
        # se ejecuta desde inicio hasta el limite
        # for con range() o for con colecciones:
        j=0 
        while j<5:
            print('while',j)
            j=j+1
        
        for i in range(5): # rango(0,1,2,3,4)
            print('for',i,end=" ")
        print()
        for i in range(1,5):  # rango(1,2,3,4)
            print('for',i,end= " ")
        print()
        for i in range(2,10,2): # rango(2,4,6,8)
            print('for',i,end =" ")
        print()
        for i in range(12,3,-3): # range(12,9,6)
            print('for',i,end =" ")
        
        lon = len(nombre)
        for pos in range(lon):
            if pos%2 == 0 and pos !=0:
               print(pos,nombre[pos])
        
        vocal = ('a','e','i','o','u')    
        for elem in datos:
            print(elem,end=" ")
        for elem in nombre:
            print(elem,end=" ") 
        
        lon = len(datos)
        for pos in range(lon):
               print(pos,datos[pos])
               
        for pos, valor in enumerate (datos):
            print(pos,valor)      
            
        for clave,valor in docente.items():
            print(clave,valor,end=" ")   
        print(listaNotas)
        for notas in listaNotas:
            print("For externo",notas)
            for nota in notas:
                print(nota,end=" ")
            print("Saliendo del for interno")
        
        print(listaNotas)
        for notas in listaNotas:
            acum=0
            for nota in notas:
                acum=acum+nota
            print(acum/len(notas),end=" ")
        
        listaAlumnos = [{"nombre":"Jairo","final":140},{"nombre":"David","final":120},{"nombre":"Josue","final":180}]
        print("\nDiccionario de alumnos")
        print(listaAlumnos)
        acum=0
        
        for alumnos in  listaAlumnos:
            print(alumnos,len(alumnos))
            
            for clave,valor in alumnos.items():
               print(clave,":",valor,end=" ")
               if clave == 'final':
                  acum=acum+valor
                  
            print()
        print("Promedio",acum/len(listaAlumnos))     
                       
bucle = For()
bucle.usoFor()

