def is_perfect_triangle(side1, side2, side3):
    # Check if the sum of squares of two shorter sides equals the square of the longest side
    if side1**2 + side2**2 == side3**2 or side2**2 + side3**2 == side1**2 or side3**2 + side1**2 == side2**2:
        return True
    else:
        return False

# Input side lengths as multiples of 3, 4, and 5
side1 = int(input("Enter the length of side 1 (multiple of 3): "))
side2 = int(input("Enter the length of side 2 (multiple of 4): "))
side3 = int(input("Enter the length of side 3 (multiple of 5): "))

if is_perfect_triangle(side1, side2, side3):
    print("It's a perfect triangle!")
else:
    print("It's not a perfect triangle.")
