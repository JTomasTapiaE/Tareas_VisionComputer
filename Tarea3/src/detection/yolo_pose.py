# detection/yolo_pose.py

from ultralytics import YOLO
import cv2
import numpy as np

# Índices que SÍ queremos conservar (tronco y extremidades)
INDICES_VALIDOS = list(range(5, 17))  # Asume que hay 17 keypoints

class YoloPoseDetector:
    def __init__(self, model_path="yolo11s-pose.pt", device="cpu"):
        self.model = YOLO(model_path)
        self.device = device

    def detectar_poses(self, frame_bgr):
        """
        Detecta poses humanas excluyendo puntos del rostro.
        """
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        results = self.model.predict(source=frame_rgb, device=self.device, verbose=False)

        poses = []
        for result in results:
            for kp, box in zip(result.keypoints.xy, result.boxes.xyxy):
                keypoints = kp.cpu().numpy()  # (N, 2)
                # Filtrar keypoints válidos
                keypoints_filtrados = keypoints[INDICES_VALIDOS]
                bbox = box.cpu().numpy()
                poses.append({
                    "bbox": bbox,
                    "keypoints": keypoints_filtrados
                })
        return poses
