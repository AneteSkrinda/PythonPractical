text = input("Enter some text: ")
letter = input("Enter a letter: ")

count = 0
for char in text:
    if char == letter:
        count += 1

print("The letter '{}' occurs {} times in the text.".format(letter, count))

#1.1 task
text = input("Enter some text: ")

char_counts = {}
for char in text:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

print("Character counts:")
for char, count in char_counts.items():
    print("'{}': {}".format(char, count))