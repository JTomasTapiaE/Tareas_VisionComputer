import cv2
import os   
import numpy as np

from detection.yolo_pose import YoloPoseDetector
from detection.golden_pose import guardar_poses_doradas_por_tiempo
from tracking.player_tracker import PlayerTracker
from evaluation.similarity import mse_similarity
from evaluation.classification import clasificar_precision
from evaluation.score_report import ScoreManager
from utils.draw_utils import dibujar_resultados
from utils.config import (
    VIDEO_PATH,
    MODELO_POSE,
    GOLDEN_TIMES,
    CARPETA_GOLDEN,
    CARPETA_SCORES,
    MAX_DISTANCIA_TRACKING,
    FRAMES_POR_SEGUNDO_EFECTIVO
)

# --- Inicialización ---
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("❌ No se pudo abrir el video.")
    exit()

fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_interval = max(1, fps // FRAMES_POR_SEGUNDO_EFECTIVO)

pose_detector = YoloPoseDetector(model_path=MODELO_POSE, device="cpu")
tracker = PlayerTracker(max_distancia=MAX_DISTANCIA_TRACKING)
score_manager = ScoreManager()

frame_idx = 0


def emparejar_pose_por_bbox(bbox_target, poses, umbral=20):
    """
    Busca la pose cuyo centroide esté más cerca del bbox dado.
    """
    cx_t = (bbox_target[0] + bbox_target[2]) / 2
    cy_t = (bbox_target[1] + bbox_target[3]) / 2

    min_dist = float("inf")
    mejor_pose = None

    for ph in poses:
        cx = (ph["bbox"][0] + ph["bbox"][2]) / 2
        cy = (ph["bbox"][1] + ph["bbox"][3]) / 2
        dist = np.hypot(cx - cx_t, cy - cy_t)
        if dist < min_dist and dist < umbral:
            min_dist = dist
            mejor_pose = ph

    return mejor_pose

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Procesar solo cada 1 segundo
    if frame_idx % frame_interval != 0:
        frame_idx += 1
        continue

    alto, ancho = frame.shape[:2]
    mitad = ancho // 2
    frame_humano = frame[:, :mitad].copy()
    frame_avatar = frame[:, mitad:].copy()

    poses_humano = pose_detector.detectar_poses(frame_humano)
    poses_avatar = pose_detector.detectar_poses(frame_avatar)

    # --- Guardar pose dorada si corresponde ---
    guardar_poses_doradas_por_tiempo(
        frame_idx,
        fps,
        frame_humano,
        frame_avatar,
        poses_humano,
        poses_avatar,
        GOLDEN_TIMES,
        CARPETA_GOLDEN
    )

    # --- Tracking jugadores humanos ---
    bboxes_humano = [ph["bbox"] for ph in poses_humano]
    jugadores = tracker.actualizar(bboxes_humano)

    # --- Comparación con avatar y clasificación ---
    if poses_avatar:
        pose_avatar = poses_avatar[0]  # para comparar con jugadores

        # Dibujar visualización del avatar (opcional, para verlo)
        for avatar_pose in poses_avatar:
            dibujar_resultados(
                frame_avatar,
                avatar_pose["bbox"],
                avatar_pose["keypoints"],
                "Avatar"
            )

        for jugador_id, bbox in jugadores.items():
            pose_jugador = emparejar_pose_por_bbox(bbox, poses_humano)

            if pose_jugador is None:
                continue
      

            sim = mse_similarity(pose_jugador["keypoints"], pose_avatar["keypoints"])
            clasificacion = clasificar_precision(sim)
            score_manager.registrar(jugador_id, clasificacion)

            texto = f"Jugador {jugador_id} - {clasificacion}"
            dibujar_resultados(frame_humano, pose_jugador["bbox"], pose_jugador["keypoints"], texto)


    # --- Mostrar resultado ---
    frame_completo = cv2.hconcat([frame_humano, frame_avatar])
    cv2.imshow("DanceMatch AI", frame_completo)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

    frame_idx += 1

# --- Finalizar ---
cap.release()
cv2.destroyAllWindows()

# --- Generar reportes finales ---
score_manager.generar_reportes(CARPETA_SCORES)
print("✅ Proceso finalizado. Reportes generados.")
