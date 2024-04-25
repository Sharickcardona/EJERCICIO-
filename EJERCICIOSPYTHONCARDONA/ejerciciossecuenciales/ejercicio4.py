#hallar cada procedimiento 
sueldo = 600000
comisiones = 500 
tcomosiones = 0 
ventas = 0
total = 0 

nombre = str (input (" digite el vendedor ") )

ventas  = int ( input ( " digite la cantidad de venta") )

tcomisiones = ventas*comisiones 
total= tcomisiones+sueldo 

print ( f" el venderdor {nombre}, tiene un sueldo de {sueldo}, durante el mes obtuvo una comision de {tcomisiones} y el valor final a pagar es {total}"  )

