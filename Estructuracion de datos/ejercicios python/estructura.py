clase sintaxis:
    instancia=0 #atributo de clase

     # __init__ Metodocontructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
     # e iniciar los atributos de la clase. self es un objeto que representa la clase ceada
    def __init__(self,dato="llamando al contructor"):
        self.frase=dato # atributo de instancia
        sintaxis.instancia = sintaxis.instancia+1

print("sintaxis antes de instancia es: {}".format(sintaxis.instancia))
ejer1 = sintaxis() # instancia la clase sintaxis y crea el objeto ejert(copia de la clase)
print("sintaxis de ejer1 es: {}".format(sintaxis.instancia))
ejer2 = sintaxis("instancia2")
print(ejer1.frase)
print("sintaxis de ejer2 es: {}".format(sintaxis.instancia))
print(ejer2.frase)