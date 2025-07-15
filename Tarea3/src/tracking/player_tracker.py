# tracking/player_tracker.py

import numpy as np
from scipy.spatial import distance

class PlayerTracker:
    def __init__(self, max_distancia=50):
        self.proximo_id = 0
        self.objetos = {}  # id -> centroide actual
        self.max_distancia = max_distancia

    def actualizar(self, bboxes):
        """
        Recibe una lista de bounding boxes (x1, y1, x2, y2).
        Asocia cada una a un ID persistente.
        Retorna un dict: {id: bbox}
        """
        centroides_actuales = np.array([
            [(x1 + x2) // 2, (y1 + y2) // 2]
            for (x1, y1, x2, y2) in bboxes
        ])

        nuevos_ids = {}

        if len(self.objetos) == 0:
            for c in centroides_actuales:
                self.objetos[self.proximo_id] = c
                nuevos_ids[self.proximo_id] = c
                self.proximo_id += 1
            return {id_: bbox for id_, bbox in zip(nuevos_ids.keys(), bboxes)}

        # Comparar centroides antiguos vs nuevos
        objetos_ids = list(self.objetos.keys())
        objetos_centros = list(self.objetos.values())

        D = distance.cdist(np.array(objetos_centros), centroides_actuales)

        filas = D.min(axis=1).argsort()
        columnas = D.argmin(axis=1)

        usados = set()
        resultado = {}

        for fila in filas:
            columna = columnas[fila]
            if columna in usados:
                continue

            distancia = D[fila, columna]
            if distancia < self.max_distancia:
                id_ = objetos_ids[fila]
                self.objetos[id_] = centroides_actuales[columna]
                resultado[id_] = bboxes[columna]
                usados.add(columna)

        # Nuevos jugadores no emparejados
        for i in range(len(centroides_actuales)):
            if i not in usados:
                self.objetos[self.proximo_id] = centroides_actuales[i]
                resultado[self.proximo_id] = bboxes[i]
                self.proximo_id += 1

        return resultado

