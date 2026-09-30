str = input("enter a string: ")
length = len(str)
half_index = length // 2
lower_half = str[:half_index].lower()
upper_half = str[half_index:].upper()
print(lower_half + upper_half)
