#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conect = sqlite3.connect('pos_empresa.db')

cursor = conect.cursor()
#------------------------------------------------------------------------------------------

print "******Cantidad total de ventas en 2013******" 
cursor = conect.execute("SELECT COUNT(*) FROM sale WHERE date LIKE \"2013%\";")
for row in cursor:
    print ("Venta total del 2013 fue = ",row[0])
    print"-----"

#------------------------------------------------------------------------------------------

print "******Precio promedio de venta por producto******"
cursor = conect.execute("SELECT product.name,AVG(sale_product.net_unit_price) FROM sale_product JOIN product ON product.id = sale_product.product_id GROUP BY product_id LIMIT 5")
for row in cursor:
    print "nombre del producto = " ,row[0]
    print "Precio promedio de venta = ",row[1]
    print"-----"



#-------------------------------------------------------------------------------------------

print "******Total de ventas por cliente******"
cursor = conect.execute("SELECT entity.names,entity.surnames,entity.company_name,SUM(gross_total) FROM sale JOIN entity ON entity.id = sale.entity_id GROUP BY entity_id LIMIT 10;")
print("total de ventas por cliente: ")
for row in cursor:
    print("nombres: ",row[0])
    print("apellidos: ",row[1])
    print("compania: ",row[2])
    print("total de ventas: ",row[3])
    print"-----"



#-------------------------------------------------------------------------------------------

print "******Total de ventas por cliente en año 2014******"
cursor = conect.execute("SELECT entity.names,entity.surnames,entity.company_name,SUM(gross_total) FROM sale JOIN entity ON entity.id = sale.entity_id WHERE sale.date BETWEEN '2014-01-01' AND '2014-12-31' GROUP BY entity_id LIMIT 1;")
print("total de ventas por cliente en el año 2014: ")
for row in cursor:
    print("nombres: ",row[0])
    print("apellidos: ",row[1])
    print("compañia: ",row[2])
    print("total de ventas : ",row[3])
    print"-----"

#--------------------------------------------------------------------------------------------

print "******Cantidad y monto total de ventas por dias en noviembre en 2013******"
cursor = conect.execute("SELECT date, COUNT(*), SUM(gross_total) FROM sale WHERE date LIKE \"2013-11%\" GROUP BY date;")
print ("Total de ventas por fecha en noviembre del 2013:")
for row in cursor:
	print ("Fecha: ",row[0])
	print ("Cantidad de ventas: ",row[1])
	print ("Total ventas: ",row[2])
	print "-----"



#---------------------------------------------------------------------------------------------

print"******Cantidad y montos totales agrupados por producto en orden descendente segun cantidad******"
cursor = conect.execute("SELECT product.name, sale_product.quantity, sale_product.gross_total FROM sale_product JOIN product ON sale_product.product_id = product.id ORDER BY sale_product.quantity DESC LIMIT 5;")
for row in cursor:
 	print "Producto: ",row[0]
 	print "cantidad: ",row[1]
 	print "T.ventas: ",row[2]
 	print "-----"
