def count_vowels(input_string):
    vowels = 'aeiouAEIOU'  
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1  
    
    return count

input_string = input("Enter the string: ")

vowel_count = count_vowels(input_string)
print(f"Number of vowels = {vowel_count}")
