def decode_message(message: str, decoder_key: str) -> bool:
    if len(message) != len(decoder_key):  
        return False
    
    for i in range(len(message)):  # Iterate through each character
        if decoder_key[i] == '?':  # Check if it's a question mark
            continue  # Move to the next character
        elif decoder_key[i] == '*':  # Check if it's a star symbol
            continue  # Move to the next character
        elif decoder_key[i] != message[i]:  # Check if characters don't match
            return False  # If they don't match, return False
    
    return True  # If all characters match or are wildcard symbols, return True
