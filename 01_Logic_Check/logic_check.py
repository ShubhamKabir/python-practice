def get_type(age):
    return "Adult" if age >= 18 else "Minor"

name = input("Name: ")
try:
    age = int(input("Age: "))
    print(f"Summary: {name} - {get_type(age)}")
except:
    print("Enter a number.")