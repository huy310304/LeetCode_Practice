def check_subsequence(s:str, t:str) -> bool:
    if s == t or s == "": return True

    i = 0
    for letter in t:
        if s[i] == letter:
            i += 1
            if i == len(s):
                return True
    
    return False
