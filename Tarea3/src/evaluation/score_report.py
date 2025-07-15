# evaluation/score_report.py

import os

class ScoreManager:
    def __init__(self):
        # Dict por jugador: {id_jugador: {"Perfect": x, "Good": y, ...}}
        self.data = {}

    def registrar(self, jugador_id, clasificacion):
        """
        Guarda una clasificación (Perfect, Good, etc.) para un jugador.
        """
        if jugador_id not in self.data:
            self.data[jugador_id] = {"Perfect": 0, "Good": 0, "Ok": 0, "Bad": 0}

        if clasificacion in self.data[jugador_id]:
            self.data[jugador_id][clasificacion] += 1
        else:
            self.data[jugador_id]["Bad"] += 1  # default si clasificación no válida

    def calcular_estrellas(self, jugador_id):
        """
        Calcula estrellas en escala de 0 a 5 según proporción ponderada.
        """
        clasif = self.data[jugador_id]
        total = sum(clasif.values())

        if total == 0:
            return 0.0

        puntos = (
            clasif["Perfect"] * 1.0 +
            clasif["Good"] * 0.75 +
            clasif["Ok"] * 0.5 +
            clasif["Bad"] * 0.0
        )

        estrellas = 5 * (puntos / total)
        return round(estrellas, 2)

    def generar_reportes(self, carpeta_salida):
        os.makedirs(carpeta_salida, exist_ok=True)

        for jugador_id, conteos in self.data.items():
            total = sum(conteos.values())
            estrellas = self.calcular_estrellas(jugador_id)

            with open(os.path.join(carpeta_salida, f"jugador_{jugador_id}.txt"), "w") as f:
                f.write(f"Jugador {jugador_id}\n")
                f.write("-" * 30 + "\n")
                f.write(f"Total poses evaluadas: {total}\n")
                for clase in ["Perfect", "Good", "Ok", "Bad"]:
                    f.write(f"{clase}: {conteos[clase]}\n")
                f.write(f"Estrellas: {estrellas} *\n")


                if estrellas >= 4.5:
                    resumen = "Excelente"
                elif estrellas >= 3.5:
                    resumen = "Muy bueno"
                elif estrellas >= 2.5:
                    resumen = "Aceptable"
                else:
                    resumen = "Debe mejorar"

                f.write(f"Clasificación final: {resumen}\n")
