#Primera prueba de cambios
var = 0

fin = 0

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
    fin = var
    print(fin)
    
print ("Hello Git")