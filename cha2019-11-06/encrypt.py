def encrypt(text, rule):
    return "".join(chr((i+rule)%256) for i in map(ord, text)) 
