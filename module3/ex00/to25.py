#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def imprimehasta25 (valor):
	while valor <=25:
		print (f"Numero:{valor}")
		valor= valor +1

try:
	num1=float(input("Ingrese el Numer:"))
	if num1 >25:
		print("Error")
	else:
		imprimehasta25(num1)

except ValueError:
