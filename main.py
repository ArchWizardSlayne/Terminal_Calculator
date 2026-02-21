def main():
    ##############
    ###Greeting###
    ##############
    print("Welcome to Terminal Calculator!")
    print("Enter 'quit' to exit or 'reset' to reset the calculation\n")


    ###############
    ###Main Loop###
    ###############
    while True:
    

        ###########
        ###Input###
        ###########
        expression = input("Enter calculation: ")
        
        if expression.lower() == 'quit':
            print("Goodbye!")
            quit()


        #################################
        ###Split Expression into Parts###
        #################################
        parts = expression.split()
        if len(parts) != 3:
            print("Please use proper format: (2 + 2)")
            continue
        num1 = float(parts[0])
        num2 = float(parts[2])


        ###############
        ###Calculate###
        ###############
        if parts[1] == "+": result = num1 + num2 
        elif parts[1] == "-": result = num1 - num2 
        elif parts[1] == "*" or parts[1] == "x": result = num1 * num2 
        elif parts[1] == "/":
            if num2 == 0:
                print("Cannot devide by 0")
                continue 
            result = num1 / num2 
        else: print("Unknown operator")

        print(round(result, 2))
        
        
        #################################
        ###Continuous Calculation Loop###
        #################################
        while True:


            ###########
            ###Input###
            ###########
            expression = input()

            if expression.lower() == "quit":
                print("Goodbye!")
                quit()
            elif expression.lower() == "reset":
                break


            #################################
            ###Split Expression into Parts###
            #################################
            parts = expression.split()
            if len(parts) != 2:
                print("Try Again")
                continue
            num1 = float(result)
            num2 = float(parts[1])


            ###############
            ###Calculate###
            ###############
            if parts[0] == "+": result = num1 + num2 
            elif parts[0] == "-": result = num1 - num2 
            elif parts[0] == "*" or parts[0] == "x": result = num1 * num2 
            elif parts[0] == "/":
                if num2 == 0:
                    print("Cannot devide by 0")
                    continue 
                result = num1 / num2 
            else: print("Unknown operator")

            print(round(result, 2))

if __name__ == "__main__":
    main()