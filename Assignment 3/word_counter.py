sentence = input("enter a sentence: ")

count = 0

for word in sentence.split():
    count += 1

print(count)