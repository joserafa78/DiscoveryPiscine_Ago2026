#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
def caracteresMultiplicados(numero):#funcion que hace el calculo.
    texto = ""
    multiplica = 0
    num=0
    while num <=10:
        multiplica = num * numero
        texto += f"{str(multiplica)}  "
        num += 1
        
    return texto
	
fila = 0
while fila <=10:
    print(f"Table of {fila}: {caracteresMultiplicados(fila)}")
    fila += 1