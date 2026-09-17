import random

words_bank = ["tree", "book", "blue", "fish", "woman", "man", "iran", "sky", "train", "life"]
user_mistakes = 0

good_chars = []
bad_chars = []

x = random.randint(0, len(words_bank)-1)
word = words_bank[x]

while user_mistakes < 6:
    for i in range(len(word)):
         if word[i] in good_chars:
             print(word[i], end=" ")

         else:
            print("- ", end=" ")


    if all(char in good_chars for char in word):
        print()
        print("you win👏")        
        break

    user_char = input("please write your guess: ").lower()
    if len(user_char) == 1:
        if user_char in word:
            good_chars.append(user_char)
            print("✅")
        else:
            bad_chars.append(user_char)
            user_mistakes +=1
            print("❌")

    else:
        print("mesle adam vared kon: ")

    if user_char == 6:
        print("game over⚰️")
