def calculate_square(n):
    result = n * n
    return result

def main():
    number = int(input("Enter a number: "))
    square_result = calculate_square(number)
    print(f"The square of {number} is: {square_result}")

if __name__ == "__main__":
    main()
