import psycopg2


# connect to the postgres DB
conn = psycopg2.connect(database="A3",
                        host="localhost",
                        user="postgres",
                        password="simon",
                        port="5432")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
def getAllStudents():
    # create SQL statement

    cur.execute("SELECT * FROM students")
    return cur.fetchall()
    #get alls tudent records from db

def addStudent(f_name,l_name,email, enrollment_date):
    # create SQL statement
    query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
    # Execute query with parameters
    cur.execute(query, (f_name, l_name, email, enrollment_date))
    # Commit the transaction
    print (f"{f_name},{l_name},{email},{enrollment_date}")
    conn.commit()

def updateStudentEmail(s_id,new_email):
        # create SQL statement
    query = f"UPDATE students SET email=%s WHERE student_id=%s"
    # Execute query with parameters
    cur.execute(query,(new_email,s_id))
    # Commit the transaction
    conn.commit()

    print (f"updateStudentEmail: id={s_id}, new_email={new_email}")

def deleteStudent(s_id):
    # create SQL statement
    query = f"DELETE FROM students WHERE student_id=%s"
    # Execute query with parameters
    cur.execute(query,(s_id,))
    # Commit the transaction
    conn.commit()

    print (f"deleted Student: id={s_id}")



# # Retrieve query results
# #records = cur.fetchall()
    
# #updateStudentEmail(4,"adik@gmail.com")
# deleteStudent(4)

# print("getAllStudents: ")
# print(getAllStudents())

# # print("addStudent: ")
# # addStudent("simon","amable","s@gmail.com","06/06/2022")
# #updateStudentEmail(4,"adik@gmail.com")



#main runs a simple conditional loop for user testing.
def main():
    print("Please choose an option(0-4) from the menu provided , and then follow the promts")


    choice = int (input ("""1. GetAllStudents()
2. addStudent()
3. updateStudentEmail()
4. deleteStudent()
0. Quit ()
          """))
    while (choice > 0 ):
        if (choice == 1):
            print (getAllStudents())
        elif (choice == 2):
            f_name=input ("Enter the first name:")
            l_name=input ("Enter the last name:")
            email=input ("Enter the email:")
            er_date=input ("Enter the enrollment date (form : mm/dd/yy):")
            addStudent(f_name,l_name,email,er_date)
        elif (choice == 3):
            s_id=input ("Enter the students id:")
            email=input ("Enter the new email:")
            updateStudentEmail(s_id,email)
        elif choice == 4:
            deleteStudent(s_id)
        elif choice == 0 :
            break
        choice = int(input ("Please make another selection!"))
            



if __name__  == "__main__":
    main()