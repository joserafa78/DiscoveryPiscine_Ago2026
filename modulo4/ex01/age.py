#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    age = int(input("Please tall me your age:"))
    print (f"Your are currently {age} years old.")
    print (f"In 10 years, you will be {age + 10} years old.")
    print (f"In 20 years, you will be {age + 20} years old.")
    print (f"In 30 years, you will be {age + 30} years old.")
except ValueError:
    print("Ingresa con un Número Real,Mamarracho")
