# Laboratorio #2, Fundamentos de Programación - V2

'''Desarrollar un programa que solicite tres números enteros desde teclado al usuario, luego el programa deberá determinar e indicar a 
través de un mensaje en pantalla, cuál de los tres es el más grande sin importar el orden que se ingrese los números, así mismos el número 
más pequeño y el número de en medio.
Requerimientos
El mensaje en pantalla deberá mostrar el número que resulto ser el más grande, mediano, pequeño de los tres, por ejemplo: 3, 7, 8
“El número 8 es el número más grande de los tres”
“El número 3 es el número más pequeño de los tres”
“El número 7 es el número de en medio de los tres”.'''

# Mensaje de bienvenida.
print("\033[1m"+"\nBienvenid@ al desarrollo del codigo perteneciente al laboratorio #2, Fundamentos de Programación - V2.\n"+"\033[0m")

# Variables que capten los numeros enteros ingresados por el usuario.

num1 = int(input("Ingrese el primer número entero. -> "))
num2 = int(input("Ingrese el segundo número entero. -> "))
num3 = int(input("Ingrese el tercer número entero. -> "))

if num1 > num2 and num1 > num3 and num2 > num3:
    print(f"\nEl número {num1} es el número mas grande de los tres.")
    print(f"El número {num2} es el número de en medio de los tres.")
    print(f"El número {num3} es el número mas pequeño de los tres.")

elif num1 > num2 and num1 > num3 and num3 > num2:
    print(f"\nEl número {num1} es el número mas grande de los tres.")
    print(f"El número {num3} es el número de en medio de los tres.")
    print(f"El número {num2} es el número mas pequeño de los tres.")

elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f"\nEl número {num2} es el número mas grande de los tres.")
    print(f"El número {num1} es el número de en medio de los tres.")
    print(f"El número {num3} es el número mas pequeño de los tres.")

elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f"\nEl número {num2} es el número mas grande de los tres.")
    print(f"El número {num3} es el número de en medio de los tres.")
    print(f"El número {num1} es el número mas pequeño de los tres.")

elif num3 > num1 and num3 > num2 and num2 > num1:
    print(f"\nEl número {num3} es el número mas grande de los tres.")
    print(f"El número {num2} es el número de en medio de los tres.")
    print(f"El número {num1} es el número mas pequeño de los tres.")

elif num3 > num1 and num3 > num2 and num1 > num2:
    print(f"\nEl número {num3} es el número mas grande de los tres.")
    print(f"El número {num1} es el número de en medio de los tres.")
    print(f"El número {num2} es el número mas pequeño de los tres.")

else:
    print("Asegurate de ingresar números enteros.")

# Mensaje que indica el fin del programa.
print("\033[1m"+"\nFin del programa.\n"+"\033[0m")