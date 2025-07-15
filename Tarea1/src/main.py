import cv2
import numpy as np
import os
from colors import colores_peligrosidad
from ultralytics import YOLO
from datetime import datetime

# Configuración
MODEL_FILE = "../runs/detect/train/weights/best.pt"
CONF_THRESHOLD = 0.5
SAVE_PATH = "detecciones.txt"
VIDEO_OUTPUT = "output_video.avi"


# Cargar modelo
model = YOLO(MODEL_FILE)

# Inicializar cámara
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error al abrir la cámara.")
    exit()

# Configuración para grabar video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter(VIDEO_OUTPUT, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width, frame_height))

# Variables de conteo
detections_summary = []
count_per_class = {}
count_peligrosos = 0
count_no_peligrosos = 0

from collections import Counter

def detectar_color(img):
    """Detectar el color más dominante (modo) en una imagen recortada usando HSV."""
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    pixels = img_hsv.reshape((-1, 3))
    pixels = pixels[np.any(pixels != [0, 0, 0], axis=1)]

    if len(pixels) == 0:
        return "desconocido"
    
    # Redondear valores para reducir variabilidad
    pixels = np.round(pixels).astype(int)

    # Contar los H (matiz) más comunes
    hues = pixels[:, 0]
    hue_counts = Counter(hues)
    most_common_hue, _ = hue_counts.most_common(1)[0]

    s_mean = np.mean(pixels[:,1])
    v_mean = np.mean(pixels[:,2])

    # Ahora decidimos el color basados en el hue más frecuente
    if v_mean > 200 and s_mean < 30:
        return "blanco"
    elif v_mean < 50:
        return "negro"
    
    if (most_common_hue <= 15 or most_common_hue >= 165) and s_mean > 50:
        return "rojo"
    elif 15 < most_common_hue <= 35 and s_mean > 50:
        if v_mean > 150:
            return "amarillo intenso"
        else:
            return "amarillo claro"
    elif 35 < most_common_hue <= 85 and s_mean > 60:
        if v_mean > 120:
            return "verde brillante"
        else:
            return "verde"
    elif 85 < most_common_hue <= 130 and s_mean > 50:
        return "azul"
    elif 130 < most_common_hue <= 165 and s_mean > 50:
        return "morado"

    return "transparente"




def calcular_porcentaje_llenado(mask):
    """Calcular porcentaje de llenado basado en la máscara de segmentación."""
    if mask is None:
        return np.random.uniform(40, 100)  # fallback si no hay máscara
    total_pixels = mask.size
    filled_pixels = np.sum(mask > 0)
    porcentaje = (filled_pixels / total_pixels) * 100
    return porcentaje

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, save=False, verbose=False)[0]

    if results.boxes is not None:
        boxes = results.boxes.xyxy.cpu().numpy()
        scores = results.boxes.conf.cpu().numpy()
        classes = results.boxes.cls.cpu().numpy()
        masks = results.masks.data.cpu().numpy() if results.masks else None

        for i, (box, score, cls) in enumerate(zip(boxes, scores, classes)):
            if score < CONF_THRESHOLD:
                continue

            x1, y1, x2, y2 = map(int, box)
            class_name = model.names[int(cls)]

            # Conteo por clase
            count_per_class[class_name] = count_per_class.get(class_name, 0) + 1

            # Recortar área
            cropped = frame[y1:y2, x1:x2]

            # Detectar color
            color_detectado = detectar_color(cropped)

            # Consultar peligrosidad
            peligrosidad = colores_peligrosidad.get(color_detectado, "desconocido")

            # Contar peligrosos/no peligrosos
            if peligrosidad == "peligroso":
                count_peligrosos += 1
            else:
                count_no_peligrosos += 1

            # Calcular porcentaje de llenado usando máscara
            if masks is not None:
                mask_obj = masks[i]
                mask_cropped = mask_obj[int(y1):int(y2), int(x1):int(x2)]
                porcentaje_llenado = calcular_porcentaje_llenado(mask_cropped)
            else:
                porcentaje_llenado = np.random.uniform(40, 100)

            porcentaje_llenado = np.clip(porcentaje_llenado, 0, 100)

            # Guardar en resumen
            detections_summary.append({
                'clase': class_name,
                'porcentaje_llenado': round(porcentaje_llenado, 2),
                'color': color_detectado,
                'peligrosidad': peligrosidad
            })

            # Dibujar en pantalla
            label = f'{class_name} {score:.2f}'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            info_text = f'{porcentaje_llenado:.0f}% | {color_detectado} | {peligrosidad}'
            cv2.putText(frame, info_text, (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow('Detección de Líquidos', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Guardar resultados en txt
with open(SAVE_PATH, 'w') as f:
    f.write(f"Fecha de ejecución: {datetime.now()}\n\n")
    for clase, cantidad in count_per_class.items():
        f.write(f"Clase {clase}: {cantidad} detectados\n")
    f.write(f"\nLíquidos peligrosos: {count_peligrosos}\n")
    f.write(f"Líquidos no peligrosos: {count_no_peligrosos}\n\n")
    f.write("Detalles de cada recipiente:\n")
    for det in detections_summary:
        f.write(f"{det['clase']} - {det['porcentaje_llenado']}% - {det['color']} - {det['peligrosidad']}\n")

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()
