#ciclo repeticion for -> para
import os
os.system

#for x in range(3):  #la funcion range siempre espera un entero. Siempre parte de 0
    
#   print(f"TONOTOS: {x}")

#cantidad = int(input("ingrese cantidad de notas a promediar: "))

# contadornota = 0

# try:

#  for x in range(cantidad):
#     nota = float(input(f"ingrese nota {x+1}: \n"))
#     contadornota = contadornota + nota
#     promedio = round(contadornota/cantidad)
#     promedioRedondeado = round(promedio,1)

#     print(f"el resultado de las {cantidad} notas es: {promedioRedondeado}")

# except:
#     print("Tipo de dato no es compatible")
    
    
bandera = True

while bandera:
    numero = int(input("ingrese un numero: \n"))
    if numero%2==0:
        print("Puede elegir otro numero.")
    else:
        print("el numero es impar, se acabo el ciclo")
        #bandera = False
        break
print("Muchas gracias por usar la aplición. ")
    
    
    
    

