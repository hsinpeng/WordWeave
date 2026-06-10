import random, string, opencc


def gen_random_string(length:int=10, is_punctuation:bool=False) -> str:
    """
    Generate a random string of a specific length.
    """
    if is_punctuation:
        characters = string.ascii_letters + string.digits + string.punctuation
    else: 
        characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def chinese_conversion(intput:str, target:str="TW") -> str:
    """
    Simplified/Traditional Chinese conversion
    """
    config_file:str = ""
    match target:
        case "TW":
            config_file = "s2tw.json"
        case "CN":
            config_file = "t2s.json"
        case "HK":
            config_file = "s2hk.json"
        case _:
            print(f"Error: Wrong target({target}).") 
            return None
    try:
        converter = opencc.OpenCC(config_file)
        return converter.convert(intput)
    except Exception as e:
        print(f"Unknown Error: {e}") 
        return None