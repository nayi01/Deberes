from typing import DefaultDict

class ciclo:
    def __init__(self,numero=5):
        self.numero=numero
        self.numero2=0

    def usowhile(self):
        # ciclo repetitivo que se ejecuta mientras la condicion se cumpla(verdadero),
        # es decir sale por falso
        car = input("ingrese vocal")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car1 = input("ingrese vocal").lower()
        print("felicitacion su vocal es:{}".format(car))



ciclo1 = ciclo()
ciclo1.usowhile()
print("fin de uso ciclo")