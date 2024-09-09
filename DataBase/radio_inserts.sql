-- Inserción de marcas:
INSERT INTO radios.marcas (nombre) VALUES ('Sony');
INSERT INTO radios.marcas (nombre) VALUES ('Panasonic');
INSERT INTO radios.marcas (nombre) VALUES ('JVC');
INSERT INTO radios.marcas (nombre) VALUES ('Philips');
INSERT INTO radios.marcas (nombre) VALUES ('Suono');

-- Inserción de radios:
INSERT INTO radios.radios (modelo, frecuencia_minimo, frecuencia_maxima, id_marca) 
VALUES ('X123', 87.5, 108.0, 1);
INSERT INTO radios.radios (modelo, frecuencia_minimo, frecuencia_maxima, id_marca) 
VALUES ('P456', 88.0, 107.9, 2);
INSERT INTO radios.radios (modelo, frecuencia_minimo, frecuencia_maxima, id_marca) 
VALUES ('J789', 86.0, 108.5, 3);
INSERT INTO radios.radios (modelo, frecuencia_minimo, frecuencia_maxima, id_marca) 
VALUES ('Ph101', 87.9, 108.2, 4);
INSERT INTO radios.radios (modelo, frecuencia_minimo, frecuencia_maxima, id_marca) 
VALUES ('SW1-2', 87.0, 108.5, 5);

-- Inserción de tipos:
INSERT INTO radios.tipos (nombre) VALUES ('Digital');
INSERT INTO radios.tipos (nombre) VALUES ('Analógico');
INSERT INTO radios.tipos (nombre) VALUES ('AM');
INSERT INTO radios.tipos (nombre) VALUES ('DAB');
INSERT INTO radios.tipos (nombre) VALUES ('Satélite');
INSERT INTO radios.tipos (nombre) VALUES ('FM'); 

-- Inserción de relacion muchos a muchos en radios_tipos:
INSERT INTO radios.radios_tipos (id_radio, id_tipo) VALUES (1, 1);
INSERT INTO radios.radios_tipos (id_radio, id_tipo) VALUES (2, 2);
INSERT INTO radios.radios_tipos (id_radio, id_tipo) VALUES (3, 3);
INSERT INTO radios.radios_tipos (id_radio, id_tipo) VALUES (3, 6);
INSERT INTO radios.radios_tipos (id_radio, id_tipo) VALUES (4, 4);
INSERT INTO radios.radios_tipos (id_radio, id_tipo) VALUES (5, 3);
INSERT INTO radios.radios_tipos (id_radio, id_tipo) VALUES (5, 6);