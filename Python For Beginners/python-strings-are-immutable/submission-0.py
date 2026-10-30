def remove_fourth_character(word: str) -> str:
    before_second = word[:3]
    after_second = word[4:]
    
    daddy = before_second + after_second
    return daddy


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
