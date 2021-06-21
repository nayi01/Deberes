class for:
    def __init__(self):
        pass
    def usofor(self):
        #ciclo repetivo de incrementos o decrementos se ejecuta por verdadero
        nombre="Daniel"
        datos=["Daniel",50,True]
        numeros=(2,5.6,4,1)
        docente={'nombre': 'daniel', 'edad': 50, 'fac': 'faci'}
        listanotas = [(30,40),(20,40,50),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"yady","fianl":60}{"nombre":"Danny","fianl":90}]
        # range([inicio=0],limite,[inc/dec=1]). Genera un rango de valores desde un valor inicial a un valor final
        # se ejecuta desde inicio hasta el limite
        # for con range() o for con colecciones
        j=0
        while j<5:
            print('while',j)
             j=+1
        for i in range(5): # rango(0,1,2,3,4)
            print('for',i,end=" ")
        print()
        for i in range(1,5): # rango(1,2,3,4)
            print('for',i,end=" ")
        print()
        for i in range(2,10,2): # rango(2,4,6,8)
            print('for',i,end=" ")
        print()
        for i in range(12,3,+3): rango (12,9,6)
            print('for',i,and=" ")

        lon = len(numeros)
        for pos in range(lon):
            if pos%2 == 0 and pos !=0:
            print(pos,numeros[pos])
        
        # vocal = ('a','e','i','o','u')
        for elem in datos:
            print(elem,end=" ")
        for elem in nombre:
            print(elem,end=" ")
        
        lon = len(datos)
        for pos in range(lon):
            print(pos,datos[pos])

        for pos,valor in enumerate(datos):
            print(pos,valor)

        for clave,valor in docente.items():
            print(clave,valor,end=" ")

        print(listanotas)
        for notas in listanotas:
            print("for externo",notas)
            for nota in notas:
                print(nota,end=" ")
            print("saliendo del for interno")

        #promedio    
        print(listanotas)
        for notas in listanotas:
            acum=0
            for nota in notas:
                acum=acum+nota
            print(acum/len(notas),end=" ")

        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"yady","fianl":60}{"nombre":"Danny","fianl":90}]
        print("\ndisccionario de alumnos")
        print(listaAlumnos)
        acum=0
        for alumnos in listaAlumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor,valor,end=" ")
                if clave == 'final':
                    acum=acum+valor
            print()
        print("promedio",acum/len(listaAlumnos))

        listanotas = [(30,40,10,20),(20,40,50),(50,40,10)(10,20)]
        acum,cont=0,0
        for notas in listanotas:
            print(notas)
            acumparcial=0
            contparcial=0
            for notas in notas:
                acumparcial += nota
            acum= acum+acumparcial
            print("totalparcial:{} promparcial:{}".formt(acumparcial,acumparcial/len(notas))
        print("totalparcial:{} promparcial:{}".formt(acum,acum/cont))
                acum=acum+nota
                
        print(acum/cont)
bucle = for()
bucle.usofor()
