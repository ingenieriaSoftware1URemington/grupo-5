# Grupo 5
- Juan Diego Sánchez  
- Alejandra Roas  

---

## Nombre de la aplicación
Mars Climate Orbiter – Sistema de Control de Navegación

---

## Lenguaje de desarrollo
C / C++

Estos lenguajes se utilizaron para desarrollar una aplicación crítica, capaz de ejecutar cálculos complejos de navegación y control en tiempo real dentro de un sistema aeroespacial.

---

## Tipo de aplicación
Aplicación de software crítico (Mission-Critical Application)

Aplicación integrada al sistema de control de una sonda espacial no tripulada destinada al estudio del clima de Marte.

---

## Funcionalidad de la aplicación
La aplicación se encargaba de:

- Calcular fuerzas de propulsión
- Controlar la trayectoria de la nave
- Ajustar la altitud durante la aproximación a Marte
- Intercambiar información entre distintos módulos de navegación

---

## Descripción del fallo de la aplicación
El fallo ocurrió por una mala integración entre módulos del sistema:

- Un módulo generaba datos en libras-fuerza (sistema imperial)
- Otro módulo esperaba esos datos en newtons (sistema métrico)

La aplicación no realizó la conversión de unidades ni validó los datos recibidos, provocando errores en los cálculos de navegación.

---

## Manifestación del error
Durante la ejecución de la aplicación en la fase de aproximación a Marte en 1999:

- La aplicación calculó una altitud incorrecta
- La nave descendió más de lo previsto
- El sistema no detectó el error
- No se activaron mecanismos de corrección
- Se perdió la comunicación con la sonda

---

## Consecuencias
- Fallo total de la aplicación de navegación
- Destrucción de la sonda espacial
- Pérdida económica aproximada de 125 millones de dólares
- Evidencia de fallas en:
  - Validación de datos
  - Pruebas de integración
  - Manejo de errores entre módulos
  
![casos de uso](img/diagrama.png)
[casos de uso](img/diagramanuevo.png)
![casos de uso](img/diagrama-clases.png)
