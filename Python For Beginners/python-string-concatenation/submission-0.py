def concatenate(s1: str, s2: str) -> str:
    daddy = s1 + s2
    if(len(daddy) > 10):
        return "Too long!"
    else:
        return daddy




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
