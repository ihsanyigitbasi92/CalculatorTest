def validate_input(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Invalid input: must be a number.")
