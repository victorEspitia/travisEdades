##
import unittest
from Edad import Edad
class FugurasTest(unittest.TestCase):

	def setUp(self):
		self.edad = Edad()

	def test_edad_prueba1(self):
		self.edad.calcular_edad(0)
		self.assertEquals(self.edad.obtener_edad(), 'No existes')

	def test_edad_prueba2(self):
		self.edad.calcular_edad(6)
		self.assertEquals(self.edad.obtener_edad(), 'Infancia')
		
	def test_edad_prueba3(self):
		self.edad.calcular_edad(14)
		self.assertEquals(self.edad.obtener_edad(), 'Adolescencia')

	def test_edad_prueba4(self):
		self.edad.calcular_edad(24)
		self.assertEquals(self.edad.obtener_edad(), 'Adultez')

	def test_edad_prueba5(self):
		self.edad.calcular_edad(145)
		self.assertEquals(self.edad.obtener_edad(), 'Estas Muerto')

	def test_edad_prueba6(self):
		self.edad.calcular_edad(85)
		self.assertEquals(self.edad.obtener_edad(), 'Ancianidad')

	def test_edad_prueba7(self):
		self.edad.calcular_edad(45)
		self.assertEquals(self.edad.obtener_edad(), 'Adultez')

	def test_edad_prueba8(self):
		self.edad.calcular_edad(21)
		self.assertEquals(self.edad.obtener_edad(), 'Adultez')

	def test_edad_prueba9(self):
		self.edad.calcular_edad(10)
		self.assertEquals(self.edad.obtener_edad(), 'Infancia')

	def test_edad_prueba10(self):
		self.edad.calcular_edad(15)
		self.assertEquals(self.edad.obtener_edad(), 'Adolescencia')

	def test_edad_prueba11(self):
		self.edad.calcular_edad(199)
		self.assertEquals(self.edad.obtener_edad(), 'Estas Muerto')

if __name__ == '__main__': # pragma: no cover
	unittest.main()
