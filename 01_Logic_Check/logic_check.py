def get_type(age):
    return "Adult" if age >= 18 else "Minor"

# Standard input process for beginners
name = input("Name: ")

try:
    age = int(input("Age: "))
    # Combining the input and the logic function
    print(f"Summary: {name} - {get_type(age)}")
except ValueError:
    print("Error: Please enter a valid number for age.")