import random
from tkinter import *
from tkinter import filedialog
from tkinter import ttk,messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageDraw, ImageFont

BACKGROUND_COLOR = '#4D4D4D'
global img
class Upload_img:
    def __init__(self):
        self.upload_window = Tk()
        self.f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png'),("all files","*.*")]
        self.filename = filedialog.askopenfilename(filetypes=self.f_types)
        self.pic = Image.open(self.filename).convert("RGBA")
        self.pic = self.pic.resize((600, 400), Image.ANTIALIAS)
        self.txt = Image.new("RGBA", (600, 400), (255, 255, 255, 0))

        self.image = ImageTk.PhotoImage(self.pic)
        self.y = 50
        self.x = 50
        self.canvas = Canvas(self.upload_window,bg=BACKGROUND_COLOR,width=600, height=400,highlightthickness=0)
        self.canvas.pack()
        self.window()
        self.water_mark_widgets()
        self.upload_window.mainloop()


    def window(self):
        title_label_0 = Label(text="MI|YA", bg=BACKGROUND_COLOR, font=('Arial', 15, "bold"), fg="white")
        title_label_01 = Label(text="Simplicity is beauty, functionality is strength", bg=BACKGROUND_COLOR,
                               font=('Arial', 10), fg="white")
        title_label_0.place(x=10, y=10)
        title_label_01.place(x=10, y=30)
        self.upload_window.title("Watermark")
        self.upload_window.config(background=BACKGROUND_COLOR)
        self.upload_window.geometry("800x600")
        self.canvas.create_image(0,0,anchor=NW,image=self.image)
        self.canvas.place(x=40,y=50)


# ---- Water Mark Text Edit ---
    def water_mark_widgets(self):
        wm_text_label = Label(text="Your Watermark Text:",bg=BACKGROUND_COLOR, font=('Arial', 15, "bold"), fg="white")
        wm_text_label.place(x=40,y=450)
        self.wm_text_entry = Entry(self.upload_window,bg=BACKGROUND_COLOR, font=('Arial', 15, "bold"), fg="white",insertbackground="white",highlightcolor="white")
        self.wm_text_entry.place(x=40,y=480,width=600)

        wm_size_label = Label(text="Font Size:", font=('Arial', 15, "bold"), bg=BACKGROUND_COLOR,fg="white")
        wm_size_label.place(x=645, y=30)
        self.wm_size_entry = Entry(self.upload_window, width=15, bg="white", font=('Arial', 15, "bold"), fg=BACKGROUND_COLOR, insertbackground="white", highlightcolor="white")
        self.wm_size_entry.place(x=645, y=50)

        wm_position_x_label = Label(text="Text Position(x)", font=('Arial', 15, "bold"), bg=BACKGROUND_COLOR,fg="white")
        wm_position_x_label.place(x=645, y=80)
        self.wm_position_x_entry = Entry(self.upload_window, width=15, bg="white", font=('Arial', 15, "bold"),
                                   fg=BACKGROUND_COLOR, insertbackground="white", highlightcolor="white")
        self.wm_position_x_entry.place(x=645, y=110)

        wm_position_y_label = Label(text="Text Position(y)", font=('Arial', 15, "bold"), bg=BACKGROUND_COLOR,
                                    fg="white")
        wm_position_y_label.place(x=645, y=140)
        self.wm_position_y_entry = Entry(self.upload_window, width=15, bg="white", font=('Arial', 15, "bold"),
                                         fg=BACKGROUND_COLOR, insertbackground="white", highlightcolor="white")
        self.wm_position_y_entry.place(x=645, y=170)


        wm_text_apply_button = Button(self.upload_window, text="Apply", bg="white", font=('Arial', 20, "bold"),
                                      fg=BACKGROUND_COLOR, command=self.wm_photo)
        wm_text_apply_button.place(x=270, y=510, width=200)

        wm_img_save_button = Button(self.upload_window, text="Save image", bg='#7AA874', font=('Arial', 20, "bold"),
                                      fg='#7AA874', command=self.save_img)
        wm_img_save_button.place(x=270, y=540, width=200)


    def upload_img(self):
        self.f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')]
        filename = filedialog.askopenfilename(filetypes=self.f_types)
        self.image = ImageTk.PhotoImage(file=filename)
        self.canvas.create_image(0,0,anchor=NW,image=self.image)
        self.canvas.place(x=40, y=50)


    def save_img(self):
        self.watermarked.save('watermarked.png')
        messagebox.showinfo(title="SAVED", message="Check Your Project file. Image has been saved")

    def wm_position(self):
        self.x = float(self.wm_position_x_entry.get())
        self.y = float(self.wm_position_y_entry.get())

    def wm_text(self):
        self.wm_text = self.wm_text_entry.get()

    def wm_font_and_size(self):
        self.font_size = int(self.wm_size_entry.get())
        self.font = ImageFont.truetype('Arial.ttf', self.font_size)

# ---- Create watermark on image ----
    def wm_photo(self):
        self.wm_font_and_size()
        self.img_to_draw = ImageDraw.Draw(self.txt)
        self.img_to_draw.text((self.x, self.y),self.wm_text_entry.get(),font_size=self.font_size,font=self.font,fill=(255,255,255,125))
        self.watermarked = Image.alpha_composite(self.pic, self.txt)
        self.watermarked.show()

