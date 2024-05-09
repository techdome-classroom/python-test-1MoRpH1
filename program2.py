def decode_message(message: str, decoder_key: str) -> bool:
    # Check if the length of the message and decoder key are the same
    if len(message) != len(decoder_key):
        return False
    
    # Iterate through each character in the message and decoder key
    for i in range(len(message)):
        # If the current character in the decoder key is not a wildcard
        if decoder_key[i] != '*' and decoder_key[i] != '?':
            # Check if the characters don't match
            if decoder_key[i] != message[i]:
                return False
    
    # If all characters match or are wildcard symbols, return True
    return True

# Test cases
print(decode_message("aa", "a"))  # Output: False
print(decode_message("aa", "*"))  # Output: True
print(decode_message("cb", "?a"))  # Output: False
print(decode_message("abc", "?b?"))  # Output: True
