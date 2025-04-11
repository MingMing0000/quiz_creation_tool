#ask question
# choices
#  a
#  b
#  c
#  d
# answer
# save into txt file

quiz_list = []
print('Quiz Creator\n')

def show_menu():
    print('Menu:')
    print('1. Create a Quiz')
    print('2. Exit')

#ask the user for the question, choices, and answer
def make_quiz():
    question = input('Input your question: ')
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
def save_quiz():
    print('---Saving quiz...---')
    with open(quiz_name, 'a') as file:
        for quiz in quiz_list:
            file.write(f"Question: {quiz['question']}\n")
            file.write(f"a) {quiz['choices'][0]}\n")
            file.write(f"b) {quiz['choices'][1]}\n")
            file.write(f"c) {quiz['choices'][2]}\n")
            file.write(f"d) {quiz['choices'][3]}\n")
            file.write(f"Answer: {quiz['answer']}\n")
            file.write('\n')
    print(f'\n---Your quiz has been saved as {quiz_name}.---\n')

while True:
    show_menu()
    choice = input('Choose an option: ')
    if choice == '1':
        print(); make_quiz()
        while True:
            add_more = input('Do you want to add another question? (y/n): ')
            if add_more.lower() == 'y':
                print(); make_quiz()
            elif add_more.lower() == 'n':
                save = input('Do you want to save the quiz? (y/n): ')
                if save.lower() == 'y':
                    quiz_name = input('Enter the file name of the quiz: ')
                    quiz_name += '.txt'
                    save_quiz()
                    break
                elif save.lower() == 'n':
                    print('--Quiz not saved.--\n')
                    quiz_list.clear()
                    break
                else:
                    print('Invalid option, please try again.\n')    
            else:
                print('Invalid option, please try again.\n')
    elif choice == '2':
        print('\n--Exiting...--')
        break
    else:
        print('Invalid option, please try again.\n')