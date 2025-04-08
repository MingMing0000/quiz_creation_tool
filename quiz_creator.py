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
    answer = input('Input the correct answer from the choices(a,b,c,d): '); print()

    #append the inputs into a list
    quiz_list.append({
        'question': question,
        'choices': [choice_a, choice_b, choice_c, choice_d],
        'answer': answer
    })

#save the question, choices, and answer into a txt file
with open('quiz_creator.txt', 'a') as file:
    for quiz in quiz_list:
        file.write(f"Question: {quiz['question']}\n")
        file.write(f"a) {quiz['choices'][0]}\n")
        file.write(f"b) {quiz['choices'][1]}\n")
        file.write(f"c) {quiz['choices'][2]}\n")
        file.write(f"d) {quiz['choices'][3]}\n")
        file.write(f"Answer: {quiz['answer']}\n")
        file.write('\n')

print('\nYour quiz has been saved to quiz_creator.txt')