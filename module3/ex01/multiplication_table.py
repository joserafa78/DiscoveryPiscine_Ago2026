#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
def imprimefila(num1,num2):#funcion que hace el calculo.
	resultado = num1*num2
	print(f"{num1} x {num2} = {resultado}")
	
try:
	numero=int(input("Ingrese un Numero:"))
	fila = 0
	while fila <10:
		imprimefila(fila,numero)
		fila += 1
except ValueError:
	print("Gran Error,Por Odin, Uste no ha ingresado valor Numerico,CHAO!!!")