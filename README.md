# Sistema Agencia de Viajes

Proyecto de Ingeniería de Software I.

Este proyecto simula el funcionamiento básico de una **agencia de viajes**, donde se pueden registrar turistas y realizar reservas de **hoteles o vuelos**.

El sistema funciona por consola y está desarrollado usando **Programación Orientada a Objetos (POO)** en Python.

---

## Funcionalidades

El sistema permite:

- Registrar turistas
- Listar turistas registrados
- Registrar hoteles
- Registrar vuelos
- Crear reservas de hotel
- Crear reservas de vuelo
- Consultar reservas realizadas

---

## Estructura del proyecto

El proyecto está organizado en carpetas para separar las responsabilidades del sistema.

- **models:** Contiene las clases del dominio (entidades del sistema).
- **services:** Contiene la lógica de negocio del sistema.
- **main.py:** Archivo principal desde donde se ejecuta el programa.

Ejemplo de estructura:

---

## Descripción de las clases

### Turista
Representa a un cliente de la agencia.

Atributos principales:
- id
- nombre
- documento
- email
- presupuesto

---

### Hotel
Representa un hotel disponible para reservas.

Atributos principales:
- id
- nombre
- ciudad
- estrellas
- habitaciones disponibles

---

### Vuelo
Representa un vuelo que puede ser reservado.

Atributos principales:
- id
- origen
- destino
- fecha
- precio

---

### Sucursal
Representa una sucursal de la agencia de viajes.

Atributos principales:
- id
- nombre
- ciudad
- dirección

---

## Lógica del sistema

La clase **SistemaAgencia** se encarga de:

- Registrar turistas
- Registrar hoteles
- Registrar vuelos
- Registrar sucursales
- Crear reservas
- Consultar información del sistema

---

## Cómo ejecutar el proyecto

1. Abrir la terminal en la carpeta del proyecto.
2. Ejecutar el archivo principal:

```bash
python main.py