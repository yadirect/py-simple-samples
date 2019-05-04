import random

var1 = 1000
var2 = "abc"
list1 = ["A", "B", "C"]


def get_random(num):
    return random.randint(1, num)


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]
