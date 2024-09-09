Create database radios;

create table radios.marcas (
id_marca int auto_increment primary key,
nombre varchar(50) not null
);

create table radios.radios (
id_radio int auto_increment primary key,
modelo varchar(50) not null,
frecuencia_minimo decimal(4,1) not null,
frecuencia_maxima decimal(4,1) not null,
id_marca int,
foreign key(id_marca) references radios.marcas(id_marca) on delete set null on update cascade
);

create table radios.tipos (
id_tipo int auto_increment primary key,
nombre varchar(50) not null
);

create table radios.radios_tipos (
id_radio int,
id_tipo int,
primary key(id_radio, id_tipo),
foreign key(id_radio) references radios.radios(id_radio),
foreign key(id_tipo) references radios.tipos(id_tipo)
);