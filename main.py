from conn import conexion
import os

def menu():

    os.system('clear')
    print(" BIENVENIDO A LA TIENDITA")
    print(" REGISTRO DE PRODUCTO (1) || REGISTRAR COMPRA (2)  || MOSTRAR FACTURAS REGISTRDAS (3)")
    
while True:

    menu()
    numero = int(input("IGRESE LA SELECCION ::: "))

    if numero == 1:
        
        print(" REGISTRO DE PRODUCTO ")

        producto = input("INGRESE PRODUCTO :: ")
        precio = input("INGRESE PRECIO ::")
        
        conexion().registros("""
        
            INSERT INTO productos(producto, precio) VALUES ('{0}','{1}')

        """.format(producto,precio))

    elif numero == 2:

        cont = int(conexion().contador_compra())
        pedido = []
        num_sum = []

        print(" REGISTRO DE COMPRAS Y FACTURA")
        conexion().mostrar_producto("SELECT * FROM productos")
        input()

        
        os.system("clear")
        validar = 1

        while validar == 1:

            codigo = int(input("INGRESE CODIGO DE PRODUCTO :: "))
            cantidad = float(input("INGRESE CANTIDAD :: "))
            
            num_sum.append(cantidad)
            pedido.append((cont, codigo, cantidad))

            validar = int(input("INGRESAR OTRO PRODUCTO SI <1> || NO <0>:: "))
        
        subtotal = sum(num_sum)
        igv = subtotal * 0.18
        total = subtotal + igv

        conexion().registros("""
            INSERT INTO facturas(idcompra, fecha, igv, subtotal, total) VALUES('{0}', current_date, '{1}', '{2}', '{3}')  
        """.format(cont, igv, subtotal, total))
        
        conexion().compra(pedido)

        input()

    elif numero == 3:
        print(":::: MOSTRAR FACTURAS REGISTRADAS :::::")
        
        conexion().mostrar("SELECT * FROM facturas")
        input()
    else:
        menu()