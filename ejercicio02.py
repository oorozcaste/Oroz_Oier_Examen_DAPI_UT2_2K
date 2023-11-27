clase = {}
izenak = []
while True:
    x = input("elija una opcion del sigueinte menu: (1) Añadir alumno, (2) Numero de aprobados, (3) Mostrar todo el alumando: ")
   
    
    if x == "1":
        nombre = input("dime el nombre del alumno: ")
        aprobado = input("ha aprobado el modulo? (si/no): ")
        izenak.append(nombre)
        if aprobado == "si":
            gainditua = "si"
        elif aprobado == "no":
            gainditua = "no"
        clase[nombre] = gainditua
    if x == "2":
        p = 0
        for i in clase.values():
            if i == "si":
                p = p + 1
        zembakia = p
        print("el numero de aprobados es de ",zembakia)
    if x == "3":
        print(izenak)