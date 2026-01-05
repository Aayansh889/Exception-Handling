valid=False

while not valid:
    try:
        n=int(input("Enter any number:"))
        while n%2==0:
            valid=True
            print("Bye")
    except ValueError:
        print("Invalid")
    except:
        print("How do you even get here?")