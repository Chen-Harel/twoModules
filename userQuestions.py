def studentInfo(name, age, gender):
    print(name + " is in this school.")
    if gender.lower() == "male":
        return f"He is {age} years old."
    else:
        return f"She is {age} years old."
