# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from abc import ABC, abstractmethod

class Usuario(ABC):
    
    def __init__(self, edad:int, fumador:str, extra_prima:str,\
                 suma_asegurada:float):
        
        self.edad = edad
        self.x = self.edad
        self.f = fumador
        self.ep = extra_prima
        self.sa = suma_asegurada
        self.k : float
        self.p : float
        self.factor_de_edad()
        
    
    def validar_edad(self):
        return self.edad >= 18 and self.edad <= 99
    
    def validar_sa(self):
        return 500000 <= self.sa <= 3000000
    
    def set_edad(self, edad:int):
        self.edad = edad
    
    def set_sa(self, sa:float):
        self.sa = sa
    
    
    def calcular_edad(self):
        if self.f == "No":
            self.x -= 5
            
        if self.ep == "Si":
            self.x += 10
        
        if self.x < 18:
            self.x = 18
        
        if self.x > 99:
            self.x = 99
            
            
    @abstractmethod
    def factor_de_edad(self):
        pass
            
    
    def calcular_prima(self):
        self.p = (self.sa * self.k) / 1000
    
    @abstractmethod
    def __str__(self):
        pass
        
            

class Femenino(Usuario):
    
    def __init__(self, edad:int, fumador:str, extra_prima:str,\
                 suma_asegurada:float):
        
        super().__init__(edad, fumador, extra_prima,\
                     suma_asegurada)
        self.x += 10
        
            
    def factor_de_edad(self):
        self.calcular_edad()
        if self.x in range(18,25):
            self.k = 1.5
        elif self.x in range(25,45):
            self.k = 1.7
        elif self.x in range(45,65):
            self.k = 2
        else:
            self.k = 2.2
    
    
    def __str__(self):
        return "Asegurada:\n\n" +\
                f"Género: F\n" +\
                f"Edad: {self.edad}\n"+\
                f"Fumador: {self.f}\n"+\
                f"Extra-prima: {self.ep}\n\n"+\
                "-"*30 + "\n"\
                f"Suma asegurada: {self.sa:,.2f}\n"+\
                f"Prima: {self.p/21.13:,.2f} DLS"
        
        
class Masculino(Usuario):
    
    def __init__(self, edad:int, fumador:str, extra_prima:str,\
                 suma_asegurada:float):
        
        super().__init__(edad, fumador, extra_prima,\
                     suma_asegurada)
            
            
    def factor_de_edad(self):
        self.calcular_edad()
        if self.x in range(18,25):
            self.k = 2
        elif self.x in range(25,45):
            self.k = 2.3
        elif self.x in range(45,65):
            self.k = 2.5
        else:
            self.k = 3
    
        
    def __str__(self):
        return "Asegurado:\n\n" +\
                f"Género: M\n" +\
                f"Edad: {self.edad}\n"+\
                f"Fumador: {self.f}\n"+\
                f"Extra-prima: {self.ep}\n\n"+\
                "-"*30 + "\n"\
                f"Suma asegurada: {self.sa:,.2f}\n"+\
                f"Prima: {self.p/21.13:,.2f} DLS"
        



"""
NOTA:
    Ya no hice el script de prueba como debería, pero las clases están construidas.
"""


def calcular_prima():
    edad = 20
    fumador = "No"
    extra_prima = "Si"
    suma_asegurada = 1989000.0
    sexo = "F"
    
    if sexo == "F":
        seguro = Femenino(edad, fumador, extra_prima,\
                     suma_asegurada)

        while not seguro.validar_edad() or not seguro.validar_sa():
            
            if not seguro.validar_edad():
                print("Tu edad debe estar entre 18 y 99 años")
                edad = int(input("Ingresa una edad válida: "))
                print("\n\n" + "-"*40)
                seguro.set_edad(edad)
            else:
                print("La Suma Asegurada debe estar entre 500,000 y 3,000,00")
                sa = float(input("Ingresa una Suma Asegurada válida: "))
                print("\n\n" + "-"*40)
                seguro.set_sa(sa)
        
        seguro.calcular_prima()
        
        print(seguro)
        
    else:
        seguro = Masculino(edad, fumador, extra_prima,\
                     suma_asegurada)

        while not seguro.validar_edad() or not seguro.validar_sa():
            
            if not seguro.validar_edad():
                print("Tu edad debe estar entre 18 y 99 años")
                edad = int(input("Ingresa una edad válida: "))
                print("\n\n" + "-"*40)
                seguro.set_edad(edad)
            else:
                print("La Suma Asegurada debe estar entre 500,000 y 3,000,00")
                sa = float(input("Ingresa una Suma Asegurada válida: "))
                print("\n\n" + "-"*40)
                seguro.set_sa(sa)
        
        seguro.calcular_prima()
        
        print(seguro)

calcular_prima()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    