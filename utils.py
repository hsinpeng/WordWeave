import random, string


def gen_random_string(length:int=10, is_punctuation:bool=False) -> str:
    """
    Generate a random string of a specific length.
    """
    if is_punctuation:
        characters = string.ascii_letters + string.digits + string.punctuation
    else: 
        characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
