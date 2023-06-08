name = input("What is your name: ")
age = int(input(f"How old are you {name}? "))

def print_my_information():
    print(f"Your name is {name}, and you are {age} years old")


def print_random_data(item1, item2):
    print(f"You provided a value of {item1} for item1, and a value of {item2} for item two")

def get_number_of_decades_lived(age):
    return int(age/10)

print_my_information()
print_random_data(name, age)

print(f"You have lived {get_number_of_decades_lived(age)} full decades.")