# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:36:48 2023

@author: Fernando
"""
from metodos_ordenamiento_class import Insercion, BurbujaMejorado
from abc import ABC, abstractmethod
from itertools import chain


class ObtenerDiccionario(ABC):
    
    def __init__(self, texto:str):
        self.texto = texto
        self.palabras = []
        
    @abstractmethod
    def limpiar(self):
        pass
    
    @abstractmethod
    def separar(self):
        pass
    
    @abstractmethod
    def ordenar(self):
        pass
    
    @abstractmethod
    def eliminar_duplicados(self):
        pass
        


class Diccionario(ObtenerDiccionario):
    
    def __init__(self, texto:str):
        super().__init__(texto.lower())
        self.limpiar()
        self.separar()
        self.ordenar()
        self.eliminar_duplicados()


    def limpiar(self):
        #Checar el código ASCII para ver qué caracteres se están quitando.
        for i in chain(range(1,32),range(33,65),range(8221,8222)):
            self.texto = self.texto.replace(chr(i),"")
            
    
    def separar(self):
        self.palabras = self.texto.split()
        
    
    def ordenar(self):                           
        Insercion().ordenar(self.palabras)
        #BurbujaMejorado().ordenar(self.palabras)

        
    def eliminar_duplicados(self):                          #O(n^2)
        i = 0
        while i < len(self.palabras):                       #O(n)
            palabra = self.palabras[i]
            j = i+1
            repetido = True
            while j < len(self.palabras) and repetido:      #O(n)
                if self.palabras[j] == palabra:
                    self.palabras.pop(j)
                    j -= 1
                else:
                    repetido = False
                j += 1
            i += 1
        
        
    def __str__(self):
        salida = ""
        for palabra in self.palabras:
            salida += "\n" + palabra 
            
        return salida
    

texto = "Adventures in Disneyland \nTwo blondes were going to Disneyland when they came to a fork in the road. The sign read: ”Disneyland LEFT.” So they went home."

print(Diccionario(texto))
       


    
