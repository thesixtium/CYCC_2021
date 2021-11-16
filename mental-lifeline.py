from tkinter import *
from tkinter import messagebox
from random import randint
import webbrowser, os, csv

SYMPTOMS = []
SOLUTIONS = []
symptoms_points = {}
common_words = ['of', 'and', 'from', 'or', 'in', 'a', 'the', 'for']

with open('Mental_Illnesses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for i in range(len(row)):
                if row[i] != '':
                    SYMPTOMS.append([row[i], []])
                    SOLUTIONS.append([row[i], []])
                    symptoms_points[row[i]] = 0
        elif line_count != 1:
            index = 0
            for i in range(0, len(row), 2):
                if row[i] != '':
                    SYMPTOMS[index][1].append(row[i].lower())
                    if row[i+1] != '':
                        SOLUTIONS[index][1].append(row[i+1].lower())
                index += 1
        line_count += 1

FILENAME = 'Google.html'

background_color = "#1bb6bd"
foreground_color = "#FFF"

root = Tk()
root.title("Mental Health Lifeline")
root.configure(background=background_color)
root.option_add('*Font', 'Open-Sans 14')
root.geometry("600x400")
root.resizable(0, 0)
root.iconbitmap(os.path.realpath('app-icon.ico'))

frame = LabelFrame(root, padx=30, pady=30, bg=background_color)
frame.pack(padx=10, pady=10, fill='both', expand=True)

button_frame = LabelFrame(root, padx=30, pady=30, bg=background_color)
button_frame.pack(padx=10, pady=10, fill='both', expand=True)

symptom_label = Label(frame, text="Symptom:", bg=background_color,
fg=foreground_color)
symptom_label.grid(row=0, column=0, padx=15)
solution_label = Label(frame, text="Solution:", bg=background_color,
fg=foreground_color)
solution_label.grid(row=1, column=0, pady=50)
message = Label(frame, bg=background_color, fg=foreground_color, wraplength=400)
message.grid(row=1, column=1, sticky='W')

text_input = Entry(frame, width=20)
text_input.grid(row=0, column=1, columnspan=2, sticky='W')

def getSymptom():
    global SYMPTOMS
    global symptoms_points
    given_symptom = text_input.get().lower()
    text_input.delete(0, END)
    for illness in SYMPTOMS:
        for symptom in illness[1]:
            if given_symptom == symptom:
                symptoms_points[illness[0]] += 10
            else:
                for word in given_symptom.split():
                    if word in symptom.split() and word not in common_words:
                        symptoms_points[illness[0]] += 1

def getSolution():
    if max(symptoms_points.values()) == 0:
        messagebox.showerror("Error", "Please enter a symptom")
        return
    diagnosis = max(symptoms_points, key=symptoms_points.get)
    for solution in SOLUTIONS:
        if solution[0] == diagnosis:
            message.configure(text=str(solution[1][randint(0, len(solution[1])-1)]))
            break

def resetScores():
    message.configure(text="")
    for illness in symptoms_points.keys():
        symptoms_points[illness] = 0

submit = Button(button_frame, text="Submit", command=getSymptom,
bg=background_color, fg=foreground_color)
solution = Button(button_frame, text="Solution", command=getSolution,
bg=background_color, fg=foreground_color)
reset = Button(button_frame, text="Reset", command=resetScores,
bg=background_color, fg=foreground_color)
peer_support = Button(button_frame, text="Peer Support",
command=lambda: webbrowser.open('file://' + os.path.realpath(FILENAME), new=2),
bg=background_color, fg=foreground_color)

submit.pack(side=RIGHT, padx=15)
solution.pack(side=RIGHT)
reset.pack(side=RIGHT, padx=15)
peer_support.pack(side=RIGHT)

root.mainloop()
