# person.py

class Person:
    def __init__(self, name, age, gender):  # Corrected to double underscores
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# If you want to run this file directly, you can include the following
if __name__ == "__main__":  # Corrected to double underscores
    # Create instances of the Person class
    bridget = Person(name="Bridget", age=19, gender="Female")
    eliud = Person(name="Eliud", age=25, gender="Male")

    # Display the information for each person
    bridget.display_info()
    print()  # Add a newline for better readability
    eliud.display_info()
