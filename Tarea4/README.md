Tarea 4 - Visión por Computador: Robot Visión
=============================================
José Tomás Tapia Espinaza
Curso: IPD-441 Visión por Computador  

------------------------------------------------------------
OBJETIVO
------------------------------------------------------------

Desarrollar un sistema de visión robótica capaz de detectar objetos en imágenes capturadas por un robot móvil (Unitree B2) y estimar su distancia utilizando modelos de profundidad. El sistema combina detección con YOLOv11 y estimación de profundidad con dos modelos distintos para interpretar la escena en 3D.

------------------------------------------------------------
MODELOS UTILIZADOS
------------------------------------------------------------

1. YOLOv11 (detección de objetos)
- Usado para detectar personas, perros, bancas y otros objetos.
- Modelo cargado con Ultralytics a partir del archivo 'yolo11s.pt'.
- Confianza mínima fijada en 60%.

2. MiDaS v3.1 (estimación de profundidad)
- Cargado desde Torch Hub.
- Devuelve mapas de profundidad relativa con alta calidad.

3. Depth Anything V2 (estimación de profundidad)
- Cargado desde Hugging Face.
- Basado en Vision Transformers, con buena precisión y generalización.

------------------------------------------------------------
ESTRUCTURA DEL PROYECTO
------------------------------------------------------------

/src/                          → Código Jupyter Notebook  
/frames/                       → Imágenes originales (input)  
/outputs/
    /modelo_midas/            → Mapas de profundidad con MiDaS  
    /modelo_depth_anything/   → Mapas de profundidad con Depth Anything  
    /modelo_midas_yolo/       → Detección de objetos con YOLO sobre MiDaS  
    /modelo_depth_anything_yolo/ → Detección de objetos con YOLO sobre Depth Anything  
/summarize/
    comparativa_summary_total.png → Imagen resumen tipo collage (5x5)

README.txt                    → Este archivo

------------------------------------------------------------
ESTIMACIÓN DE DISTANCIAS
------------------------------------------------------------

Los modelos de profundidad utilizados entregan mapas de escala relativa (no en metros).  
Para obtener una escala aproximada en metros:

- Se asumió que una persona estaba a 1.5 metros del robot.
- Se usó su detección como referencia para obtener un valor de profundidad relativo.
- Se calculó un factor de escala: escala = 1.5 / profundidad_relativa
- Ese factor se aplicó a todo el mapa de profundidad para estimar otras distancias.

------------------------------------------------------------
RESULTADOS GENERADOS
------------------------------------------------------------

- 5 mapas de profundidad con MiDaS
- 5 mapas de profundidad con Depth Anything V2
- 5 imágenes con detección YOLO sobre MiDaS
- 5 imágenes con detección YOLO sobre Depth Anything
- 5 gráficos individuales comparativos
- 1 imagen resumen comparativa (5x5)

------------------------------------------------------------
INSTRUCCIONES DE USO
------------------------------------------------------------

1. Instalar dependencias:
   pip install torch torchvision transformers ultralytics timm accelerate

2. Ejecutar el notebook principal:
   RobotVision_Tarea4.ipynb

------------------------------------------------------------
COMENTARIO FINAL
------------------------------------------------------------

Este sistema entrega una simulación funcional de visión robótica utilizando únicamente una cámara RGB.  
Para obtener medidas reales más precisas, se recomienda el uso de cámaras estéreo calibradas o sensores de profundidad físicos.

