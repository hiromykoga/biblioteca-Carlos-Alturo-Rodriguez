#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Modulo_Archivo import Archivo
from Modulo_libro import Libro
from Modulo_base_de_datos import Bdd

class CarlosArturoRodriguez():

	def __init__(self):
		self.mensaje = ''

	def guardarLibros(self,rutaExcel):
		"""
		Metodo para guardar el registro de libros en la base de datos
		"""
		print('---------> guardarLibros')
				
		tabla = 'libros'
		archivo = Archivo(rutaExcel)
		hoja = archivo.cargarArchivo()
		arregloRegistroLibros = archivo.convertirExcelEnDiccionario(hoja)
		arregloLibros = []
		for libro_dic in arregloRegistroLibros:
			libro = Libro(1,libro_dic[archivo.columnas[0]],libro_dic[archivo.columnas[1]],libro_dic[archivo.columnas[2]],libro_dic[archivo.columnas[3]],libro_dic[archivo.columnas[4]],libro_dic[archivo.columnas[5]],libro_dic[archivo.columnas[6]],libro_dic[archivo.columnas[7]],libro_dic[archivo.columnas[8]])
			arregloLibros.append(libro)
			
		#for posicion in range(len(arregloLibros)):
		#	print(arregloLibros[posicion].__str__())
			
		bdd = Bdd()
		bdd.insertar(tabla,arregloLibros)




		self.mensaje = 'Archivo guardado exitosamente'
		
		self.mensaje = 'Archivo no guardado'

		return self.mensaje


#----------------------------------------------------
ruta = "hoja_de_vida_libros.xlsx"
escuela = CarlosArturoRodriguez()
mensaje = escuela.guardarLibros(ruta)
print('--------> mensaje:',mensaje)