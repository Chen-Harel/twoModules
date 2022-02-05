def calculator(calc, x, y):
    if calc == "add":
        return x+y
    elif calc == "subtract":
        return x-y
    elif calc == "multiply":
        return x*y
    elif calc == "divide":
        return x/y
    else:
        return "You must pick add, subtract, multiply, or divide."