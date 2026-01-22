import random
import os 
import requests
from datetime import date
import requests
from datetime import date
#gpt shit
# Get today's date in YYYY-MM-DD format
today_date = date.today().isoformat()

# Construct the API URL for today's date
url = f"https://www.nytimes.com/svc/wordle/v2/{today_date}.json"

try:
    response = requests.get(url)
    # Check if the request was successful
    response.raise_for_status()

    data = response.json()
    wordle_answer = data.get("solution")

    if wordle_answer:
        pass
    else:
        pass

except requests.exceptions.RequestException as e:
    pass
#gpt shit end
current_dir = os.path.dirname(__file__)
guesses_path = os.path.join(current_dir,'guesses.txt')
guesses = open(guesses_path)
def dick(answer):
    output_list_1 = []
    output_list_2 = []
    output_list_3 = []
    guesses_str = guesses.read()
    guesses_list = guesses_str.split( );
    for list_word in guesses_list:
        if list_word[2] == answer[2]:
            if list_word[0] != answer[0] and list_word[1] != answer[1] and list_word[3] != answer[3] and list_word[4] != answer[4]:
                output_list_1.append(list_word)
        elif list_word[1] == answer[1] and list_word[3] == answer[3]:
            if list_word[0] != answer[0] and list_word[2] != answer[2] and list_word[4] != answer[4]:
                output_list_2.append(list_word)
        elif list_word[0] != answer[0] and list_word[1] != answer[1] and list_word[2] != answer[2] and list_word[3] != answer[3] and list_word[4] != answer[4]:
            output_list_3.append(list_word)
    line_1 = output_list_1[random.randint(0,len(output_list_1)-1)]
    line_2 = output_list_1[random.randint(0,len(output_list_1)-1)]
    line_3 = output_list_1[random.randint(0,len(output_list_1)-1)]
    line_4 = output_list_2[random.randint(0,len(output_list_2)-1)]
    line_5 = output_list_3[random.randint(0,len(output_list_3)-1)]
    line_6 = answer
    guesses.close()
    return f'{line_1}\n{line_2}\n{line_3}\n{line_4}\n{line_5}\n{line_6}'
def autodick():
    autoreturn = dick(wordle_answer)
    return autoreturn
#run as script, basically equals to wddick_run
if __name__ == "__main__":
    input_answer = input("Enter a five letter word or today's wordle answer:\n")
    while len(input_answer) != 5:
        print("I told u to enter 5 letter word!")
        input_answer = input("Enter a five letter word or today's wordle answer:\n")
    print("Now enter\n" + dick(input_answer) + "\ninto wordle :)")

