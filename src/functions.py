

def say_hi():
    print("Hello user")

print("Top")
say_hi()
print("Bottom\n")


def say_hi_name(name):
    print("Hello " + name + "!")

say_hi_name("Mike")
say_hi_name("Steve")
print("\n")


def say_hi_name_age(name, age):
    print("Hello " + name + ", you are " + age)

say_hi_name_age("Mike", "33")
say_hi_name_age("Steve", "22")
print("\n")


def say_hi_name_age_int(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi_name_age_int("Mike", 33)
say_hi_name_age_int("Steve", 22)
print("\n")
