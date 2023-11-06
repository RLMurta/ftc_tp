def copy_dict(dict):
    new_dict = dict.copy()
    for key in dict:
        new_dict[key] = dict[key].copy()
    return new_dict
