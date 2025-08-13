while True:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
    
    cont = input("Check another age? (y/n): ").lower()
    if cont != 'y':
        break