# utils/draw_utils.py

import cv2
import numpy as np

COLOR_CLASIFICACION = {
    "Perfect": (0, 255, 0),     # Verde
    "Good": (255, 255, 0),      # Amarillo
    "Ok": (0, 165, 255),        # Naranjo
    "Bad": (0, 0, 255),         # Rojo
}

def dibujar_resultados(frame, bbox, keypoints, clasificacion):
    """
    Dibuja bounding box, keypoints y clasificación sobre el frame (modifica el frame en sí).
    """
    color = COLOR_CLASIFICACION.get(clasificacion, (255, 255, 255))

    x1, y1, x2, y2 = map(int, bbox)
    h, w = frame.shape[:2]

    # Limita coordenadas dentro de frame
    x1 = max(0, min(x1, w-1))
    x2 = max(0, min(x2, w-1))
    y1 = max(0, min(y1, h-1))
    y2 = max(0, min(y2, h-1))

    # Bounding box
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    # Texto clasificación
    cv2.putText(
        frame,
        clasificacion,
        (x1, max(0, y1 - 10)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2,
        cv2.LINE_AA
    )

    # Keypoints
    for x, y in keypoints:
        if 0 <= int(x) < w and 0 <= int(y) < h:
            cv2.circle(frame, (int(x), int(y)), 4, color, -1)
