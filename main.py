from tkinter import *
from tkinter import messagebox
import random



# ===============================password generator=================================================

Alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
           ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SYMBOLS=["!","@","$","%","^","&","#","*"]
NUMBERS=[0,1,2,3,4,5,6,7,8,9]
letters_need=4
symbols_need=3
numbers_need=5

def password_generator():
    passwrd_list=[]
    for a in range(0,letters_need):
        pswd=random.randint(0,len(Alphabets)-1)
        ltrs=Alphabets[a]
        passwrd_list.append(ltrs)
        
    for b in range(0,symbols_need):
        sn=random.randint(0,len(SYMBOLS)-1)
        symbls=SYMBOLS[sn]
        passwrd_list.append(str(symbls))
        
    for c in range(0,numbers_need):
        nu=random.randint(0,len(NUMBERS)-1)
        num=NUMBERS[nu]
        passwrd_list.append(str(num))

    random.shuffle(passwrd_list)
    genarated_password="".join(passwrd_list)
    print(genarated_password)
    password_entry.insert(0,genarated_password)
    


# ===========================================UI===============================

tkwindow=Tk()
tkwindow.title("Password Manager")
tkwindow.config(padx=50,pady=50)

canvas=Canvas(width=400,height=300)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(200,150,image=logo_img)
canvas.grid(row=0,column=1)
# all labels names
wedsite_label=Label(text="website :")
wedsite_label.grid(row=1,column=0)
email_label=Label(text="Email/Username :")
email_label.grid(row=2,column=0)
password_label=Label(text="Password :")
password_label.grid(row=3,column=0)

    
# ======================placeholders for filling data=======================
website_entry=Entry(width=45)
website_entry.grid(row=1,column=1)
email_entry=Entry(width=45)
email_entry.insert(0, 'rohini123@gmail.com')
email_entry.grid(row=2,column=1)
password_entry=Entry(width=35)
password_entry.grid(row=3,column=1) 

# is_dataentered()


def entered_values():
    website_data=website_entry.get()   
    email_data=email_entry.get()   
    password_data=password_entry.get() 
     
    if len(website_data)==0 or len(email_data)==0 or len(password_data) == 0:
        print(len(website_data),len(email_data),len(password_data))
        messagebox.showinfo(title="Warning",message="please fill all fields")
    else:    
        with open("data.txt","a") as file:
            file.write(f"||{website_data}|{email_data}|{password_data}||\n")
            messagebox.showinfo(title="Title",message="your info is saved")
            website_entry.delete(0,'end')
            password_entry.delete(0,'end')



# Buttons=================================events=====================
generate_password_button=Button(text="Generate password",bg="pink",command=password_generator)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",command=entered_values)
add_button.grid(row=4,column=1)

    
       





tkwindow.mainloop()