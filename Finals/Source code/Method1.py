def main():
    # Find the largest number among three numbers
    L = []

    # Input the three numbers
    num1 = float(input("Enter the first number: "))
    L.append(num1)

    num2 = float(input("Enter the second number: "))
    L.append(num2)

    num3 = float(input("Enter the third number: "))
    L.append(num3)

    # Find and print the largest number
    largest_number = max(L)
    print("The largest number among the three is:", largest_number)

# Call the main function
if __name__ == "__main__":
    main()