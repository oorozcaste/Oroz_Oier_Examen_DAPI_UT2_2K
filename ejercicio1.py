abizenak = ["oier oroz","aimar itoiz","yoel guimaraes"]
def ListaNombre(lista):
    abizenak = []
    izenak = []
    o = []
    orden = []
    
    
    for i in lista:
        nombres,apellidos = str(i).split(" ")
        o.append(nombres)
        o.append(apellidos)
        abizenak.append(apellidos)
        izenak.append(nombres)
    abizenak.sort()
    for j in abizenak:
        zembakia = int(o.index(j))
        añadir = o.pop([zembakia - 1])
        nombreapellidos = (zembakia,añadir)
        orden.append(nombreapellidos)
    return orden
print(ListaNombre(abizenak))