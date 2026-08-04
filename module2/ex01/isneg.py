#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    numero = int (input("Ingres un Número:"))
    if numero > 0:
        print("This number is positive.")
    if numero < 0:
        print("This number is negative.")
    if numero == 0:
        print("This number is both positive and negative.")

except ValueError:
    print("Ingresa con un Número Real,Mamarracho")
