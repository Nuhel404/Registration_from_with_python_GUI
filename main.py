from tkinter import *
from tkinter import ttk
from pil import Image, ImageTk

class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1420x710+0+0")
        self.root.title("Face Recognition System")
        
        #first Image
        img = Image.open(r"C:\Users\zakir\OneDrive\Desktop\Making Attendance With Face Detection\college_images\f1.jpg")
        img = img.resize((430, 110), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=430, height=110)
        #Second Image
        img1 = Image.open(r"C:\Users\zakir\OneDrive\Desktop\Making Attendance With Face Detection\college_images\f2.png")
        img1 = img1.resize((430, 110), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=430, y=0, width=430, height=110)
        #Third Image
        img2 = Image.open(r"C:\Users\zakir\OneDrive\Desktop\Making Attendance With Face Detection\college_images\f3.jpg")
        img2 = img2.resize((430, 110), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=860, y=0, width=430, height=110)
        
        #bg Image
        img3 = Image.open(r"C:\Users\zakir\OneDrive\Desktop\Making Attendance With Face Detection\college_images\f4.jpg")
        img3 = img3.resize((1420, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=110, width=1420, height=710)

        lbl_title = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 25, "bold"), bg="white", fg="red")
        lbl_title.place(x=0, y=0, width=1420, height=45)

        #button
        img4 = Image.open(r"college_images\g8.jpg")
        img4 = img4.resize((180, 180), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4, cursor = "hand2")
        b1.place(x=160, y=60, width=180, height=180)

        b1_1 = Button(bg_img, text="Student Details",  cursor = "hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=170, y=240, width=165, height=40)

        #face detector
        img5 = Image.open(r"college_images\g10.jpg")
        img5 = img5.resize((180, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg5, cursor = "hand2")
        b1.place(x=460, y=60, width=180, height=180)

        b1_2 = Button(bg_img, text="Face Detector", cursor = "hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_2.place(x=460, y=240, width=180, height=40)

        #Attendance face detector
        img6 = Image.open(r"college_images\g11.jpg")
        img6 = img6.resize((180, 180), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg6, cursor = "hand2")
        b1.place(x=760, y=60, width=180, height=180)

        b1_3 = Button(bg_img, text="Attendance", cursor = "hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_3.place(x=760, y=240, width=180, height=40)

        #help
        img7 = Image.open(r"college_images\g12.jpg")
        img7 = img7.resize((180, 180), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, cursor = "hand2")
        b1.place(x=1060, y=60, width=180, height=180)

        b1_3 = Button(bg_img, text="Help", cursor = "hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_3.place(x=1060, y=240, width=180, height=40)

        #Train Face Button
        img8 = Image.open(r"college_images\13.jpeg")
        img8 = img8.resize((165, 165), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimg8, cursor = "hand2")
        b1.place(x=160, y=300, width=165, height=165)

        b1_4 = Button(bg_img, text="Train Face", cursor = "hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_4.place(x=160, y=465, width=165, height=40)

        #photos face button
        img9 = Image.open(r"college_images\g14.jpg")
        img9 = img9.resize((165, 165), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9, cursor = "hand2")
        b1.place(x=450, y=300, width=165, height=165)

        b1_4 = Button(bg_img, text="Photos", cursor = "hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_4.place(x=450, y=465, width=165, height=40)

        # Developer button
        img10 = Image.open(r"college_images\g15.jpg")
        img10 = img10.resize((165, 165), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimg10, cursor = "hand2")
        b1.place(x=740, y=300, width=165, height=165)

        b1_4 = Button(bg_img, text="Developer", cursor = "hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_4.place(x=740, y=465, width=165, height=40)

        #Exit face button
        img11 = Image.open(r"college_images\g16.png")
        img11 = img11.resize((165, 165), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img, image=self.photoimg11, cursor = "hand2")
        b1.place(x=1040, y=300, width=165, height=165)

        b1_4 = Button(bg_img, text="Exit", cursor = "hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_4.place(x=1040, y=465, width=165, height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()