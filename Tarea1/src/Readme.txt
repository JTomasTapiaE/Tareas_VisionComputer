Detección y Análisis de Líquidos en Botellas

Asignatura: Visión por Computador (IPD-441)
Profesor: Nicolás Torres
Ayudante: Isidora Ubilla
Fecha: Abril 2025
Autor: José Tomás Tapia

Links Dataset y Video

Dataset: https://universe.roboflow.com/shinta-v3hi3/liquido-en-recipientes 

Video: https://drive.google.com/drive/folders/1y3j3i2-lpOOhroN8A2Q2FgqSl8BQEFZY?usp=drive_link

Descripción del Proyecto:

Este proyecto consiste en un sistema en tiempo real que detecta botellas, vasos y copas de vidrio, analiza el porcentaje de llenado de líquidos, detecta el color del líquido y evalúa su peligrosidad.
Utiliza técnicas de visión por computador y aprendizaje profundo, empleando un modelo YOLOv11 entrenado sobre un dataset personalizado en Roboflow.

Estructura del Código:

Carpeta /src:

main.py (Script principal que realiza la detección y análisis)

colors.py (Diccionario de colores y niveles de peligrosidad)

detecciones.txt (Archivo de salida con el resumen de las detecciones)

Carpeta /train-results:

confusion_matrix.png

f1_curve.png

pr_curve.png

results.png (Resultados del entrenamiento)

Otros archivos de resultados de validación

Proceso de Validación:

Entrenamiento: Modelo entrenado en Roboflow utilizando un conjunto de más de 300 imágenes divididas entre botellas, vasos y copas.

Epochs: Se entrenó durante un mínimo de 20 epochs, como requería la tarea.

Validación:

Se analizaron las matrices de confusión para evaluar el desempeño por clase.

Se generaron las curvas de Precision-Recall (PR) y F1-Score.

Resultados:

Se alcanzó una accuracy promedio superior al 60%.

Se observó un buen balance entre precisión y sensibilidad.

Interpretación de Resultados:

Matriz de Confusión: Se observó un buen reconocimiento de las clases de recipiente.

Curvas PR y F1: Las curvas mostraron una buena separación de clases, confirmando que el modelo es capaz de detectar líquidos de forma precisa incluso con iluminación y fondos variables.

Análisis de errores: Se detectaron algunas confusiones menores en copas muy transparentes.


Información de Detecciones:

Durante la ejecución del programa, se genera automáticamente un archivo "detecciones.txt" que incluye:

Cantidad de recipientes detectados por clase.

Número de líquidos peligrosos y no peligrosos detectados.

Porcentaje de llenado de cada recipiente.

Color del líquido detectado.

Clasificación de peligrosidad según el color.

Comentarios Finales:

Se implementó una detección de color utilizando el color dominante (modo) en espacio HSV para evitar confusión por reflejos en los recipientes de vidrio.
Además, el cálculo del porcentaje de llenado se basa en segmentaciones reales de las máscaras de los objetos detectados, mejorando la precisión.

El sistema puede detectar múltiples recipientes en tiempo real, grabar video de la ejecución y generar automáticamente los reportes solicitados.