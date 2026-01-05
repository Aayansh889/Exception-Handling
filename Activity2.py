try:
    num1,num2= eval(input("Enter two numbers, separated by a comma:"))
    result= num1/num2
    result=round(result, 2)
    print("The answer is",result)
except SyntaxError:
    print("Comma is missing.Enter numbers separated by commas.")
except ZeroDivisionError:
    print("We cant divide by zero since its mathematically wrong")
except:
    print("Wrong input")
finally:
    print("This will always print")