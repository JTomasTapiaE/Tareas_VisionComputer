# utils/video_utils.py

import cv2

def cargar_video_side_by_side(video_path, fps_objetivo=1):
    """
    Carga el video y devuelve frames cada 1 segundo.
    Cada frame es un dict: {"humano": frame_izq, "avatar": frame_der}
    """
    cap = cv2.VideoCapture(video_path)

    fps_original = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps_original // fps_objetivo)

    frames_divididos = []
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frame_interval == 0:
            alto, ancho, _ = frame.shape
            mitad = ancho // 2
            frame_humano = frame[:, :mitad]
            frame_avatar = frame[:, mitad:]

            frames_divididos.append({
                "humano": frame_humano,
                "avatar": frame_avatar
            })

        frame_idx += 1

    cap.release()
    return frames_divididos



