Feature: Calcular etapa de la vida de una persona
    Como usuario del sistema
    deseo saber en que etapa de la vida esta una persona
    para saber que personas utilizan mi aplicación

  Scenario: Calcular edad de 0 anos
    Dado que ingreso la edad de "0" anos
    cuando realizo la operacion
    su etapa es "No existes"

  Scenario: Calcular edad de 9 anos
    Dado que ingreso la edad de "9" anos
    cuando realizo la operacion
    su etapa es "Infancia"

  Scenario: Calcular edad de 15 anos
    Dado que ingreso la edad de "15" anos
    cuando realizo la operacion
    su etapa es "Adolescencia"

  Scenario: Calcular edad de 57 anos
    Dado que ingreso la edad de "57" anos
    cuando realizo la operacion
    su etapa es "Adultez"

  Scenario: Calcular edad de 92 anos
    Dado que ingreso la edad de "92" anos
    cuando realizo la operacion
    su etapa es "Ancianidad"

  Scenario: Calcular edad de 189 anos
    Dado que ingreso la edad de "189" anos
    cuando realizo la operacion
    su etapa es "Estas Muerto"


