#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def analizaResultado (valor):
	if valor > 0:
		print("The result is positive")
	if valor < 0:
		print ("The result es negative")
	if valor == 0:
		print ("The resultado es Zero")


try:
	num1=int(input("Ingrese el Numero Uno:"))
	num2=int(input("Ingrese el Numero Dos:"))
	resultado=num1*num2
	print(f"Los valores son: {num1} x {num2} = {resultado} ")
	analizaResultado(resultado)

except ValueError:
	print("Gran Error,Por Odin, Uste no ha ingresado valor Numerico,CHAO!!!")
