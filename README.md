Simon Amable
101267294
Asignment 3, part 1,  COMP3005


Compilation instuctions:

run step by step in the terminal after cloning the repository:
- pip install psycopg2
- python ./simpleSQL.py


Gereral instruction:
once running the program Follow the text promts in the terminal to test all features


getAllStudents():
 - returns all students records in the DB
 - executes a SELECT querry, then returns and prints results

addStudent(first_name, last_name, email, enrollment_date): 
 - add a student to the db based on the provided parameters
 - executes a INSERT statment with the supplied values

updateStudentEmail(student_id, new_email):
 - add a student to the db based on the provided parameters
 - executes a UPDATE statment with the supplied values,

deleteStudent(student_id)
 - delete a student based off of id
 - executes a UPDATE statment with the supplied values,
