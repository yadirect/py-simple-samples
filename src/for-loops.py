
for letter in "Python":
    print(letter)

print("\n")


friends = ["Jim", "Karen", "Kevin"]
for friends in friends:
    print(friends)

print("\n")


friends = ["Kevin", "Karen", "Jim"]
for name in friends:
    print(name)

print("\n")


for index in range(10):
    print(index)

print("\n")


for index in range(3, 10):
    print(index)

print("\n")


friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(index)

for index in range(len(friends)):
    print(friends[index])

print("\n")


for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first iteration")
