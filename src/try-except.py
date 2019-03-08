
try:
    number_value = int(input("Enter integer or abc: "))
    division = 10 / 0

except ValueError:
    print("Invalid number value input")
# except ZeroDivisionError:
#     print("Divided by zero")
except ZeroDivisionError as error:
    print(error)
