#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    numero = float(input("Give me a number:"))
    residuo= numero % 1
    if residuo == 0:
        print(f"The number {numero} is an Integer.")
    else:
        print(f"The number {numero} is a Float.")

except ValueError:
    print("Ingresa con un Número Real,Mamarracho") 
  