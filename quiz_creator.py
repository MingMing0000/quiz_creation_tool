#ask question
# choices
#  a
#  b
#  c
#  d
# answer
# save into txt file

quiz_list = []
print('Quiz Creator')
#ask the user for the question, choices, and answer
while True:
    question = input('Input your question (type "exit" to stop): ')
    if question.lower() == "exit":
        break
    print('Input your choices')
    choice_a = input('Input choice a: ')
    choice_b = input('Input choice b: ')
    choice_c = input('Input choice c: ')
    choice_d = input('Input choice d: ')
    answer = input('Input the correct answer from the choices: ')

    #append the inputs into a list
    quiz_list.append({
        'question': question,
        'choices': [choice_a, choice_b, choice_c, choice_d],
        'answer': answer
    })