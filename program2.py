def decode_message(s: str, p: str) -> bool:
    if len(s) != len(p):  # Check if the lengths of the message and decoder key are the same
        return False
    
    for i in range(len(s)):  # Iterate through each character in the message and decoder key
        if p[i] != '*' and p[i] != '?' and p[i] != s[i]:  # Check if the characters don't match
            return False
    
    return True  # If all characters match or are wildcard symbols, return True

# Test cases
print(decode_message("aa", "a"))  # Output: False
print(decode_message("aa", "*"))  # Output: True
print(decode_message("cb", "?a"))  # Output: False
