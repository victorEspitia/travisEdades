# -*- coding: utf-8 -*-
from lettuce import step, world
from Edad import Edad

@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass

# Calcular Edades
@step(u'Dado que ingreso la edad de "([^"]*)" anos')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.ed = Edad()
    world.ed.calcular_edad(int(num1))
@step(u'su etapa es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = world.ed.obtener_edad()
    assert esperado == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)