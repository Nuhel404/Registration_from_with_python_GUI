from tkinter import *
from tkinter import ttk
from pil import Image, ImageTk
from tkinter import messagebox

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\zakir\OneDrive\Desktop\github\Login_form\pa.jpg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth = 1, relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\zakir\OneDrive\Desktop\github\Login_form\R3.jpg")
        left_bg=Label(self.root, image=self.bg1)
        left_bg.place(x=50, y=60, width = 430, height=550)
        #Main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=480, y=60, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        #label and entry
        #row1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        #row2
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        #row3
        security_Q = Label(frame, text="Select security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"]=("select", "Your Birth Place", "Your Best Friend name", " Your Mother's Birthplace")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)
        
        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"))
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        #row 4
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"))
        password.place(x=50, y=310)
        self.txt_password = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_password.place(x=50, y=340, width=250)

        confirm_paswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"))
        confirm_paswd.place(x=370, y=310)
        self.txt_confirm_paswd = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_confirm_paswd.place(x=370, y=340, width=250)

        #Check Button
        chkbtn = Checkbutton(frame, text="I Agree The Terms & Conditions", font=("times new roman", 10, "bold"))
        chkbtn.place(x=50, y=380)

        #Buttons
        img = Image.open(r"C:\Users\zakir\OneDrive\Desktop\github\Login_form\R6.png") 
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"C:\Users\zakir\OneDrive\Desktop\github\Login_form\R7.png") 
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b2.place(x=330, y=420, width=200)


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
