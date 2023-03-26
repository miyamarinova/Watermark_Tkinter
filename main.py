from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile
from upload_image import Upload_img

BACKGROUND_COLOR = '#4D4D4D'


class Screen:
    def __init__(self):
        self.window = Tk()
        self.front_screen()
        self.window.mainloop()

    def front_screen(self):
        self.window.title("Watermark")
        self.window.geometry("800x600")
        self.window.resizable(False, False)
        self.window.config(background=BACKGROUND_COLOR)
        title_label_0 = Label(text="MI|YA", bg=BACKGROUND_COLOR, font=('Arial', 15, "bold"), fg="white")
        title_label_01 = Label(text="Simplicity is beauty, functionality is strength", bg=BACKGROUND_COLOR,
                               font=('Arial', 10), fg="white")
        title_label_1 = Label(text="Make", bg=BACKGROUND_COLOR, font=('Arial',50,"bold"),fg="white")
        title_label_2 = Label(text="Your Watermark", bg=BACKGROUND_COLOR, font=('Arial', 50, "bold"), fg="white")
        title_label_0.place(x=10,y=10)
        title_label_01.place(x=10, y=30)
        title_label_1.place(x=70,y=100)
        title_label_2.place(x=70, y=150)

        screen_button = Button(text="Upload image", bg='#BFDB38', fg=BACKGROUND_COLOR, font=('Arial',40,"bold"),command=self.upload_img)
        screen_button.place(x=70, y=250)

    def upload_img(self):
        self.window.destroy()
        Upload_img()




Screen()