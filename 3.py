input_string = input("Enter your string: ")

words = input_string.split()

word_count = {}
for word in words:
    word = word.lower()  
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Each word repeated:", word_count)