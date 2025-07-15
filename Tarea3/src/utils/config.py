# utils/config.py

# Rutas principales
VIDEO_PATH = "videos/unasio.mp4"
MODELO_POSE = "yolo11s-pose.pt"

# Carpetas de salida
CARPETA_GOLDEN = "images/cancion1/avatar"
CARPETA_SCORES = "scores/cancion1"

# Tiempos donde ocurre pose dorada (en segundos)

GOLDEN_TIMES = [104] #1
#GOLDEN_TIMES = [54, 107, 135] #3
#GOLDEN_TIMES = [80, 190] #4

# Frecuencia de evaluación (ej: 1 por segundo)
FRAMES_POR_SEGUNDO_EFECTIVO = 1

# Parámetro del tracker
MAX_DISTANCIA_TRACKING = 50
