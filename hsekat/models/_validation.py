def validate_energy(value: float) -> float:
    if type(value) not in (int, float):
        raise ValueError("Энергопотребление должно быть числом")
    if value < 0:
        raise ValueError("Энергопотребление не может быть отрицательным")
    return float(value)
