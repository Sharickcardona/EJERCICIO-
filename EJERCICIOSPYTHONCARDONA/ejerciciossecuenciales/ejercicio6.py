#declararvariables
nombre= str(input ("digite su nombre :"))
n1 = float (input ("inserte el promedio de notas:"))
n2 = float (input ("ingrese la nota del proyecto"))
n3 = float (input ("ingrese el promedio de evaluaciones"))

prom1 = n1 * 0.3
prom2 = n2 * 0.5
prom3 = n3 * 0.2
total = prom1 + prom2 + prom3

print ( f"la nota final de {nombre}es de {total}")

