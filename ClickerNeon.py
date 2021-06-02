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
    print("Tenes 5 segundos para colocar el cursor arriba del boton 'START NEW SHIFT'")
    time.sleep(6)
    print(f"Valor de X e Y (New Shift): #{pa.position()}")
    print("Tenes 5 segundos para colocar el cursor arriba del boton 'BANK PAY'")
    time.sleep(6)
    print(f"Valor de X e Y (Bank Pay): #{pa.position()}")

# Repetidor de clicks

def repetidor():
    xxx = int(input("NEW SHIFT X: "))
    yyy = int(input("NEW SHIFT Y: "))
    xx = int(input("BANK PAY X: "))
    yy = int(input("BANK PAY Y: "))
    tiempo = float(input("Ingresa cada cuantos minutos queres que se repita el click"))
    print("Cierra el programa para finalizar")
    while True:
        pa.click(x = xxx, y = yyy)
        time.sleep(2)
        pa.click(x = xx, y = yy)
        time.sleep(tiempo * 60)


print('''
Ingresa la opción que desees:
1. Programar apagado de pc
2. Averiguar donde hacer clicks
3. Setear donde y cada cuanto hacer click
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
