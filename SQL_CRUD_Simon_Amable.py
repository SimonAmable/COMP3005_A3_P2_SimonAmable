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
def getAllStudents() -> str:   #select all students and return data
    # create SQL statement

    cur.execute("SELECT * FROM students")
    return cur.fetchall()
    #get alls tudent records from db

def addStudent(f_name,l_name,email, enrollment_date):   #add student 
    # create SQL statement
    query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
    # Execute query with parameters
    cur.execute(query, (f_name, l_name, email, enrollment_date))
    # Commit the transaction
    print (f"{f_name},{l_name},{email},{enrollment_date}")
    conn.commit()

def updateStudentEmail(s_id,new_email): #Update email by student_id
    # create SQL statement
    query = f"UPDATE students SET email=%s WHERE student_id=%s"
    # Execute query with parameters
    cur.execute(query,(new_email,s_id))
    # Commit the transaction
    conn.commit()

    print (f"updateStudentEmail: id={s_id}, new_email={new_email}")


def deleteStudent(s_id):    #this is a DELETE by student_id
    # create SQL statement
    query = f"DELETE FROM students WHERE student_id=%s"
    # Execute query with parameters
    cur.execute(query,(s_id,))
    # Commit the transaction
    conn.commit()

    print (f"deleted Student: id={s_id}")



def format_data(data):
    headers = ["ID", "first_name", "last_name", "Email", "enrollement_date"]
    formatted_data = [headers]
    for item in data:
        formatted_item = [str(item[0]), item[1], item[2], item[3], item[4].strftime("%Y-%m-%d")]
        formatted_data.append(formatted_item)
    
    # Find maximum width for each column
    column_widths = [max(len(row[i]) for row in formatted_data) for i in range(len(headers))]
    
    # Format each row
    formatted_table = ''
    for row in formatted_data:
        formatted_row = ''
        for i, cell in enumerate(row):
            formatted_row += cell.ljust(column_widths[i] + 2)  # Add 2 for padding
        formatted_table += formatted_row.strip() + '\n'

    return formatted_table

#main runs a simple conditional loop for user testing.
def main():


    choice = 1 #filler value / choice name declaration
    while (choice > 0 ):
        print("Please choose an option(0-4) from the menu provided , and then follow the promts")


        choice_str = input ("""1. GetAllStudents()
2. addStudent()
3. updateStudentEmail()
4. deleteStudent()
0. Quit ()
            """)
        try:
            choice=int(choice_str)
        except:
            print("you seem to have entered something incorrectly please try again!")
            continue

        if (choice == 1):
            print (format_data(getAllStudents()))
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
            s_id=input ("Enter the students id:")
            deleteStudent(s_id)
        elif choice == 0 :
            break
        else:
            print("you seem to have entered something incorrectly please try again")
        #choice = int(input ("Please make another selection!"))
            



if __name__  == "__main__":
    main()