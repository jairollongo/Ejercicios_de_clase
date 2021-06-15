# Tuplas - Listas - diccionarios

usuario = ('dllongo', '2,4,6,8','dllongo@gmail.com')
materias = ['Visual Studio','Python','PHP','Go']
estudiante = {'nombre':'Jairo','edad':21,'fac':'faci'}
print(usuario[0],materias[1],estudiante['nombre'])
print(usuario[0:2],estudiante.keys(),estudiante.values())
materias.append('Programacion Movil')
estudiante['sexo'],estudiante['edad']='M',21
print(materias,estudiante)
tupla,lista,diccionario= (),[],{}

# Recorridos tupla y lista con in
for valor in usuario: print(valor)

#Recorridos listas con enumerate
for i, c in enumerate(materias):print(i,':',c)

# Recorridos diccionario con items
for c, v in estudiante.items(): print(c,':',v)
