puntuacion_x_rol_turno = 5
puntuacion_x_rol_sucursal = 2.5

#Aqui ingresamos los datos del usuario

while True:
    hay_faltas = input("Tienes faltas en el rol?(si/no): ").lower()
    if hay_faltas == "si":
        hay_faltas = (int(input("Cuantas faltas tienes?(1,2,3...): "))) * 10
        if hay_faltas > 4:
            hay_faltas = 40
            break
    elif hay_faltas == "no":
        hay_faltas = 0
        break
    else:
        print("Error: ingresa si o no")

while True:
    hay_retardos = input("Tienes retardos en el rol?(si/no): ").lower()
    if hay_retardos == "si":
        hay_retardos = (int(input("Cuantas retardos tienes?(1,2,3...): "))) * 10
        if hay_retardos > 2:
            hay_retardos = 20
            break
    elif hay_retardos == "no":
        hay_retardos = 0
        break
    else:
        print("Error: ingresa si o no")

while True:
    hay_faltantes = input("Tuviste faltantes de dinero en tu anterior rol?(si/no): ")
    if hay_faltantes == "si":
        faltante = int(input("Cual es la suma de todos tus faltantes juntos?($$$ sin centavos): "))
        if faltante > 500:
            faltante = 6
            break
        elif faltante > 100:
            faltante = 4
            break
        else:
            faltante = 1
            break
    elif hay_faltantes == "no":
        faltante = 0
        break
    else:
        print("Error: ingresa si o no")

while True:
    hay_actas = input("Tienes actas administrativas?(si/no): ")
    if hay_actas == "si":
        actas = int(input("Cuantas veces firmaste actas administrativas?(1,2,3...): "))
        if actas > 3:
            actas = 9
            break
        elif actas > 2:
            actas = 6
            break
        else:
            actas = 3
            break
    elif hay_actas == "no":
        actas = 0
        break
    else:
        print("Error: ingresa si o no")

anios_trabajando = int(input("Cuantos años cumplidos tienes en la empresa?: "))
if anios_trabajando > 10:
    anios_trabajando = 10

roles_en_turno = int(input("¿Cuantos roles llevas en el mismo turno(máx 2): "))
if roles_en_turno > 2:
    roles_en_turno = 2

roles_en_sucursal = int(input("Cuantos roles llevas cumplidos en la misma sucursal(máx 4)"))
if roles_en_sucursal > 4:
    roles_en_sucursal = 4

#Aqui definimos a cuanto equivalen los valores ingresados en calificacion
asistencia = 40 - hay_faltas
puntualidad = 20 - hay_retardos
meritos = 15 - actas - faltante
antiguedad_empresa = anios_trabajando * 0.5
antiguedad_turno = puntuacion_x_rol_turno * roles_en_turno
antiguedad_sucursal = puntuacion_x_rol_sucursal * roles_en_sucursal

calificacion_total = asistencia + puntualidad + meritos + antiguedad_empresa + antiguedad_turno + antiguedad_sucursal

print({asistencia})
print({puntualidad})
print({meritos})
print({antiguedad_empresa})
print({antiguedad_turno})
print({antiguedad_sucursal})
print(f"Tu calificación total en este rol es: {calificacion_total}!")