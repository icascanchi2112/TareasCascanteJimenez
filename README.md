Tareas Cascante Jimenez
Repositorio de la Tarea 1 del curso MT-7003 Microprocesadores y Microcontroladores (ITCR, II Semestre 2026), sobre uso de Git, GitHub, Pytest y Flake8.

Integrantes
•	Ignacio Cascante Chinchilla
•	Dilana Jimenez Solano

Contenido
Todo el trabajo está dentro de la carpeta "Tarea 1":
•	Preguntas teóricas-Tarea_Git_y_GitHub.pdf — respuestas a las 10 preguntas teóricas.
•	tarea_1_example_solution.py — implementación de las funciones filtrar_vocales y encontrar_extremos 
•	tarea_1_testing.py — archivo de pruebas provisto por el profesor.

Cómo correr las pruebas
Desde la carpeta "Tarea 1", con Python instalado:
python -m pytest tarea_1_testing.py
Deben pasar las 4 pruebas.

Cómo correr flake8
python -m flake8 tarea_1_example_solution.py
No debe mostrar ninguna advertencia.

Ramas
•	main — versión estable del código con las funciones y las pruebas pasando.
•	errores-flake8 — rama con un archivo adicional usado para practicar la corrección de errores de formato detectados por flake8, e incluye el Pull Request hacia main.
