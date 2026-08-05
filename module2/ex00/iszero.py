#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    numero = int(  input("ingrese un numero: "))
    if numero == 0:
        print ("This number is equal to zero")
    else :
        print ("Thisidd number is different from zero.")

except ValueError:
        print ("Ingresa un Númer valido, mamaracho")
