def calculate_right_side(digit):
    return {
        'original': digit,
        'add_3': (digit + 3) % 10,
        'add_2': (digit + 2) % 10,
        'add_1': (digit + 1) % 10
    }

def calculate_left_side(digit):
    return {
        'original': digit,
        'subtract_3': (digit - 3) % 10,
        'subtract_2': (digit - 2) % 10,
        'subtract_1': (digit - 1) % 10
    }

def main():
    print("Select an option:")
    print("1. 3-digit number")
    print("2. 4-digit number")
    print("3. 5-digit number")
    
    option = input("Enter your option (1/2/3): ")
    
    if option == '1':
        length = 3
    elif option == '2':
        length = 4
    elif option == '3':
        length = 5
    else:
        print("Invalid option.")
        return
    
    input_number = input(f"Enter a {length}-digit number: ")
    
    if len(input_number) != length or not input_number.isdigit():
        print(f"Please enter a valid {length}-digit number.")
        return

    print("\nCalculations:")
    for digit in input_number:
        num = int(digit)
        
        # Right side calculations (add)
        right_results = calculate_right_side(num)
        
        # Left side calculations (subtract)
        left_results = calculate_left_side(num)
        
        print(f"Digit: {digit}")
        print("Right Side Calculations (Add):")
        for key, value in right_results.items():
            print(f"  {key}: {value}")
        
        print("Left Side Calculations (Subtract):")
        for key, value in left_results.items():
            print(f"  {key}: {value}")
        print()

if __name__ == "__main__":
    main()
