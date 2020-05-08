import psycopg2
import psycopg2.extensions
import sys

class conexion():

    def __init__(self, server='localhost', user='postgres', password='199705', database='tienda'):
        self.db = psycopg2.connect(host=server, user=user, password=password, database=database)
        self.cursor = self.db.cursor()

    def registros(self, sql, parametro=None):
        self.cursor.execute(sql)
        self.db.commit()

    def contador_compra(self, parametro=None):
        self.cursor.execute("select * from compras ORDER BY cont DESC LIMIT 1")
        cont = self.cursor.fetchone()
        cont = cont[1] + 1
        return cont
    
    def compra(self, pedido):
        self.cursor.executemany("INSERT INTO compras(cont, idproducto, cantidad) VALUES ('%s', '%s','%s')",pedido)
        self.db.commit()

    def cerrar_conexion(self):
        self.db.close()
        print("desconectado")
    
    def rollback(self):
        self.db.rollback
        return True

    def mostrar_producto(self, sql):
        self.cursor.execute(sql)
        tabla = self.cursor.fetchall()
        for lista in tabla:
            print("CODIGO :: {0}, PRODUCTO :: {1}, PRECIO :: $ {2}".format(lista[0], lista[1], lista[2]))

    def mostrar(self, sql):
        self.cursor.execute(sql)
        tabla = self.cursor.fetchall()
        for lista in tabla:
            print(""" 
                CODIGO DE VENTA : {0}
                FECHA : {1}
                IGV : {2}
                SUBTOTAL : {3}
                TOTAL : {4}
            """.format(lista[1], lista[2], lista[3], lista[4], lista[5]))