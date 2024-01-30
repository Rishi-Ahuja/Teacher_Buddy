def calculate_square(number):
    result = number * number
    return result

def main():
    n = int(input("Enter a number: "))
    square_result = calculate_square(n)
    print(f"The square of {n} is: {square_result}")

if __name__ == "__main__":
    main()
