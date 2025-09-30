import math
import datetime 
import random as rd

def suma(c,d=10):
    """Esta esta una función para sumar """
    print(f"Hoy estamos a: {datetime.datetime.now()}")
    x= c+d+math.pi
    return x

def resta(c,d):
    print(f" valore aleatorio {rd.randint(3,1000)}")
    x = c-d
    return x


# while True:
#     menu = input("1-Suma\n2-Resta:\n3-Salir\n --> ")
#     a= int(input("ingrese numero 1:"))
#     b= int(input("ingrese numero 2:"))
#     if menu == "1":
#         print(suma(a,b))
#     elif menu == "2":
#         print(resta(a,b))
#     elif menu =="3":
#         break
#     else:
#         print("Opcion correcta")

# def operar(f,f1,y,z):
#     return f(f(y,z),f1(y,z))



# help(suma)


# print("SOLICITANDO VALORES PARA LAS OPERACIONES ")

hola = suma
h = hola(456)
print(h)
h1 = resta(45,23)
print(h1)

# # print(operar(suma,resta,a,b))

# print(f"el reultado en la suma es:{h}")
# print(f"el reultado en la resta es:{h1}")

# k = []

# for i in range(3):
#     k.append(h/h1) 
    
    
# print(k)





# print(f"El resultado de la suma fue: 😎🤘: {suma()}")
# print(f"El resultado de la resta fue: 😎🤘: {resta()}")
