import tkinter as tk
from tkinter import messagebox
from control import GradeControl
import csv

def cal_avg():
    try:
        numStudent = int(num_students_entry.get())
        if numStudent < 1 or numStudent > 6:
            messagebox.showerror("Error", "Number of students must be between 1 and 6!")
            return
    except ValueError:
        messagebox.showerror("Error", "Number of students must be an integer!")
        return

    scores = []
    for entry in scores_entry:
        try:
            score = int(entry.get())
            if score < 0 or score > 100:
                messagebox.showerror("Error", "Score must be between 0 and 100!")
                return
        except ValueError:
            score = 0
        scores.append(score)

    controller = GradeControl(scores)
    student_grades = controller.get_grades()
    avg, avg_grade = controller.get_avg_and_grade()

    result_text.delete(1.0, tk.END)
    for student in student_grades:
        result_text.insert(tk.END, f"Student {student[0]} score is {student[1]} and grade is {student[2]}\n")
    result_text.insert(tk.END, f"The average score is {avg:.2f} a grade of {avg_grade}\n")

    with open('StudentScores.csv', 'w', newline='') as csvfile:
        fieldnames = ['Student', 'Score', 'Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_grades:
            writer.writerow({'Student': f'Student {student[0]}', 'Score': student[1], 'Grade': student[2]})
        writer.writerow({'Student': 'Average', 'Score': avg, 'Grade': avg_grade})

def score_entry():
    for widget in score_frame.winfo_children():
        widget.destroy()
    global scores_entry
    scores_entry = []
    try:
        numStudent = int(num_students_entry.get())
        if numStudent < 1 or numStudent > 6:
            messagebox.showerror("Error", "Number of students must be between 1 and 6")
            return
    except ValueError:
        messagebox.showerror("Error", "Number of students must be an integer")
        return

    for i in range(numStudent):
        '''Generate score box(es) equal to the number of student'''
        tk.Label(score_frame, text=f"Student {i+1} Score").grid(row=i, column=0)
        entry = tk.Entry(score_frame)
        entry.grid(row=i, column=1)
        scores_entry.append(entry)

root = tk.Tk()
root.title("Score Calculator")

num_students_label = tk.Label(root, text="Number of Students")
num_students_label.grid(row=0, column=0)
num_students_entry = tk.Entry(root)
num_students_entry.grid(row=0, column=1)

score_button = tk.Button(root, text="To add score", command=score_entry)
score_button.grid(row=2, column=0, columnspan=2)

score_frame = tk.Frame(root)
score_frame.grid(row=1, column=0, columnspan=2)

cal_button = tk.Button(root, text="Calculate Average", command=cal_avg)
cal_button.grid(row=3, column=0, columnspan=2)

result_text = tk.Text(root)
result_text.grid(row=4, column=0, columnspan=2)

root.mainloop()