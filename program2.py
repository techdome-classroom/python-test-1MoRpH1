def decode_message(message: str, decoder_key: str) -> bool:
    if len(message) != len(decoder_key):  
        return False
    
    for i in range(len(message)):  
        if decoder_key[i] == '?':  
            continue  
        elif decoder_key[i] == '*': 
            continue  
        elif decoder_key[i] != message[i]:  
            return False  
    
    return True 
