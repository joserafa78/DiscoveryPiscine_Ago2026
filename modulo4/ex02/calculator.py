#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    numero1 = int(input("Give me the first number:"))
    numero2 = int(input("Give me the second number:"))
    print("Thank yout")
    print (f"{numero1} + {numero2} = {numero1 + numero2}.")
    print (f"{numero1} - {numero2} = {numero1 - numero2}.")
    print (f"{numero1} / {numero2} = {numero1 / numero2}.")
    print (f"{numero1} * {numero2} = {numero1 * numero2}.")
except ValueError:
    print("Ingresa con un Número Real,Mamarracho")
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
