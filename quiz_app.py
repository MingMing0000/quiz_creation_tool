#read the txt file
#put the quiz items in a list
#randomize the quiz items
#show the quiz
#get user's answer
#check the answer if it is correct

import random
import tkinter as tk
from tkinter import filedialog

#create a list to store the quiz items
questions = []
question_count = 0
score = 0 

#prevent buttons from showing before selecting a file
def hide_buttons():
    the_question.pack_forget()
    choice_a.pack_forget()
    choice_b.pack_forget()
    choice_c.pack_forget()
    choice_d.pack_forget()
    feedback_label.pack_forget()
    timer.pack_forget()
    score_label.pack_forget()

# Function to show quiz elements
def show_buttons():
    the_question.pack(pady=45)
    choice_a.pack(pady=10)
    choice_b.pack(pady=10)
    choice_c.pack(pady=10)
    choice_d.pack(pady=10)
    feedback_label.pack(pady=20)
    timer.pack(pady=10)
    score_label.pack(pady=15)

# Open file dialog to select a .txt file
def open_quiz_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        # Clear the questions list and insert the new file's content
        questions.clear()
        for line in range(0, len(lines), 7):  # Assuming 7 lines per quiz item
            question = lines[line].strip().replace('Question: ', '')
            choice_a_text = lines[line + 1].strip()
            choice_b_text = lines[line + 2].strip()
            choice_c_text = lines[line + 3].strip()
            choice_d_text = lines[line + 4].strip()
            answer = lines[line + 5].strip().replace('Answer: ', '')

            questions.append({
                'question': question,
                'choices': [choice_a_text, choice_b_text, choice_c_text, choice_d_text],
                'answer': answer
            })

        # Randomize the quiz items
        random.shuffle(questions)

        # Show quiz elements and start the quiz
        open_button.pack_forget()
        welcome_text.pack_forget()
        wlecome_subheading.pack_forget()
        show_buttons()
        global question_count
        question_count = 0  # Reset question count
        display_quiz(question_count)
    else:
        feedback_label.config(text="No file selected.", fg="red")

#making the GUI of the quiz app
root = tk.Tk()
root.title("Quiz App")
root.configure(bg="turquoise")
root.geometry("1280x720")

#Add welcome text
welcome_text = tk.Label(root, text="Welcome to the Quiz App!", font=("Times New Roman", 40), bg="turquoise")
welcome_text.pack(pady=50)
wlecome_subheading = tk.Label(root, text="--Open a quiz file to start--", font=("Times New Roman", 25), fg="gray", bg="turquoise")
wlecome_subheading.pack(pady=20)

#Add a button to open the quiz file
open_button = tk.Button(root, text="Open Quiz File", font=("Times New Roman", 25), bg="lightblue", command=open_quiz_file)
open_button.pack(pady=50)

#making the buttons
the_question = tk.Label(root, text="", font=("Times New Roman", 30), bg="turquoise", wraplength=800)

choice_a = tk.Button(root, text="", font=("Times New Roman", 25), bg="lightblue", width=30, command=lambda: check_answer(0))

choice_b = tk.Button(root, text="", font=("Times New Roman", 25), bg="lightblue", width=30, command=lambda: check_answer(1))

choice_c = tk.Button(root, text="", font=("Times New Roman", 25), bg="lightblue", width=30, command=lambda: check_answer(2))

choice_d = tk.Button(root, text="", font=("Times New Roman", 25), bg="lightblue", width=30, command=lambda: check_answer(3))

# Add a label for feedback when checking answer
feedback_label = tk.Label(root, text="", font=("Times New Roman", 20), bg="turquoise")

# Add a label for countdown timer
timer = tk.Label(root, text="", font=("Times New Roman", 20), bg="turquoise")

# Add a label for score
score_label = tk.Label(root, text="", font=("Times New Roman", 20), bg="turquoise")

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
    question_count += 1
    
    if question_count < len(questions):
        countdown(3)  # 3-second delay before next question
    else:
        score_label.config(text=f"Quiz finished! Your score is: {score}/{len(questions)}", fg="purple")

def countdown(seconds):
    if seconds > 0:
        timer.config(text=f"Next question in {seconds}", fg="blue")
        root.after(1000, countdown, seconds - 1)  
    else:
        move_to_next_question()

def move_to_next_question():
    if question_count < len(questions):
        feedback_label.config(text="")
        timer.config(text="")  
        display_quiz(question_count)

#hide buttons at the start
hide_buttons()

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()