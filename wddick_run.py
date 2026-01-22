import __init__
input_answer = input("Enter a five letter word or today's wordle answer:\n")
while len(input_answer) != 5:
    print("I told u to enter 5 letter word!")
    input_answer = input("Enter a five letter word or today's wordle answer:\n")
print("Now enter\n" + __init__.dick(input_answer) + "\ninto wordle :)")