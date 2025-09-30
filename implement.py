from ejemC10 import *
# from ejemC10 import suma,resta
# import ejemC10 as ej10

while True:
    menu = input("1-Suma\n2-Resta:\n3-Salir\n --> ")
    a= int(input("ingrese numero 1:"))
    b= int(input("ingrese numero 2:"))
    if menu == "1":
        print(suma(a,b))
    elif menu == "2":
        print(resta(a,b))
    elif menu =="3":
        break
    else:
        print("Opcion correcta")

def operar(f,f1,y,z):
    return f(f(y,z),f1(y,z))