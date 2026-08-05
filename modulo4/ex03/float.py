#!/usr/bin/env python3
# -*- coding: utf-8 -*-
numero = int(input("Give me a number:"))
tipo= type(numero)
if tipo == int:
    print(f"The number {numero} is an Integer.")
if tipo == float:
    print(f"The number {numero} is a Float.")
if tipo == str:
    print(f"The number {numero} is a String.")
    
  
  
  
