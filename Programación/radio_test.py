import pytest
from radio_class import Radio

def test_inicializacion():
    radio = Radio(modelo = 'X123', frecuencia_minima = 87.5, frecuencia_maxima = 108.0, marca = 'Sony')
    assert radio.modelo == 'X123'
    assert radio.frecuencia_minima  == 87.5
    assert radio.frecuencia_maxima == 108.0
    assert radio.marca == 'Sony'
    assert radio.frecuencia_actual == 87.5

def test_sintonizar_valido():
    radio = Radio(modelo='X123', frecuencia_minima =87.5, frecuencia_maxima=108.0, marca='Sony')
    resultado = radio.sintonizar(100.0)
    assert resultado == 'Sintonizado a 100.0 MHz.'
    assert radio.frecuencia_actual == 100.0

def test_sintonizar_fuera_de_rango():
    radio = Radio(modelo='X123', frecuencia_minima =87.5, frecuencia_maxima=108.0, marca='Sony')
    with pytest.raises(ValueError, match="Frecuencia 110.0 MHz fuera de rango."):
        radio.sintonizar(110.0)

def test_buscar_siguiente_frecuencia():
    radio = Radio(modelo='X123', frecuencia_minima =87.5, frecuencia_maxima=108.0, marca='Sony')
    radio.sintonizar(100.0)
    siguiente_frecuencia = radio.buscar_siguiente_frecuencia()
    assert siguiente_frecuencia == 100.5
    siguiente_frecuencia = radio.buscar_siguiente_frecuencia()
    assert siguiente_frecuencia == 101.0

def test_buscar_siguiente_frecuencia_fuera_de_rango():
    radio = Radio(modelo='X123', frecuencia_minima =87.5, frecuencia_maxima=108.0, marca='Sony')
    radio.sintonizar(108.0)
    with pytest.raises(ValueError, match="No hay mas frecuencias disponibles."):
        radio.buscar_siguiente_frecuencia()

def test_escanear_frecuencias():
    radio = Radio(modelo='X123', frecuencia_minima =87.5, frecuencia_maxima=88.0, marca='Sony')
    frecuencias = radio.escanear_frecuencias()
    assert frecuencias == [87.5, 88.0]
