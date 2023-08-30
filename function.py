from datetime import *


def convert_date(date):
    return datetime.strptime(date, '%d.%m.%Y')


def sortDate(date):
    return sorted(date, key=convert_date)


def predictionAnnuelle(observation, times, model, encoder):
    start_date = datetime.now().date()
    for i in range(1, times):

        # Calculer le nombre de jours prédits par le modèle
        predicted_days = model.predict(encoder.transform(observation).toarray())[0]
        predicted_date = start_date + timedelta(days=int(predicted_days)) / 365.5

        # Vérifier si la date prédite est valide
        if predicted_date.year < 1 or predicted_date.year > 9999:
            print("La date prédite est invalide.")

        # Mettre à jour la date de début pour la prochaine prédiction
        start_date = predicted_date + timedelta(days=1)
    return start_date.strftime('%d.%m.%Y')


def ExcelConvertDate(date):
    try:
        entier = int(date)
        return (datetime(1900, 1, 1) + timedelta(days=entier - 2)).strftime('%d.%m.%Y')

    except Exception:
        print("Erreur de conversion en Entier détectée")


def ReverseExcelConvertDate(date_str):
    try:
        target_date = datetime.strptime(date_str, '%d.%m.%Y')
        base_date = datetime(1900, 1, 1)
        delta = target_date - base_date
        entier = delta.days + 2
        return str(entier)

    except Exception:
        print("Erreur de conversion de date détectée")

