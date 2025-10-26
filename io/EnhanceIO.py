import unicodedata

def get_text(msg:str)->str:
    txt = input(msg)
    txt = str(txt).strip()
    if len(txt) == 0:
        return ""
    
    # Normalize to NFC form to handle special characters
    txt = unicodedata.normalize('NFC', txt)

    # Remove non-UTF-8 characters
    txt = txt.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
    return txt

def get_int(msg:str)->int:
    return 0

def get_select(msg:str, options: list[str]) -> str:
    print(msg)
    index = 1
    map_option = {}
    for option in options:
        patterns = option.split(",")
        if len(patterns) < 2: 
            continue
        map_option[index] = patterns[1]
        print(f"{index}. {patterns[0]}")
        index = index + 1

    text = input(f"Enter your select (0 or x to quit): ")
    if text is None or len(text.strip()) == 0:
        return None
    
    if text in["0","x"]:
        return text
    try:
        index = int(text.strip())
        if index not in map_option:
            print(f"Keyword \"{text}\" is invalid.")
            return None
        return map_option[index]
    except Exception as e:
        print(f"Keyword \"{text}\" is invalid.")
        return None
        pass
    

    