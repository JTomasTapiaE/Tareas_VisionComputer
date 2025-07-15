import numpy as np

def normalizar_pose(pose):
    """
    Centra y escala la pose (keypoints) respecto al centroide y magnitud.
    """
    centroide = np.mean(pose, axis=0)
    pose_centrada = pose - centroide
    norma = np.linalg.norm(pose_centrada)
    if norma == 0:
        return pose_centrada
    return pose_centrada / norma

def cosine_similarity(pose1, pose2):
    """
    Similitud de coseno entre poses normalizadas.
    """
    v1 = normalizar_pose(pose1).flatten()
    v2 = normalizar_pose(pose2).flatten()

    dot = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return float(np.clip(dot / (norm1 * norm2), 0.0, 1.0))

def mse_similarity(pose1, pose2):
    """
    Similitud basada en el inverso del error cuadrático medio.
    """
    p1 = normalizar_pose(pose1)
    p2 = normalizar_pose(pose2)

    if p1.shape != p2.shape:
        return 0.0

    mse = np.mean((p1 - p2) ** 2)
    return float(np.clip(1.0 / (1.0 + mse), 0.0, 1.0))

def combined_similarity(pose1, pose2):
    """
    Promedio de similitud de coseno y MSE inverso.
    """
    sim_cos = cosine_similarity(pose1, pose2)
    sim_mse = mse_similarity(pose1, pose2)
    return (sim_cos + sim_mse) / 2.0
