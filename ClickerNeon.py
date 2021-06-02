import keyboard as kb
import pyautogui as pa
import subprocess as sp
import time
import tkinter
from tkinter import messagebox
import os

# Apagado de PC

t = 1
s = ""

def turnoff():
    t = (int (input("¿En cuantos minutos queres que se apague la PC? ")))*60
    
    if t > 1:
        sp.call("shutdown -s -t %d" %t)

        s = str(input("Desea cancelar el apagado? (y/n) "))

        while s != "y" or s != "n":
            s = str(input("Desea cancelar el apagado? (y/n) "))
            if s == "y":
                sp.call("shutdown -a")
                break
            if s == "n":
                break

# Posicionamiento del cursor

def pos():
    print("Tenes 5 segundos para colocar el cursor arriba del boton 'BANK PAY'")
    time.sleep(5)
    print(f"Valor de X e Y: #{pa.position()}")
    print("Tenes 5 segundos para colocar el cursor arriba del boton 'NEW DELIVERY'")
    time.sleep(5)
    print(f"Valor de X e Y: #{pa.position()}")

# Repetidor de clicks

def repetidor():
    xx = int(input("BANK PAY X: "))
    yy = int(input("BANK PAY Y: "))
    xxx = int(input("NEW DELIVERY X: "))
    yyy = int(input("NEW DELIVERY Y: "))
    tiempo = float(input("Ingresa cada cuantos minutos queres que se repita el click"))
    print("Ciera el programa para finalizar")
    while True:
        pa.click(x = xx, y = yy)
        time.sleep(2)
        pa.click(x = xxx, y = yyy)
        time.sleep(tiempo * 60)


print('''
Ingresa la opción que desees:
1. Programar apagado de pc
2. Averiguar donde hacer clicks
3. Setear cada cuanto hacer click
4. Salir
''')

z = 0
while z != 4:
    z = int(input("Ingresa un numero del 1 al 4: "))
    if z == 1:
        turnoff()
    if z == 2:
        pos()
    if z == 3:
        repetidor()      
    if z == 4:
        break




