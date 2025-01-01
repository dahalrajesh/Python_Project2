from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Handle Login Function
def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'rajesh@gmail.com' and password == 'rajesh@12':
        messagebox.showinfo(
            'Login Successful',
            'Welcome to KIIT Portal!\n\nHere you can access:\n- Online Classes\n- Results\n- Course Materials'
        )
    else:
        messagebox.showerror('ERROR', 'Login Failed')

# Handle Forgot Password
def forgot_password():
    messagebox.showinfo(
        "Forgot Password",
        "Please contact admin@kiit.ac.in to reset your password."
    )

# Main Root Window
root = Tk()
root.title('Login Form')

# Configure the window
root.geometry('400x550')
root.configure(background='#1a1a2e')
try:
    root.iconbitmap("kiit.ico")
except Exception as e:
    print(f"Icon not found: {e}")

# Header Image
try:
    img = Image.open('kiit.png')
    resized_img = img.resize((120, 120))
    img = ImageTk.PhotoImage(resized_img)
    img_label = Label(root, image=img, bg='#1a1a2e')
    img_label.pack(pady=(20, 10))
except Exception as e:
    print(f"Image not found: {e}")

# Title Label
title_label = Label(root, text='KIIT Portal', fg="white", bg='#1a1a2e', font=('Verdana', 26, 'bold'))
title_label.pack(pady=(5, 20))

# Email Input Field
email_label = Label(root, text="Enter Email:", fg='white', bg='#1a1a2e', font=('Verdana', 12))
email_label.pack(pady=(5, 5))
email_input = Entry(root, width=30, font=('Verdana', 12))
email_input.pack(ipady=8, pady=(1, 15))

# Password Input Field
password_label = Label(root, text="Enter Password:", fg='white', bg='#1a1a2e', font=('Verdana', 12))
password_label.pack(pady=(5, 5))
password_input = Entry(root, width=30, show="*", font=('Verdana', 12))
password_input.pack(ipady=8, pady=(1, 15))

# Login Button with Hover Effect
def on_enter(e):
    login_btn['bg'] = '#ffa500'

def on_leave(e):
    login_btn['bg'] = '#e94560'

login_btn = Button(root, text="Login", fg='white', bg='#e94560', width=20, height=2, command=handle_login, font=('Verdana', 12))
login_btn.pack(pady=(20, 10))
login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

# Forgot Password Link
forgot_password_label = Label(root, text="Forgot Password?", fg="#00a8cc", bg="#1a1a2e", font=('Verdana', 10, 'underline'), cursor="hand2")
forgot_password_label.pack(pady=(10, 5))
forgot_password_label.bind("<Button-1>", lambda e: forgot_password())

# Footer Label
footer_label = Label(root, text="© 2024 KIIT Portal", fg="gray", bg='#1a1a2e', font=('Verdana', 8))
footer_label.pack(side=BOTTOM, pady=(10, 0))

# Run the Main Loop
root.mainloop()
