#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2, psycopg2.extras

class Bdd():
	def __init__(self):
		try:
			self.conecxion = psycopg2.connect("dbname = carlos_arturo_rodriguez user = postgres host = localhost password = 900312")
			#cursor = conecxion.cursor()
			print('conecxion a la base de datos correcta')
		except:
			print('fallo la conecxion a la base de datos')

	def consultar(self,tabla):
		"""
		metodo para el manejo de consultas en la base de datos
		"""
		cursorConsulta = self.conecxion.cursor(cursor_factory = psycopg2.extras.DictCursor)
		sql = "SELECT * FROM %s;"%(tabla)
		cursorConsulta.execute(sql)
		filas = cursorConsulta.fetchall()
		print(filas)

		cursorConsulta.close()
		self.conecxion.close()

	def insertar(self,tabla,arreglo):
		"""
		metodo para el manejo de insercion de datos en la base de datos
		"""
		print("-----------------> insertar")
		accion = "insert"
		cursorInsertar = self.conecxion.cursor()
		for libro in arreglo:
			sql = self.crearQuery(accion,tabla,libro)
			print("")
			print("----> sql 2: ",sql)
			cursorInsertar.execute(sql)

		cursorInsertar.close()
		self.conecxion.commit()
		self.conecxion.close()


	def eliminar(self):
		"""
		metodo para la eliminacion de datos en la base de datos
		"""
		pass

	def  crearQuery(self,tipo_accion,tabla,elemento):
		"""
		metodo que arma el query de las acciones select, update, delete, insert
		"""
		print("-----------------> crearQuery")
		sql = ""
		#llaves = elemento.keys()
		#valores = elemento.values()
		#print(elemento.titulo)
		#print(elemento.autores)

		columnasLibros = ["lib_titulo","lib_autores","lib_editorial","lib_codigo_isbn","lib_cantidad","lib_color_cinta","lib_color_rotulo","lib_clave_coleccion","lib_clave_autor"]
		
		if tipo_accion == "insert":
			if tabla == 'libros':
				sql = """INSERT INTO %s(%s,%s,%s,%s,%s,%s,%s,%s,%s)VALUES('%s','%s','%s','%s',%i,'%s','%s','%s','%s');"""%(tabla,columnasLibros[0],columnasLibros[1],columnasLibros[2],columnasLibros[3],columnasLibros[4],columnasLibros[5],columnasLibros[6],columnasLibros[7],columnasLibros[8],elemento.titulo,elemento.autores,elemento.editorial,elemento.codigo_isbn,elemento.cantidad,elemento.color_cinta,elemento.color_rotulo,elemento.clave_coleccion,elemento.clave_autor)
				
		#print("----> sql: ",sql)
		return sql


#bdd = Bdd()
#bdd.consultar("libros")