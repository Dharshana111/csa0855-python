def is_valid_number(s: str) -> bool:
    """
    Validates if the input string represents a valid number, optionally starting with a '+' or '-'.

    Parameters:
        s (str): Input string to validate.

    Returns:
        bool: True if the string represents a valid number, False otherwise.
    """
    stripped_string = s.strip()
    
    if not stripped_string:
        return False
    
    if stripped_string[0] in ('+', '-'):
        stripped_string = stripped_string[1:]  
    
    try:
        float(stripped_string)
        return True
    except ValueError:
        return False

# Test cases
print(is_valid_number("  +123  "))     
print(is_valid_number(" -45.67"))      
print(is_valid_number(" 123abc"))     
print(is_valid_number("  +  "))        
print(is_valid_number("   "))         
