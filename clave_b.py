"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


# start-->
def suma(n1, n2, n3):
    result = n1 + n2 + n3
    print(result)


suma(2, 4, 6)


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


# start-->
def sumaImpares():
    result = 0
    for n in range(1, 1001, 2):
        result = result + n
    print(result)


sumaImpares()


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m
perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""


# start-->

pi = 3.141592


def definicionEsfera(radio):
    perimetro = 2 * pi * radio
    area = 4 * radio ** 2 * pi
    volumen = (4 / 3) * pi * radio ** 3
    print(
        "La esfera de radio",
        radio,
        "tiene perimetro de",
        perimetro,
        ", area de",
        area,
        "y volumen de",
        volumen,
    )


definicionEsfera(12)


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase
"""


# start-->
class Esfera:
    pi = 3.141592

    def __init__(self, radio):
        self.__radio = radio

    def obtenerPerimetro(self):
        return self.__radio * 2 * pi

    def obtenerArea(self):
        return self.__radio ** 2 * pi * 4

    def obtenerVolumen(self):
        return self.__radio ** 3 * (4 / 3) * pi

    def definicionEsfera(self):
        result = {
            "perimetro": self.obtenerPerimetro(),
            "area": self.obtenerArea(),
            "volumen": self.obtenerVolumen(),
        }
        print(result)


class Resolucion:
    def __init__(self, operationList):
        self.__operationList = operationList

    def getOperationList(self):
        return self.__operationList

    def definicionEsfera(self):
        operation_list = self.__operationList
        for operation in operation_list:
            operation.showOperaciones()


from clave_b import Esfera
from clave_b import Resolucion


esfera = Esfera(12)
result = esfera.definicionEsfera()
if result == {
    "perimetro": 75.39822368615503,
    "area": 1809.5573684677208,
    "volumen": 7238.229473870882,
}:
    print("ejercicio04: pass")
else:
    print("ejercicio04: fail")


"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:
    def procesar(self):
        return 0

    def abonosSanSalvador(self):
        return 0

    def abonosBalYRod(self):
        return 0


class Cliente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/andresh-2000/Parcial"
