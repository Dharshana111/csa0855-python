def find_square_and_cube(number):
    square = number ** 2  
    cube = number ** 3    
    
    return square, cube

number = float(input("Given Number: "))

square, cube = find_square_and_cube(number)

print(f"Square Number: {square}")
print(f"Cube Number: {cube}")
