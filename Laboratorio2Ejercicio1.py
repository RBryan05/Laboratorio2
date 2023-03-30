# Laboratorio #2, Fundamentos de Programación - V2

''' 1. Construye un programa que, registe que un policía de tránsito reporta a la central un promedio de N infracciones 
en el mes de las cuales el 20% se producen en las horas de la mañana, el 35% se producen en horas de la tarde y el 45% 
restante se producen en horas de la noche. Realizar un programa que calcule e imprima lo siguiente.
Promedio diario matutino de infracciones
Promedio diario vespertino de infracciones
Promedio diario nocturno de infracciones'''


# Mensaje de bienvenida.
print("\033[1m"+"\nBienvenid@ al desarrollo del codigo perteneciente al laboratorio #2, Fundamentos de Programación - V2.\n"+"\033[0m")

# Variable que capte los datos ingresados por el usuario.
inf = int(input("Ingrse el numero de infracciones que registro durante el mes. -> "))

# Promedio matutino
matu = inf*0.2

print(f"\nEl promedio diario matutino de infracciones es de: {matu}")

# Promedio vespertino.
vesp = inf*0.35

print(f"\nEl promedio diario vespertino de infracciones es de: {vesp}")

# Promedio nocturno.
noc = inf*0.45

print(f"\nEl promedio diario nocturno de infracciones es de: {noc}")

# Mensaje que indica el fin del programa.
print("\033[1m"+"\nFin del programa.\n"+"\033[0m")