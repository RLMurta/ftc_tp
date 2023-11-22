def copy_dict(input_dict):
    """
    Cria uma cópia profunda de um dicionário.

    Args:
        input_dict (dict): O dicionário a ser copiado.

    Returns:
        dict: Uma cópia profunda do dicionário de entrada.
    """
    new_dict = input_dict.copy()

    # Copia cada valor do dicionário interno para garantir uma cópia profunda
    for key in input_dict:
        new_dict[key] = input_dict[key].copy()

    return new_dict
