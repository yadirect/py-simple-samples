
# text.txt
# Text string 1
# Text string 2
# Text string 3
# Text string 4
# Text string 5

# open("text.txt", "r")   # read
# open("text.txt", "w")   # write
# open("text.txt", "a")   # append to the end
# open("text.txt", "r+")  # read and write

text_file = open("text.txt", "r")
print(text_file.readable())
text_file.close()

# text_file = open("text.txt", "w")  # It wipes the file
# print(text_file.readable())
# text_file.close()

text_file = open("text.txt", "r")
print(text_file.read())
text_file.close()

text_file = open("text.txt", "r")
print(text_file.readline())
print(text_file.readline())
text_file.close()

text_file = open("text.txt", "r")
print(text_file.readlines())
text_file.close()

text_file = open("text.txt", "r")
print(text_file.readlines()[2])
text_file.close()

text_file = open("text.txt", "r")
for text in text_file.readlines():
    print(text)
text_file.close()
