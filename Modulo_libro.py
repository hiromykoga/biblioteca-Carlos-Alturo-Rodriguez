#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Libro():
	def __init__(self,identificador,titulo,autores,editorial,codigo_isbn,cantidad,color_cinta,color_rotulo,clave_coleccion,clave_autor):
		self.identificador = identificador
		self.titulo = titulo
		self.autores = autores
		self.editorial = editorial
		self.codigo_isbn = codigo_isbn
		self.cantidad = cantidad
		self.color_cinta = color_cinta
		self.color_rotulo = color_rotulo
		self.clave_coleccion = clave_coleccion
		self.clave_autor = clave_autor
	def __str__(self):
		#la linea identificador tiene esa identacion para que este alineada con los demas elementos cuando se visualiza el print
		libro = """					identificador: %i
					titulo: %s
					autores: %s
					editorial: %s
					codigo isbn: %s
					cantidad: %i
					color cinta: %s
					color rotulo: %s
					clave coleccion: %s
					clave autor: %s
				"""%(self.identificador,self.titulo,self.autores,self.editorial,self.codigo_isbn,self.cantidad,self.color_cinta,self.color_rotulo,self.clave_coleccion,self.clave_autor)
		return libro


#obj_libro = Libro(1,"LA VUELTA AL MUNDO EN OCHENTA CUENTOS","Albert Jané","Perspectiva Editorial Cultura S. A.","978-958-46-0834-5",1,"Amarillo","Verde","C","JAN1")
#libro = obj_libro.__str__()
#print libro
