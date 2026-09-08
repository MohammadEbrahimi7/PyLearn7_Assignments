s_scores = 0
count = 0

while True:
    score = input("enter your number: ")

    s_scores = s_scores + float(score)
    count = count + 1

    choice = input("Do yu want to continue? press enter to continue or type 'exit' to quit: ")
    if choice == "exit":
        break

if count > 0:
    average = s_scores / count
    print("student average: ", average)

else:
    print("no scores were entered.")