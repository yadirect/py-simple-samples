
# text.txt
# Text string 1
# Text string 2
# Text string 3
# Text string 4
# Text string 5

text_file = open("text.txt", "a")
text_file.write("# Text string 6")
text_file.close()

text_file = open("text.txt", "a")
text_file.write("\n# Text string 7")
text_file.close()

text_file = open("text.txt", "w")
text_file.write("\n# Text string 7")
text_file.close()

text_file = open("text1.txt", "w")
text_file.write("\n# Text string 7")
text_file.close()

text_file = open("index.html", "w")
text_file.write("HTML code")
text_file.close()
