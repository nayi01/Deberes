class condicion:

    def __init__(self,num1,num2):
         self.numero1=num1
         self.numero2=num2
         numero=self.numero1+self.numero2
         self.numero3=numero

    def usolf(self):
         # if ... elif... else...:permiten condicionar la ejecucion de uno o varios bloques
         # sentencias al cumplimiento de una o varias condiciones.
        if self.numero1 == self.numero2:
             print("numero1={}=numero2={}: son iguales".format(self.numero,self.numero2))
        elif self.numero1 == self.numero3:
             print("numero1 y numero3 son iguales")
        else:
             print("numeros diferentes")
        print("fin if")

# print("instancia de la clase")
# cond2= condicion()
# print(cond2.numero3)
# cond2.usolf()
cond1 = condicion(10,20)
cond1.usolf()
print("gracias por su visita")