Repositorio de Proyectos - Visión por Computador
================================================

Este repositorio reúne todos los proyectos desarrollados durante el curso de Visión por Computador. Cada tarea aplica técnicas modernas de procesamiento de imágenes, aprendizaje profundo y modelos de inteligencia artificial, con aplicaciones en escenarios reales y simulados.

------------------------------------------------
Tarea 1: Sistema de Detección de Volumen y Tipo de Líquido en Recipientes
------------------------------------------------

Objetivo:
Desarrollar un sistema en tiempo real capaz de detectar botellas, vasos y copas de vidrio, analizar el porcentaje de llenado de los líquidos, identificar su color y evaluar su peligrosidad (ej. bebidas tóxicas o inflamables).

Tecnologías utilizadas:
- Modelo de detección: YOLOv11 (segmentación y bounding boxes)
- Dataset personalizado: entrenado en Roboflow
- Análisis de color y volumen: técnicas de visión computacional y heurísticas de procesamiento de imagen

------------------------------------------------
Tarea 2: Generación de Imágenes a partir de Frases de Libros
------------------------------------------------

Objetivo:
Diseñar un pipeline creativo que transforme frases literarias en imágenes mediante modelos generativos de IA.

Etapas del proyecto:
1. Extracción de frases significativas de textos literarios
2. Generación de prompts usando LLaMA 3
3. Creación de imágenes con:
   - Stable Diffusion XL
   - FLUX.1-dev
4. Superposición del texto en las imágenes con indicación del modelo usado
5. Comparación visual mediante creación de GIFs animados

------------------------------------------------
Tarea 3: Estimación y Comparación de Poses con YOLOv11 Pose
------------------------------------------------

Objetivo:
Construir un sistema que detecte, compare y clasifique en tiempo real las poses corporales de jugadores humanos en el videojuego Just Dance, comparándolas con las del avatar digital para evaluar la similitud de movimientos.

Características:
- Detección y seguimiento con YOLOv11 Pose
- Comparación de poses usando coordenadas de keypoints
- Seguimiento multijugador (detección y asociación por ID)
- Evaluación de similitud de movimientos por jugador

------------------------------------------------
Tarea 4: Estimación de Profundidad y Detección de Objetos
------------------------------------------------

Objetivo:
Implementar un sistema de visión robótica que integre detección de objetos y estimación de profundidad para un robot móvil (Unitree B2), permitiendo interpretar escenas en 3D.

Componentes del sistema:
- Detección de objetos con YOLOv11
- Estimación de profundidad con dos modelos distintos (monoculares)
- Cálculo de distancias relativas entre el robot y los objetos detectados
- Posible integración con navegación o toma de decisiones autónoma


------------------------------------------------
Entorno General Recomendado
------------------------------------------------

Este repositorio utiliza principalmente:

- Python 3.10+
- PyTorch
- OpenCV
- NumPy
- Matplotlib
- ultralytics
- roboflow
- diffusers
- transformers

Se recomienda revisar el `README.md` de cada carpeta para más detalles sobre instalación, dependencias específicas y ejecución de cada proyecto.

------------------------------------------------
Créditos
------------------------------------------------

Proyectos desarrollados durante el curso "Visión por Computador", 2025.

Autor: José Tomás Tapia Espinaza

------------------------------------------------
Comentarios Finales
------------------------------------------------

Cada tarea representa una aplicación distinta de visión por computador, desde análisis de imágenes estáticas hasta visión en tiempo real y sistemas multicomponente. Este repositorio demuestra la versatilidad de los modelos actuales (YOLO, Diffusion, Pose Estimation) y su potencial para resolver problemas complejos en diferentes dominios.
