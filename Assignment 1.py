while True:
    n = int(input("Enter number of row: "))    # This tells the number of rows to print
    for i in range(1, n+1):                    # It iterates the given conditions and executes trhe following each if statements when the conditions are satisfied
        if i ==1:
            print('  *')
        if i==2:    
            print("  **")
        if i==3:    
            print(" ***")   
        if i>3:
            print("*"*i)   



