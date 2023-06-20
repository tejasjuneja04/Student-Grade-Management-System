#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to load student data from CSV file
def load_student_data():
    students = []
    try:
        with open('students.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        pass
    return students

# saving data to csv file
def save_student_data(students):
    with open('students.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

# add student button
def add_student():
    name = entry_name.get()
    grade = float(entry_grade.get())
    if name and grade:
        student = {"Name": name, "Grade": grade}
        students.append(student)
        save_student_data(students)
        messagebox.showinfo("Success", "Student added successfully.")
        entry_name.delete(0, tk.END)
        entry_grade.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter both name and grade.")

# calculating the average value
def calculate_average_grade():
    if students:
        total_grades = sum(float(student["Grade"]) for student in students)
        average_grade = total_grades / len(students)
        messagebox.showinfo("Average Grade", f"The average grade is: {average_grade:.2f}")
    else:
        messagebox.showinfo("Average Grade", "No students added yet.")

# deleting the student from the list
def delete_student():
    name = entry_name.get()
    deleted = False
    for student in students:
        if student["Name"] == name:
            students.remove(student)
            deleted = True
            break
    if deleted:
        save_student_data(students)
        messagebox.showinfo("Success", f"Student '{name}' deleted successfully.")
        entry_name.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", f"No student found with the name '{name}'.")

# searching student by the name 
def search_student():
    name = entry_name.get()
    found_students = [student for student in students if student["Name"].lower() == name.lower()]
    if found_students:
        result = "\n".join(f"Name: {student['Name']}, Grade: {student['Grade']}" for student in found_students)
        messagebox.showinfo("Search Results", f"Found {len(found_students)} student(s) with the name '{name}':\n\n{result}")
    else:
        messagebox.showinfo("Search Results", f"No student found with the name '{name}'.")

# display all the students in a list
def show_students():
    if students:
        result = "\n".join(f"Name: {student['Name']}, Grade: {student['Grade']}" for student in students)
        messagebox.showinfo("Student List", f"List of students:\n\n{result}")
    else:
        messagebox.showinfo("Student List", "No students added yet.")

# Create the main application window
window = tk.Tk()
window.title("Student Grade Management System")

# Create and configure the student details inputs
style = ttk.Style()
style.configure('TEntry', padding=5, width=20)

label_name = ttk.Label(window, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = ttk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_grade = ttk.Label(window, text="Grade:")
label_grade.grid(row=1, column=0, padx=10, pady=10)
entry_grade = ttk.Entry(window)
entry_grade.grid(row=1, column=1, padx=10, pady=10)

# Create and configure the action buttons
button_add = ttk.Button(window, text="Add Student", command=add_student)
button_add.grid(row=2, column=0, padx=10, pady=10)

button_average = ttk.Button(window, text="Calculate Average Grade", command=calculate_average_grade)
button_average.grid(row=2, column=1, padx=10, pady=10)

button_delete = ttk.Button(window, text="Delete Student", command=delete_student)
button_delete.grid(row=3, column=0, padx=10, pady=10)

button_search = ttk.Button(window, text="Search Student", command=search_student)
button_search.grid(row=3, column=1, padx=10, pady=10)

button_show = ttk.Button(window, text="Show Students", command=show_students)
button_show.grid(row=4, column=0, padx=10, pady=10)

# Data storage
students = load_student_data()

# Start the main event loop
window.mainloop()



# In[ ]:





# In[ ]:




