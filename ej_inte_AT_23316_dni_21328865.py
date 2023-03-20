import math
import re
""" 
EJERCICIOS INTEGRADORES PYTHON

"""
#Ejercicio 1 Funcion que calcule el maximo comun divisor entre dos numeros

print("Ejercicio 1")
a = 10
b = 70
def maxComDen(a,b):
    mcd = math.gcd(a,b)
    return mcd
#a = int(input("Ingrese un numero entero: ")) 
#b = int(input("Ingrese otro numero entero: ")) 
mcd = maxComDen(a,b)
print(f"El maximo comun denominador entre: {a} y {b} es {mcd}")



# Ej. 2 Funcion  que calcule el minimo comun multiplo entre dos numeros
# mcm es el menor numero positivo que es multipolo de 2 numeros
print("Ejercicio 2")
def minComMul(a,b):
    #calculo el numero mas gde entre los 2
    num_mayor = max(a,b)
    while True:
        if(num_mayor % a == 0) and (num_mayor % b ==0):
            return num_mayor 
        num_mayor += 1

#a = int(input("Ingrese un numero entero: ")) 
#b = int(input("Ingrese otro numero entero: ")) 
a = 34
b = 45
mcm = minComMul(a,b)
print(f"El minimo comun multiplicador entre: {a} y {b} es {mcm}")

#ej 2 otra variante MCM(a, b) = (a * b) / MCD(a, b)
# multiplicar a * b y dividir este resultado entre el maxComDen(a,b)
def mcm(a,b):
    mcm = (a*b)/maxComDen(a,b)
    return mcm
a = 34
b = 45
mcm = mcm(a,b)
#a = int(input("Ingrese un numero entero: ")) 
#b = int(input("Ingrese otro numero entero: ")) 
print(f"El minimo comun multiplicador entre: {a} y {b} es {mcm}")



""" Ej 3 y 4. Programa que recibe una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra funcion que reciba el diccionario generado con la funcion anterior y devuelva una tupla con la palabra mas repetida y su frecuencia"""

print("Ejercicio 3 y 4")

def dic_con_frecuencia(cadena):
    remover = ".,:;?=/#%\n!\"'"
    for caracter in remover:
        cadena = cadena.replace(caracter, "")
    cadena = cadena.lower()
    palabras = cadena.split()
    dic_frecuencia = {}
    for palabra in palabras:
        if palabra in dic_frecuencia:
            dic_frecuencia[palabra]  += 1
        else:
            dic_frecuencia[palabra] = 1

    print(dic_frecuencia)
    for palabra in dic_frecuencia:
        frecuencia = dic_frecuencia[palabra]
        print(f"La palabra '{palabra}' tiene una frecuencia de: {frecuencia}")
    return dic_frecuencia
cadena = input("Ingrese una cadena de caracteres:")

#print (cadena.split())
#print(type(cadena))
dic_con_frecuencia(cadena)
diccionario = dic_con_frecuencia(cadena)
print(diccionario)
def palabra_mas_repetida(diccionario):
    palabra_max = max(diccionario, key=diccionario.get)
    return (palabra_max, diccionario[palabra_max])
   # palabra_max = max(diccionario.keys(), key=lambda k: diccionario[k])
    #return print(palabra_mas)

p_m_r = palabra_mas_repetida(diccionario)
print (f"La mas repetida:  {p_m_r}")
#p_max = max(diccionario.items())
#return tuple(p_max)


""" 
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.
"""

print("Ejercicio 5")

def get_int():
     #ingreso de numero int si no vuelve a solicitarlo
     while True:
          valor = input("Ingrese un numero entero: ")
          try:
               valor = int(valor)
               return valor
          except ValueError:
               print ("ATENCION! Debe ingresar un numero entero:")

print("Ingreso el numero: ", get_int())


"""
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
"""

print("Ejercicio 6")
class Persona:
    def __init__(self, nombre=" ", edad = 0, dni = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        #self.mostrar()
        #self.es_mayor_de_edad()
#getters
    @property
    def nombre(self):
        return self.__nombre
    @property

    def edad(self):

        return self.__edad
    @property
    def dni(self):
        return self.__dni
    
    #setters
    @nombre.setter
    def nombre(self,nuevo_nombre):
        while True:
            if (re.search("[a-zA-Z|ñÑ ]", nuevo_nombre) is not None):
                self.__nombre = nuevo_nombre
                return print("Nombre cargado correctamente")
            else:
                self.__nombre = ""
                return print("Error al cargar nombre valido")

    @edad.setter
    def edad(self,nueva_edad):
        try:
            if nueva_edad > 0 and nueva_edad < 100:
                self.__edad = nueva_edad
            else:
                self.__edad = 0
                return print("Error. Ingrese una edad valida")
        except ValueError:
            self.__edad = 0
            return print("Error en ingreso de edad. Introduzca números.")

        #assert nueva_edad >= 18
        # self.__edad = nueva_edad
    @dni.setter
    def dni(self,nuevo_dni):
        try:
            if len(nuevo_dni) < 9 and len(nuevo_dni) > 6:
                self.__dni = nuevo_dni
                return print("DNI cargado correctamente") 
            else:
                self.__dni = 0
                return print("El DNI debe tener entre 7 y 8 numeros sin puntos.")  
        except ValueError:
            self.__dni = 0
            return print("Error al cargar DNI. Ingrese un numero valido sin puntos") 
        

    def mostrar(self):
        cadena = "Nombre: " + self.nombre + "Edad: " + str(self.edad) + " DNI: " + str(self.dni)
        return cadena
    
    def es_mayor_de_edad(self, edad):
        if edad >= 18:
            return True
        else:
            return False
        # return self.__edad >= 18 
persona_1 = Persona("Anto", 21, 21328865)
print(f"Nombre: {persona_1.nombre}")
print(f"Edad: {persona_1.edad} años")
print(f"DNI: {persona_1.dni}")
print(persona_1.mostrar())
edad = persona_1.edad
es_mayor = persona_1.es_mayor_de_edad(edad)
print(f"El titular {persona_1.nombre} es mayor de edad?: {es_mayor}")
"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:  Un constructor, donde los datos pueden estar vacíos.  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.  mostrar(): Muestra los datos de la cuenta.  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

"""
print("Ejercicio 7")
class Cuenta():
    def __init__(self, titular, cantidad = 0.0):
        self.__titular = Persona (titular.nombre, titular.edad, titular.dni)
        self.__cantidad = cantidad
#getter
    @property
    def titular(self):
        return self.__titular
   
    @titular.setter
    def titular(self,titular):
        self.__titular = titular   
    @property
    def cantidad(self):
        return self.__cantidad
   
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        return "Datos de la Cuenta:\n" + "Titular: " + self.titular.nombre + "\n" + "Cantidad en cuenta: $ " + str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self,cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad - cantidad

cuenta = Cuenta(persona_1, 2000)
print(cuenta.mostrar())
deposito = 200
deposita = cuenta.ingresar(deposito)
print(f"El cliente {persona_1.nombre} deposito: $ {deposito} Saldo: $ {cuenta.cantidad}")
retiro = 100
retirar = cuenta.retirar(retiro)
print(f"El cliente {persona_1.nombre} retiro: $ {retiro} Saldo: $ {cuenta.cantidad}")


"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:  Un constructor.  Los setters y getters para el nuevo atributo.  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
"""
print("Ejercicio 8")

class CuentaJoven(Cuenta):
    def __init__(self,titular, cantidad, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def mostrar(self):
        return "Datos de la Cuenta:\n" + "Titular: " + self.titular.nombre + " Cantidad: $" + str(self.cantidad) + " Bonificacion: " + str(self.bonificacion) + "%"
    
    def es_titular_valido(self):
        return self.titular.edad >= 18 and self.titular.edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Usted no puede retirar el dinero porque no es un titular  valido")

persona_2 = Persona ("Josefina Correa", 24, 69698698698)
cuenta_joven = CuentaJoven(persona_2, 1000, 20)
tit_val = cuenta_joven.es_titular_valido()
print(f"El titular {persona_2.nombre} es valido?: {tit_val}")
print(cuenta_joven.mostrar())
print(cuenta_joven.retirar(100))
print(cuenta_joven.mostrar())


