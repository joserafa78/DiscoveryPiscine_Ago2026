#!/usr/bin/env python3
# -*- coding: utf-8 -*-
arrayOriginal = [2,8,9,48,8,22,-12,2]
arrayModificado=[]
for caracter in arrayOriginal:
    if caracter >5:
        arrayModificado.append(caracter + 2)
print(arrayOriginal)        
print(set(arrayModificado))

#Usando el nuevo metodo -lista.append()- s
#Usando los Sets para eliminar duplicados
