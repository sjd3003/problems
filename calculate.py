def calculate_area(length, width):
    return length*width

def calculate_perimeter(length, width):
    return 2*(length+width)

def main():
    # Get user input for length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Call the functions to calculate area and perimeter
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    # Display the results
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

# Call the main function to run the program
main()
