def remove_vowels(s):
    vowels = "aeiouAEIOU"
    new_str = ""
    
    for char in s:
        if char not in vowels:
            new_str += char
    return new_str

print(remove_vowels("vamshi"))


