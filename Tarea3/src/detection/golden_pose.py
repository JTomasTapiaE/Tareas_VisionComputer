import cv2
import os
from utils.draw_utils import dibujar_resultados
from evaluation.similarity import combined_similarity
from evaluation.classification import clasificar_precision

def guardar_poses_doradas_por_tiempo(frame_idx, fps, frame_humano, frame_avatar,
                                     poses_humano, poses_avatar, golden_times,
                                     carpeta_salida):
    """
    Guarda una imagen combinada de jugador y avatar cuando hay pose dorada.
    """
    segundo_actual = frame_idx // fps
    if segundo_actual not in golden_times:
        return

    if not poses_avatar or not poses_humano:
        return

    os.makedirs(carpeta_salida, exist_ok=True)

    frame_avatar_out = frame_avatar.copy()
    frame_humano_out = frame_humano.copy()

    pose_avatar = poses_avatar[0]

    # Dibujar avatar con etiqueta "Golden"
    dibujar_resultados(
        frame_avatar_out,
        pose_avatar["bbox"],
        pose_avatar["keypoints"],
        "Golden"
    )

    # Dibujar todos los jugadores
    for i, pose_jugador in enumerate(poses_humano):
        sim = combined_similarity(pose_jugador["keypoints"], pose_avatar["keypoints"])
        clase = clasificar_precision(sim)
        texto = f"Jugador {i} - {clase}"

        dibujar_resultados(
            frame_humano_out,
            pose_jugador["bbox"],
            pose_jugador["keypoints"],
            texto
        )

    # Combinar ambas mitades y guardar
    imagen_final = cv2.hconcat([frame_humano_out, frame_avatar_out])
    nombre_archivo = f"golden_{segundo_actual:02d}.jpg"
    ruta = os.path.join(carpeta_salida, nombre_archivo)
    cv2.imwrite(ruta, imagen_final)
    print(f"📸 Guardada golden pose combinada en segundo {segundo_actual}")

def es_pose_dorada(frame_avatar, umbral=0.015):
    """
    Detecta si hay un resplandor dorado en la esquina inferior derecha del frame.
    """
    h, w = frame_avatar.shape[:2]
    zona = frame_avatar[int(h*0.8):, int(w*0.8):]  # esquina inferior derecha

    hsv = cv2.cvtColor(zona, cv2.COLOR_BGR2HSV)

    # Rango de amarillo/naranja brillante
    lower = np.array([20, 100, 200])   # H, S, V
    upper = np.array([40, 255, 255])

    mascara = cv2.inRange(hsv, lower, upper)
    proporcion = np.count_nonzero(mascara) / mascara.size

    return proporcion > umbral

def guardar_pose_dorada(frame_avatar, pose, clasificacion, carpeta_salida, nombre_archivo):
    """
    Dibuja y guarda el frame del avatar con la pose y clasificación.
    """
    frame_copia = frame_avatar.copy()
    dibujar_resultados(frame_copia, pose["bbox"], pose["keypoints"], clasificacion)

    os.makedirs(carpeta_salida, exist_ok=True)
    ruta = os.path.join(carpeta_salida, nombre_archivo)
    cv2.imwrite(ruta, frame_copia)

