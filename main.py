def alt_caps(original_string):
    """Convert a string to Alternating Caps

    Args:
        original_string (str): A given string with any kind of capitalization
    Returns:
        str: A new string with alternating capitalization
    Examples:
        >>> print(alt_caps("Alternating Capitalization"))
        aLtErNaTiNg CaPiTaLiZaTiOn
    """

    count = 0
    
    newer_string = ""
    for i in original_string:
        count += 1
        if count % 2 == 0:
            upper_character = i.upper()
            newer_string += upper_character
            
        else:
            lower_character = i.lower()
            newer_string += lower_character
    

    return newer_string

print(alt_caps("Alternating Capitalization"))