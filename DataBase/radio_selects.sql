-- Radios y sus marcas:
SELECT r.modelo, m.nombre AS marca
FROM radios.radios r
LEFT JOIN radios.marcas m ON r.id_marca = m.id_marca;

-- Radios y sus tipos:
SELECT r.modelo, t.nombre AS tipo
FROM radios.radios r
LEFT JOIN radios.radios_tipos rt ON r.id_radio = rt.id_radio
LEFT JOIN radios.tipos t ON rt.id_tipo = t.id_tipo;

-- Marcas y radios registrados por cada una:
SELECT m.nombre AS marca, COUNT(r.id_radio) AS total_radios
FROM radios.marcas m
LEFT JOIN radios.radios r ON m.id_marca = r.id_marca
GROUP BY m.id_marca;

-- Tipos de radio y cuantos tienen disponible:
SELECT t.nombre AS tipo, COUNT(rt.id_radio) AS total_radios
FROM radios.tipos t
LEFT JOIN radios.radios_tipos rt ON t.id_tipo = rt.id_tipo
GROUP BY t.id_tipo;

-- Radios con toda su informacion general
SELECT r.id_radio, r.modelo, m.nombre AS marca, GROUP_CONCAT(t.nombre SEPARATOR ' - ') AS tipos,
r.frecuencia_minimo, r.frecuencia_maxima
FROM radios.radios r
LEFT JOIN radios.marcas m ON r.id_marca = m.id_marca
INNER JOIN radios.radios_tipos rt ON r.id_radio = rt.id_radio
LEFT JOIN radios.tipos t ON rt.id_tipo = t.id_tipo
GROUP BY r.id_radio;