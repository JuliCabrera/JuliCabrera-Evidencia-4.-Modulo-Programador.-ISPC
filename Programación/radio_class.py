class Radio:
    def __init__(self, modelo, frecuencia_minima, frecuencia_maxima, marca):
        self._modelo = modelo
        self._frecuencia_minima = frecuencia_minima
        self._frecuencia_maxima = frecuencia_maxima
        self._marca = marca
        self._frecuencia_actual = frecuencia_minima  # La radio empieza en la frecuencia mínima.
    
    # Getters y Setters
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def frecuencia_minima(self):
        return self._frecuencia_minima

    @frecuencia_minima.setter
    def frecuencia_minima(self, value):
        self._frecuencia_minima = value

    @property
    def frecuencia_maxima(self):
        return self._frecuencia_maxima

    @frecuencia_maxima.setter
    def frecuencia_maxima(self, value):
        self._frecuencia_maxima = value

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def frecuencia_actual(self):
        return self._frecuencia_actual

    @frecuencia_actual.setter
    def frecuencia_actual(self, value):
        if self._frecuencia_minima <= value <= self._frecuencia_maxima:
            self._frecuencia_actual = value
        else:
            raise ValueError("Frecuencia fuera del rango permitido.")

    # Métodos especiales
    def __str__(self):
        return f"Radio {self._modelo} de {self._marca}, frecuencia actual: {self._frecuencia_actual} MHz"
    
    # Comportamientos clave

    # 1. Sintonizar
    def sintonizar(self, frecuencia):
        # Cambia la frecuencia actual a la especificada si esta dentro del rango permitido.
        if self._frecuencia_minima <= frecuencia <= self._frecuencia_maxima:
            self._frecuencia_actual = frecuencia
            return f"Sintonizado a {frecuencia} MHz."
        else:
            raise ValueError(f"Frecuencia {frecuencia} MHz fuera de rango.")
    
    # 2. Buscar siguiente frecuencia
    def buscar_siguiente_frecuencia(self):
        # Incrementa la frecuencia en 0.5 MHz hasta un maximo.
        if self._frecuencia_actual + 0.5 <= self._frecuencia_maxima:
            self._frecuencia_actual += 0.5
            return self._frecuencia_actual
        else:
            raise ValueError("No hay mas frecuencias disponibles.")
    
    # 3. Escanear frecuencias
    def escanear_frecuencias(self):
         # Escanea todas las frecuencias desde la mínima hasta la maxima en incrementos de 0.5 MHz.
        frecuencias_disponibles = []
        freq = self._frecuencia_minima
        while freq <= self._frecuencia_maxima:
            frecuencias_disponibles.append(freq)
            freq += 0.5
        return frecuencias_disponibles
