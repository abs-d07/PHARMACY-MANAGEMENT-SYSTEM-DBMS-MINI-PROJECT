import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pms"
)

c = mydb.cursor()

def create_table():
    c.execute('CREATE TABLE  IF NOT EXISTS Customer(C_Name VARCHAR(15) NOT NULL,C_ID VARCHAR(20) NOT NULL,C_Phone_no VARCHAR(12) NOT NULL,C_Gender VARCHAR(6) NOT NULL,PRIMARY KEY (C_ID))')


def add_data(C_Name, C_ID, C_Phone_no, C_gender):
    c.execute('INSERT INTO CUSTOMER(C_Name, C_ID, C_Phone_no, C_gender) VALUES (%s,%s,%s,%s)',
              (C_Name, C_ID, C_Phone_no, C_gender))
    mydb.commit()

def add_data_bog(C_ID,Dr_ID,I_No,Quantity):
    c.execute('INSERT INTO buys_or_generates(C_ID,Dr_ID,I_No,Quantity) VALUES (%s,%s,%s,%s)',
            (C_ID,Dr_ID,I_No,Quantity))
    mydb.commit()
def add_data_inv(I_Date,I_Time,I_No):
    
    #c.execute('INSERT INTO buys_or_generates(C_ID,Dr_ID,I_No,Quantity) VALUES (%s,%s,%s,%s)',
    #        (C_ID,Dr_ID,I_No,Quantity))
    c.execute('INSERT INTO INVOICE(I_Date,I_Time,I_No) VALUES (%s,%s,%s)',
            (I_Date,I_Time,I_No))
    mydb.commit()
def add_data_bog(C_ID,Dr_ID,I_No,Quantity):
    
    #c.execute('INSERT INTO buys_or_generates(C_ID,Dr_ID,I_No,Quantity) VALUES (%s,%s,%s,%s)',
    #        (C_ID,Dr_ID,I_No,Quantity))
    c.execute('INSERT INTO buys_or_generates(C_ID,Dr_ID,I_No,Quantity) VALUES (%s,%s,%s,%s)',
            (C_ID,Dr_ID,I_No,Quantity))
    '''UPDATE employees 
SET 
    email = 'mary.patterson@classicmodelcars.com'
WHERE
    employeeNumber = 1056;
    
    '''
    c.execute('UPDATE drug SET Dr_Quantity = Dr_Quantity-%(qty)s',{'qty':Quantity})
    mrp = c.execute('SELECT Dr_MRP FROM DRUG WHERE Dr_ID=%(drid)s',{'drid':Dr_ID})
    print('asjfdkljdsfkjdskjfkljdfkljfdkls')
    quant = c.execute('SELECT Quantity FROM buys_or_generates WHERE Dr_ID=%(dri_d)s AND C_ID=%(c_id)s',{'dri_d':Dr_ID},{'c_id':C_ID})
    print(quant)
    price = mrp*quant
    c.execute('UPDATE INVOICE SET I_Bill_Amount = %(pri)s WHERE I_No=%(i_no)s',{'pri':price},{'i_no':I_No})
    mydb.commit()

def view_all_data():
    c.execute('SELECT * FROM Customer')
    data = c.fetchall()
    return data


def view_only_customer_names():
    c.execute('SELECT C_Name FROM Customer')
    data = c.fetchall()
    return data


def get_customer(C_Name):
    c.execute('SELECT * FROM Customer WHERE C_Name="{}"'.format(C_Name))
    data = c.fetchall()
    return data


def edit_Customer_data(new_C_Name, new_C_ID, new_C_Phone_no, new_C_gender,C_Name, C_ID, C_Phone_no, C_Gender):
    c.execute("UPDATE Customer SET C_Name=%s, C_ID=%s, C_Phone_no=%s, C_Gender=%s WHERE "
              "C_Name=%s and C_id=%s and C_Phone_no=%s and C_Gender=%s", (new_C_Name, new_C_ID, new_C_Phone_no, new_C_gender,C_Name, C_ID, C_Phone_no, C_Gender))
    mydb.commit()
#    data = c.fetchall()
    return view_all_data


def delete_data(C_Name):
    c.execute('DELETE FROM Customer WHERE C_Name="{}"'.format(C_Name))
    mydb.commit()


