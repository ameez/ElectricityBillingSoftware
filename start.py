from tkinter import *
from database import *
from verification import *
from fetch_data import *
from calculation import *
from functools import partial


#pylint: disable-msg=R0913

#pylint: disable-msg=R0913









def register_user():
    c = 0
    username_info = username.get()
    password_info = password.get()
    address_info = address.get()
    aadhar_info = aadhar.get()
    radiobutton_info = var.get()
    print(radiobutton_info)

    if( len(username_info)>0  and len(password_info)>0 and len(address_info)>0  and len(aadhar_info)>0  and radiobutton_info !=0):

        if(len(password_info)<8):
            invalid_password_register()
        else:
            c = 1
        

        if(len(str(aadhar_info))!=12):
            invalid_aadhar_register()
        else:
            c = 1

        if(c == 1):
            
            writeOnDatabase(username_info,password_info,aadhar_info,address_info,radiobutton_info)
            #print("registeration success")
            register_success()

    else:
        enter_all_details()
        

def enter_all_details():
    global enter_all_details_screen
    enter_all_details_screen = Toplevel(register_screen)
    enter_all_details_screen.title("Unscuccessful")
    enter_all_details_screen.geometry("300x100")
    Label(enter_all_details_screen,text = "Enter all fields.").pack()
    Button(enter_all_details_screen,text = "OK",command = delete_enter_all_details_screen).pack()

def delete_enter_all_details_screen():
    enter_all_details_screen.destroy()



def register_success():
    global register_success_screen
    register_success_screen = Toplevel(register_screen)
    register_success_screen.title("Success!!!")
    register_success_screen.geometry("300x100")
    Label(register_success_screen,text = "Registration successful,You can login NOW!").pack()
    Button(register_success_screen,text = "OK",command = delete_register_success_screen).pack()


def delete_register_success_screen():
    register_success_screen.destroy()
    register_screen.destroy()





    

def invalid_aadhar_register():
    global invalid_aadhar_screen
    invalid_aadhar_screen = Toplevel(register_screen)
    invalid_aadhar_screen.title("Unscuccessful")
    invalid_aadhar_screen.geometry("300x100")
    Label(invalid_aadhar_screen,text = "Enter valid UID").pack()
    Button(invalid_aadhar_screen,text = "OK",command = delete_invalid_aadhar_register).pack()

def delete_invalid_aadhar_register():
    invalid_aadhar_screen.destroy()


        
       

def invalid_password_register():
    global invalid_password_screen
    invalid_password_screen = Toplevel(register_screen)
    invalid_password_screen.title("Unsuccessful")
    invalid_password_screen.geometry("300x100")
    Label(invalid_password_screen,text = "Minimum 8 character password").pack()
    Button(invalid_password_screen,text = "OK",command = delete_invalid_password_register).pack()


def delete_invalid_password_register():
    invalid_password_screen.destroy()

    



def register():
    global register_screen
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("500x500")
 
# Set text variables
    global username
    username = StringVar()
    global password 
    password = StringVar()
    global address 
    address = StringVar()
    global aadhar 
    aadhar = StringVar()

 
# Set label for user's instruction
    Label(register_screen, text="Please enter details below", bg="#fcb603").pack()
    Label(register_screen, text="").pack()
    
# Set username label
    username_lable = Label(register_screen, text="Username ")
    username_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
   
# Set password label
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
# Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()


#  set address label
    address_lable = Label(register_screen,text = "Billing Address")
    address_lable.pack()


#set address entry
    address_entry = Entry(register_screen,textvariable=address)
    address_entry.pack()


#set Aadhar label
    aadhar_lable = Label(register_screen,text = "Aadhar Number")
    aadhar_lable.pack()

#set Aadhar entry
    aadhar_entry = Entry(register_screen,textvariable=aadhar)
    aadhar_entry.pack()


#set radio button and label
    set_radioButton()

    
    Label(register_screen, text="").pack()
    
    # Set register button
    Button(register_screen, text="Register", width=10, height=1, bg="#fcb603",command = register_user).pack()


def set_radioButton():
    global var
    var = IntVar()

    Label(register_screen,text = "Enter Payment mode").pack()

    R1 = Radiobutton(register_screen, text="Prepaid", variable=var, value=1)
    R1.pack()
    R2 = Radiobutton(register_screen, text="Postpaid", variable=var, value=2)
    R2.pack()

active_account_status = 0


def login_verification():
    
    username = username_verify.get()
    password = password_verify.get()
    aadhar_number = aadhar_verify.get()
    global active_account_status
    
    if(active_account_status == 0):

        if((len(username)>0 or len(aadhar_number)>0) and len(password)>0): 
            ID,check = login_verify(username,aadhar_number,password)

            
            if(check == 1):
                active_account_status = 1
                login_successful()
                User_account_screen(ID)

            else:
                login_verify_failed()



        else:
            login_verify_failed()

    else:
        log_out_previous()
        
def log_out_previous():
    global prev_log_out_screen
    prev_log_out_screen = Toplevel(login_screen)
    prev_log_out_screen.title("INVALID")
    prev_log_out_screen.geometry("300x100")
    Label(prev_log_out_screen,text = "Log out of currently logged in account!").pack()
    Button(prev_log_out_screen,text = "OK",command = destroy_prev_log_out_screen).pack()

def destroy_prev_log_out_screen():
    prev_log_out_screen.destroy()


def login_successful():
    global login_successful_screen
    login_successful_screen = Toplevel(login_screen)
    login_successful_screen.title("Login successful")
    login_successful_screen.geometry("300x100")
    Label(login_successful_screen,text = "Login Successful!").pack()
    Button(login_successful_screen,text = "Proceed",command = destroy_login_successful_screen).pack()


def destroy_login_successful_screen():
    login_successful_screen.destroy()
    login_screen.destroy()



def User_account_screen(ID):
    
    record = []
    records = get_data(ID)
    #print(len(records[0]))
    for i in range(0,len(records[0])):
        record.append(records[0][i])

    
    global user_screen
    user_screen = Toplevel(main_screen)
    user_screen.title("User Account")
    user_screen.geometry("400x400")
    Label(user_screen,text = "Customer Details",bg="#fcb603", width="300", height="2", font=("Calibri", 13)).pack()
    #Label(user_screen,text = "").pack()

    Label(user_screen,text = "USERNAME:"+record[0],bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    Label(user_screen,text = "UNIQUE IDENTIFICATION NUMBER:"+record[1],bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    Label(user_screen,text = "CUSTOMER ADDRESS:"+record[2],bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    Label(user_screen,text = "PAYMENT MODE:"+record[3],bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    Label(user_screen,text = "UNITS USED:"+(str)(record[4]),bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    Label(user_screen,text = "MONTHS DUE:"+(str)(record[5]),bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    
    
    Button(user_screen,text="CALCULATE BILL",bg = "#91EAE3",height="2", width="300", command = partial(calculate_bill,ID)).pack()
    Button(user_screen,text="LOGOUT",bg = "#91EAE3",height="2", width="300", command =logout_dialog).pack()

 

def logout_dialog():
    print("Enter")
    global active_account_status
    active_account_status = 0
    user_screen.destroy()
    
    



def calculate_bill(ID):
    bill,fine  = bill_calculation(ID)
    write_bill(ID,bill,fine)
    global bill_screen
    bill_screen = Toplevel(user_screen)
    bill_screen.title("BILL")
    bill_screen.geometry("300x300")
    Label(bill_screen,text = "Bill Details",bg="#fcb603", width="300", height="2", font=("Calibri", 13)).pack()
    Label(bill_screen,text = "Total amount to be paid:"+(str)(bill),bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    Label(bill_screen,text = "Fine included in total amount:"+(str)(fine),bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    
    Button(bill_screen,text="PAY:"+(str)(bill),bg = "#91EAE3",height="2", width="300", command =partial(bill_payment,ID)).pack()
    Button(bill_screen,text="CLOSE",bg = "#91EAE3",height="2", width="300", command =close_bill_screen).pack()



    

    
def bill_payment(ID):
    bill = 0
    fine = 0
    
    
    write_bill(ID,bill,fine)
    set_unit(ID)
    global bill_payment_confirm_screen
    bill_payment_confirm_screen = Toplevel(bill_screen)
    bill_payment_confirm_screen.title("CONFIRM")
    bill_payment_confirm_screen.geometry("300x100")
    Label(bill_payment_confirm_screen,text = "Bill Successfully Paid!").pack()
    Button(bill_payment_confirm_screen,text = "OK",command = destroy_confirm_screen).pack()

def destroy_confirm_screen():
    bill_payment_confirm_screen.destroy()
    bill_screen.destroy()


def close_bill_screen():
    bill_screen.destroy()


    

    



    


def login_verify_failed():
    global login_verify_failed_screen
    login_verify_failed_screen = Toplevel(login_screen)
    login_verify_failed_screen.title(" Login Unscuccessful")
    login_verify_failed_screen.geometry("300x100")
    Label(login_verify_failed_screen,text = "Enter login details correctly!").pack()
    Button(login_verify_failed_screen,text = "OK",command = delete_login_verify_failed_screen).pack()

def delete_login_verify_failed_screen():
    login_verify_failed_screen.destroy()


# define login function
def login_screen():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="Enter Username or Aadhar number").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
    global aadhar_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
    aadhar_verify = StringVar()
 
   
    Label(login_screen, text="Username ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()

    Label(login_screen, text="Aadhar number ").pack()
    aadhar_login_entry = Entry(login_screen, textvariable=aadhar_verify)
    aadhar_login_entry.pack()



    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()

def admin_login_successful():
    global admin_login_successful_screen
    admin_login_successful_screen = Toplevel(admin_login_screen)
    admin_login_successful_screen.title("Admin Login successful")
    admin_login_successful_screen.geometry("300x100")
    Label(admin_login_successful_screen,text = "Login Successful!").pack()
    Button(admin_login_successful_screen,text = "Proceed",command = destroy_admin_login_successful_screen).pack()

def destroy_admin_login_successful_screen():
    admin_login_successful_screen.destroy()
    admin_login_screen.destroy()


def admin_login_verify_failed():
    global admin_login_verify_failed_screen
    admin_login_verify_failed_screen = Toplevel(admin_login_screen)
    admin_login_verify_failed_screen.title(" Login Unscuccessful")
    admin_login_verify_failed_screen.geometry("300x100")
    Label(admin_login_verify_failed_screen,text = "Enter login details correctly!").pack()
    Button(admin_login_verify_failed_screen,text = "OK",command = delete_admin_login_verify_failed_screen).pack()

def delete_admin_login_verify_failed_screen():
    admin_login_verify_failed_screen.destroy()



def admin_options():
    global admin_options_screen
    admin_options_screen = Toplevel(main_screen)
    admin_options_screen.title("Admin options")
    admin_options_screen.geometry("300x200")
    Label(admin_options_screen,text = "Choose from below").pack()
    Label(admin_options_screen,text = "").pack()
    Button(admin_options_screen,text = "Update customer details:",command = update_customer).pack()
    Label(admin_options_screen,text = "").pack()

    Button(admin_options_screen,height = "2",width = "10",text = "LOGOUT",command = admin_logout).pack()


def admin_logout():
    global active_account_status
    active_account_status = 0
    admin_options_screen.destroy()



def update_customer():
    global update_customer_screen
    global customer_ID 
    global customer_username 
    global customer_password 
    global customer_address 
    global customer_units 
    global customer_months 

    customer_ID = IntVar()
    customer_username = StringVar()
    customer_password = StringVar()
    customer_address = StringVar()
    customer_units = IntVar()
    customer_months = IntVar()


    update_customer_screen = Toplevel(admin_options_screen)
    update_customer_screen.title("UPDATE")
    update_customer_screen.geometry("300x350")
    Label(update_customer_screen,text = "Enter ID").pack()
    Entry(update_customer_screen,textvariable = customer_ID).pack()

    Label(update_customer_screen,text = "").pack()

    Label(update_customer_screen,text = "Enter customer username to be updated").pack()
    Entry(update_customer_screen,textvariable = customer_username).pack()


    Label(update_customer_screen,text = "Enter password to be updated").pack()
    Entry(update_customer_screen,textvariable = customer_password,show = "*").pack()

    Label(update_customer_screen,text = "Enter Address to be updated").pack()
    Entry(update_customer_screen,textvariable = customer_address).pack()

    Label(update_customer_screen,text = "Enter units to be updated").pack()
    Entry(update_customer_screen,textvariable = customer_units).pack()

    Label(update_customer_screen,text = "Enter monnths due").pack()
    Entry(update_customer_screen,textvariable = customer_months).pack()


    Button(update_customer_screen,text = "UPDATE" , height = "2", width = "10",command = update_customer_get).pack()
    Label(update_customer_screen,text = "").pack()

    Button(update_customer_screen,text = "CLOSE",height = "2",width = "10",command = destroy_update_customer_screen).pack()

def destroy_update_customer_screen():
    update_customer_screen.destroy()




def update_customer_get():
    print("enter")
    ID = customer_ID.get()
    username = customer_username.get()
    password = customer_password.get()
    address = customer_address.get()
    units = customer_units.get()
    months = customer_months.get()

    update_customer_admin(ID,username,password,address,units,months)
    global success_screen
    success_screen = Toplevel(update_customer_screen)
    success_screen.title("success")
    success_screen.geometry("300x100")
    Label(success_screen,text = "Updation Successful!").pack()
    Button(success_screen,text = "OK",command = destroy_success_screen).pack()

def destroy_success_screen():
    success_screen.destroy()


def admin_logout_previous():
    global admin_prev_log_out_screen
    admin_prev_log_out_screen = Toplevel(update_customer_screen)
    admin_prev_log_out_screen.title("INVALID")
    admin_prev_log_out_screen.geometry("300x100")
    Label(admin_prev_log_out_screen,text = "Log out of currently logged in account!").pack()
    Button(admin_prev_log_out_screen,text = "OK",command = destroy_admin_prev_log_out_screen).pack()

def destroy_admin_prev_log_out_screen():
    admin_prev_log_out_screen.destroy()





    





def admin_login_verification():
    username = admin_username_verify.get()
    password = admin_password_verify.get()
    global active_account_status
    
    if(active_account_status == 0):

        if(len(username)>0  and len(password)>0): 
            check = admin_login_verify(username,password)

            
            if(check == 1):
                active_account_status = 1
                admin_login_successful()
                admin_options()

            else:
                admin_login_verify_failed()



        else:
            admin_login_verify_failed()

    #else:
        #admin_log_out_previous()








def admin_login_screen():
    global admin_login_screen
    admin_login_screen = Toplevel(main_screen)
    admin_login_screen.title("Admin Login")
    admin_login_screen.geometry("300x300")
    Label(admin_login_screen, text="Please enter details below to login").pack()
    Label(admin_login_screen, text="").pack()
 
    global admin_username_verify
    global admin_password_verify
    
 
    admin_username_verify = StringVar()
    admin_password_verify = StringVar()
 
   
    Label(admin_login_screen, text="Username ").pack()
    username_login_entry = Entry(admin_login_screen, textvariable=admin_username_verify)
    username_login_entry.pack()

    
    Label(admin_login_screen, text="").pack()
    Label(admin_login_screen, text="Password * ").pack()
    password__login_entry = Entry(admin_login_screen, textvariable=admin_password_verify, show= '*')
    password__login_entry.pack()

    Label(admin_login_screen, text="").pack()
    Button(admin_login_screen, text="Login", width=10, height=1, command=admin_login_verification).pack()



    



def main_account_screen():
    global main_screen
 
# add command=register in button widget
 
    
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("main_screen")
 
    # create a Form label 
    Label(text="Vssut Electricity Billing system", bg="#fcb603", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
    
    # create Login Button 
    Button(text="Login", height="2", width="30", command = login_screen).pack()
    Label(text="").pack() 

    
   



    Button(text="Register", height="2", width="30", command=register).pack()
    Label(text = "").pack()
    Button(text = "Admin Login",height = "2",width = "30",command = admin_login_screen).pack()
    
    
    
    main_screen.mainloop()
 
main_account_screen()
