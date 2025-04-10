#read the txt file
#put the quiz items in a list
#randomize the quiz items
#show the quiz
#get user's answer
#check the answer if it is correct

import random
import tkinter as tk
#create a list to store the quiz items
questions = []
question_count = 0
score = 0 
#read the quiz from the text file
with open('quiz_creator.txt', 'r') as file:
    lines = file.readlines()

#put the items to the list
for line in range(0, len(lines), 7): # there's 7 lines per quiz item including the empty line
    question = lines[line].strip().replace('Question: ', '').capitalize()
    choice_a = lines[line + 1].strip()
    choice_b = lines[line + 2].strip()
    choice_c = lines[line + 3].strip()
    choice_d = lines[line + 4].strip()
    answer = lines[line + 5].strip().replace('Answer: ', '')

    questions.append({
        'question': question,
        'choices': [choice_a, choice_b, choice_c, choice_d],
        'answer': answer
    })

#randomize the quiz items
random.shuffle(questions)

#making the GUI of the quiz app
root = tk.Tk()
root.title("Quiz App")
root.configure(bg="turquoise")
root.geometry("1280x720")

the_question = tk.Label(root, text="", font=("Times New Roman", 30), bg="turquoise", wraplength=800)
the_question.pack(pady=50)
#making the buttons
choice_a = tk.Button(root, text="", font=("Times New Roman", 25), bg="lightblue", width=30, command=lambda: check_answer(0))
choice_a.pack(pady=10)

choice_b = tk.Button(root, text="", font=("Times New Roman", 25), bg="lightblue", width=30, command=lambda: check_answer(1))
choice_b.pack(pady=10)

choice_c = tk.Button(root, text="", font=("Times New Roman", 25), bg="lightblue", width=30, command=lambda: check_answer(2))
choice_c.pack(pady=10)

choice_d = tk.Button(root, text="", font=("Times New Roman", 25), bg="lightblue", width=30, command=lambda: check_answer(3))
choice_d.pack(pady=10)

# Add a label for feedback when checking answer
feedback_label = tk.Label(root, text="", font=("Times New Roman", 20), bg="turquoise")
feedback_label.pack(pady=20)

def display_quiz(index):
    the_question.config(text=questions[index]['question'])
    choice_a.config(text=questions[index]['choices'][0])
    choice_b.config(text=questions[index]['choices'][1])
    choice_c.config(text=questions[index]['choices'][2])
    choice_d.config(text=questions[index]['choices'][3])

def check_answer(choice_index):
    global question_count, score
    correct_answer = questions[question_count]["answer"]
    if questions[question_count]['choices'][choice_index][0] == correct_answer:
        feedback_label.config(text="✔️ Correct!", fg="green")
        score += 1
    else:
        feedback_label.config(text=f"❌ Wrong! The correct answer is: {correct_answer}", fg="red")

#display_quiz(question_count)
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
'''
score = 0 #will be used to count the score

#showing the quiz
print('\nQuiz: Read the question and choose the correct answer from the choices.\n')
#using for loop to show the quiz one at a time
for question in questions:
    print(f'Question: {question['question']}')
    for index, letter in enumerate(['A', 'B', 'C', 'D']):
        print(f'{letter}) {question['choices'][index]}')

    #get and check the user's answer
    user_answer = input('What is your answer? (A/B/C/D): ').strip().upper()
    if user_answer == question['answer'].upper():
        print('\nYour answer is correct! ✔️')
        score += 1
    else:
        print(f'\nYour answer is wrong! ❌ The correct answer is {question['answer'].upper()}')
    print()

print('\n----End of the quiz.----')
print(f'\nYour score is {score}/{len(questions)}') #show the score'''