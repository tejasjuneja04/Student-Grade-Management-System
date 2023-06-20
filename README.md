# Student-Grade-Management-System
This documentation gives an overview of the Student Grade Management System code, describing the main components and functionalities that have been created. The code is built in Python and makes use of the tkinter package to create the user interface and a CSV file to store the data.
## Table of Contents:
	User Interface
	Data Storage
	Functionality
	Error Handling

### 1.	User Interface
The Student Grade Management System's user interface is a graphical window designed with the tkinter package. It contains the following components:
Labels: Labels display text such as "Name" and "Grade" to provide instructions or to indicate the purpose of input fields.
Entry fields allow the user to enter information such as the student's name and grade. These fields are used to add, search for, and remove students.
Buttons: When a button is clicked, it performs a certain action. The system provides buttons for adding students, calculating average grades, deleting students, searching for students, and viewing the entire student list. 
The user interface allows users to engage with the system and conduct various activities on student data in a straightforward and intuitive manner.
### 2.	Data Storage
The Student Grade Management System stores data in a CSV (Comma-Separated Values) format. The information is kept in an organised style, with each row representing a student record and including the student's name and grade.
The load_student_data() function reads student data from a CSV file and produces a collection of dictionaries, one for each student record. The save_student_data() function saves student data to a CSV file, updating or generating it as needed. The system enables for persistent storage of student information by using a CSV file for data storage, allowing for data access and editing across numerous sessions.

### 3.	Functionality
The Student Grade Management System has a number of features for handling student data. These routines and event handlers are used to implement these features:
Adding a Student: When the "Add Student" button is pressed, the add_student() method is called. It reads the student's name and grade from the input fields, validates the input, constructs a dictionary representing the student record, adds the student to the list of students, and saves the revised data to the CSV file.

Average Grade Calculation: The calculate_average_grade() function computes the average grade of all students. It adds up all of the students' grades and divides the amount by the number of pupils. The outcome is shown in a message box.
Delete a Student: The delete_student() function removes a student from the list based on the name specified in the input. It removes the matching student record from the list and makes the necessary changes to the CSV file.
Finding a Student: The search_student() function looks up a student by name. It reads the name from the input field, searches the list of students case-insensitively, and presents the results in a message box.
Displaying the Entire Student List: The show_students() function displays the entire student list in a message box. It extracts and formats all of the student records from the list for presentation.
These features enable users to add, delete, search for, and see student data, resulting in a comprehensive system for managing student grades.

### 4. Error Handling
To address probable complications during data manipulation and user interactions, the Student Grade Management System includes error handling. There are the following error handling systems in place:
When adding a student, the system checks to see if the name and grade input fields are empty. If either is empty, an error notice is presented, requesting the user to enter the necessary information.
File Not Found: If the file is not found when attempting to load student data from the CSV file, the system gently handles the exception and continues without loading any prior data. This enables the creation of a new CSV file if one does not already exist.
If the user's input name does not match any student data, a warning message is presented informing them that no student with the given name was located.
These error management features improve the user experience by displaying helpful notifications and preventing unexpected crashes or undesirable behaviour.

## Conclusion
The Student Grade Management System is a Python application that allows users to manage student grades easily. It makes use of a tkinter-created user interface, a CSV file for data storage, and different features for adding, removing, searching, and displaying student records. The system has error handling capabilities to address any errors and give users with helpful feedback.
The application uses the tkinter library to create a user-friendly interface with labels, entry fields, and buttons for easy interaction. Users can enter student information such as name and grade and then conduct operations such as adding a student, calculating the average grade, deleting a student, searching for a student by name, and viewing the entire list of students.By using a CSV file as the data storage medium, the system ensures data permanence. The load_student_data() function reads student data from a CSV file and writes it back to the file, allowing for seamless data retrieval and editing over several sessions.
The Student Grade Management System's functionality is critical. Users can add new students by entering their name and grade, with input validation preventing empty fields from being entered. The system computes the average grade for each student, allowing users to evaluate overall performance. Students can be erased based on their names, and the system has search features to help you find students by name. Furthermore, the system includes a feature that displays the entire list of pupils, providing a comprehensive view.The programme features error handling methods to offer a stable and user-friendly experience. It checks input fields and displays relevant error messages when required information is lacking. The system gently handles file not found problems and alerts users when no matching student is discovered during deletion or search activities.

In summary, the Student Grade Management System demonstrates the successful use of Python programming principles such as data types, conditional expressions, looping statements, user-defined functions, and external libraries. It has a simple and intuitive user interface, strong data storage, basic functions, and error management, making it a useful tool for maintaining student grades.
