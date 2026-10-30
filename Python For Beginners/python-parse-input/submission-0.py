from typing import List

def read_integers() -> List[int]:
    string_list = input()
    string_list = string_list.split(",")
    return [int(x) for x in string_list]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
