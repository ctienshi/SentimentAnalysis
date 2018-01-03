from datetime import date, datetime, timedelta
from extractImportant import get_mail_threads
import mysql.connector

cnx = mysql.connector.connect(user='root',password='houses123',host='127.0.0.1', database='testing')
cursor = cnx.cursor()
tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO emails "
                "(threadid, sub, vpositive, positive, neutral,negative,vnegative) "
                "VALUES (%s, %s, %s, %s, %s,%s,%s)")

data_employee = ('Geert', 'Vanderkelen', 5,4,3,3,2)

# Insert new employee
cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

# Insert salary information
data_salary = {
    'emp_no': emp_no,
    'salary': 50000,
    'from_date': tomorrow,
    'to_date': date(9999, 1, 1),
}
#cursor.execute(add_salary, data_salary)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()