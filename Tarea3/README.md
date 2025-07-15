# Tarea 3 - IPD441 Visión por Computador  
## Estimación de Poses con YOLOv11 Pose

## Objetivo
Desarrollar un sistema que detecte, compare y clasifique en tiempo real los movimientos corporales de jugadores humanos en Just Dance, utilizando el modelo YOLOv11 Pose, con el fin de evaluar su similitud con las poses del avatar del videojuego.

## Canciones utilizadas

| Canción           | Jugadores | Dificultad | Avatar humano |
|-------------------|-----------|------------|----------------|
| Dynamite          | 4         | Extreme    | Sí             |
| Beach Boys        | 1         | Easy       | Sí             |
| Zero to Hero      | 3         | Medium     | Sí             |

Todas las canciones pertenecen a versiones oficiales de Just Dance y cumplen con los requisitos del enunciado.

## Descripción del sistema

- Detecta keypoints usando YOLOv11 Pose (modelo `yolo11s-pose.pt`).
- Evalúa 1 pose por segundo durante la canción.
- Compara la pose del jugador con la del avatar usando:
  - Similitud de coseno
  - Similitud inversa de MSE
  - Se promedia el resultado para obtener una similitud final
- Clasificación de precisión:
    100 % – 75 %    Perfect
    75 % – 50 %     Good
    50 % – 25 %     Ok
    25 % – 0 %      Bad
- Se usa tracking basado en centroides para identificar a cada jugador durante todo el video.
- Detecta y guarda automáticamente las Golden Poses según segundos predefinidos.
- Genera un archivo `.txt` por jugador con su conteo de poses clasificadas y estrellas finales.

## Estructura del entregable

.
├── src/
│   ├── main.py
│   ├── detection/
│   ├── evaluation/
│   ├── tracking/
│   ├── utils/
├── images/
│   └── cancion1/
│       └── avatar/
│           └── golden_XX.jpg
├── scores/
│   └── cancion1/
│       └── jugador_0.txt, jugador_1.txt, ...
├── README.md

## Cómo ejecutar

1. Instalar las dependencias:
   pip install ultralytics opencv-python numpy

2. Colocar el video en formato side-by-side en la ruta especificada en config.py:
   VIDEO_PATH = "video_side_by_side.mp4"

3. Ejecutar desde terminal:
   python src/main.py

## Decisiones técnicas

- Se utilizó el modelo `yolo11s-pose.pt` para facilitar la ejecución en CPU.
- El sistema de tracking utiliza centroides para mantener la identidad del jugador.
- Se normalizan las poses antes de calcular la similitud para reducir el impacto del desplazamiento y escala.
- La similitud se obtiene como el promedio entre la similitud del coseno y el MSE inverso.
- Las poses doradas se detectan en base al segundo del video, se extraen y se guardan con keypoints y texto en ambos lados del video (jugador y avatar).

## Enlaces a los videos (visualización de resultados)
https://usmcl-my.sharepoint.com/:f:/g/personal/jose_tapiae_usm_cl/EiAFuRYHR9ZKrJ6ghQx2jA8BLqE_2clJGPDt25qso6NoqQ?e=mTgg9J
- Dynamite (Extreme, 4 jugadores): 
- Beach Boys (Easy, 1 jugador): 
- Zero to Hero (Medium, 3 jugadores): 

Los videos están en formato side-by-side 

## Estado del proyecto

- Detección de keypoints funcionando
- Evaluación 1 vez por segundo
- Clasificación individual por jugador
- Detección y guardado de poses doradas
- Reportes en texto por jugador generados correctamente
- Código modularizado y limpio

## Autor

José Tomás Tapia  
UTFSM  
IPD-441 Visión por Computador, 2025
