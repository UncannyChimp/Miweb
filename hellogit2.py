#Primera prueba de cambios
comp = 10

var = 0

fin = 0

otro = 0

veces = input("Cuantas veces quieres mostrar: ")

try: 
    veces = int(veces)
except:
    veces = "Equivocado"

    if veces=="Equivocado":
        print("El valor esta equivocado")
        exit()

while fin < veces:
    var = var + 1

    while comp > 1:
    otro = var / 3
    print comp
    exit()

    fin = var
    print(fin)

    print ("Hello git 2")

print ("Hello Git 3")