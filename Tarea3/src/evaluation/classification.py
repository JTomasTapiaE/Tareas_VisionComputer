# evaluation/classification.py

def clasificar_precision(similitud):
    """
    Recibe un valor de similitud (entre 0 y 1) y devuelve una etiqueta:
    'Perfect', 'Good', 'Ok' o 'Bad'
    """
    if similitud >= 0.75:
        return "Perfect"
    elif similitud >= 0.5:
        return "Good"
    elif similitud >= 0.25:
        return "Ok"
    else:
        return "Bad"
# test_classification.py



