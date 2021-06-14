def usovariables(self):
    edad,_peso =50, 70.5
    nombres = 'Daniel vera'
    car = nombres[0]
    tipo_sexo = 'M'
    civil = True
    #tuplas = () son son colecciones de datos de cualquier tipo inmutables
    usuario=()
    usuario = ('dchiki','1234','chiki@gmail.com')
    print(usuario[2],nombres[7])
    #usuario[3] = "milagro"
    #listas = [] colecciones mutables
    materias = []
    materias = ['programacion web', 'php', 'poo']
    aux=materias[1]
    materias[1]="python"
    materias.append("Go")
    print(materias,aux,materias[1])
    # diaccionario = {} colecciones de objetos clave: valor tipo json
    docente = {}
    docente = {'nombre': 'daniel', 'edad': 50, 'activo': True}
    edad = docente ['edad']
    docente = ['edad']=51
    docente = ['carrera']='IS'
    #print(docente,edad,docente['edad'])
    print(usuario,usuario[0],usuario[0:2],usuario[-1])
    print(nombres,usuario[0],usuario[0:2],usuario[-1])
    print(materias,materias[2:],materias[:3],materias[::-1],materias[-2:])
    #presentacion con format
    print("""mi nombre es {}, tengo {}
         años""".format(nombres, edad))
