def main():
    print("Welcome to Terminal Calculator!")
    print("Enter 'quit' to exit\n")
    
    while True:
        expression = input("Enter calculation: ")
        

        if expression.lower() == 'quit':
            print("Goodbye!")
            break


        parts = expression.split()
        if len(parts) != 3:
            print("Please use proper format: (2 + 2)")
            continue
        num1 = float(parts[0])
        num2 = float(parts[2])


        if parts[1] == "+": result = num1 + num2 
        elif parts[1] == "-": result = num1 - num2 
        elif parts[1] == "*" or parts[1] == "x": result = num1 * num2 
        elif parts[1] == "/":
            if num1 == 0 or num2 == 0:
                print("Cannot devide by 0")
                continue 
            result = num1 / num2 
        else: print("Unknown operator")

        print(round(result, 2))

if __name__ == "__main__":
    main()