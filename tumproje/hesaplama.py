from error import InvalidHeightError, InvalidWeightError, EmptyInputError

def hesapla_bmi(boy_cm, kilo_kg):
    if not boy_cm or not kilo_kg:
        raise EmptyInputError()

    try:
        boy = float(boy_cm)
    except ValueError:
        raise InvalidHeightError("Boy sayısal bir değer olmalıdır.")
    if boy <= 0:
        raise InvalidHeightError()

    try:
        kilo = float(kilo_kg)
    except ValueError:
        raise InvalidWeightError("Kilo sayısal bir değer olmalıdır.")
    if kilo <= 0:
        raise InvalidWeightError()

    bmi = kilo / ((boy / 100) ** 2)
    return round(bmi, 2)
