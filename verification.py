
import sqlite3

def login_verify(username,aadhar,password):
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('SELECT ID,Username,Password,aadhar_number FROM Customer')
    records = cursor.fetchall()
    id = 0
    
    
    check =0
    for row in records:
        if((username == row[1] or aadhar == row[3])and password == row[2]):
            id = row[0]
            check = 1
            break
    
    return id,check

    

