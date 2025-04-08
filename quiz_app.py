#read the txt file
#put the quiz items in a list
#randomize the quiz items
#show the quiz
#get user's answer
#check the answer if it is correct

import random
#create a list to store the quiz items
questions = []

#read the quiz from the text file
with open('quiz_creator.txt', 'r') as file:
    lines = file.readlines()

#put the items to the list
for line in range(0, len(lines), 7): # there's 7 lines per quiz item including the empty line
    question = lines[line].strip().replace('Question: ', '')
    choice_a = lines[line + 1].strip()[3:]
    choice_b = lines[line + 2].strip()[3:]
    choice_c = lines[line + 3].strip()[3:]
    choice_d = lines[line + 4].strip()[3:]
    answer = lines[line + 5].strip().replace('Answer: ', '')

    questions.append({
        'question': question,
        'choices': [choice_a, choice_b, choice_c, choice_d],
        'answer': answer
    })