#final de una compra 

valorcompra= int (input ("ingrese el valor de la compra"))
descuento= int (input ("ingrese el descuento"))
descuento= descuento/100

preciodescuento= valorcompra *descuento

preciofinal= valorcompra-preciodescuento
print("la compra fue: ",valorcompra, "el descuento final es: ", descuento, "el precio final a pagar es:,")
