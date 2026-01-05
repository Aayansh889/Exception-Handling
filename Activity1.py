try:
    num=int(input("Enter a number:"))
    print("Number is",num)
except ValueError:
    print("A value error has occured because your input is not an integer")