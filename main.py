import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
import random

Image.MAX_IMAGE_PIXELS = None  # Remove the DecompressionBombWarning limit size

root = tk.Tk()
root.title("Watermarker")
root.geometry('800x800')
root.configure(bg='grey')

canvas = tk.Canvas(width=700, height=700, bg='white')
canvas.grid(row=1, column=1, padx=50, pady=(0, 0))


def save(img):
    name = "Images/Watermarked/" + str(random.randint(1000, 999999)) + '.png'
    print(f'Image save {name}')
    img.save(name)


def drawing(image):
    global entry
    text = entry.get()
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(image)
    # Use custom font
    myFont = ImageFont.truetype("arial.ttf", 15)
    # Add Text to an image
    I1.text((10, 10), text=text, font=myFont, fill='black')

def add_watermark():
    global canvas, img  # Global img allow to keep an external reference and avoid being clean by garbage collector
    max_size = (700, 700)
    img = Image.open(retrieve_file())
    if img.size[0] >= max_size[0] or img.size[1] >= max_size[1]:
        img.thumbnail(max_size)
    drawing(img)
    save(img)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(350, 350, anchor='center', image=img)
    canvas.update()


button = tk.Button(command=add_watermark, text='Open image', bg='white')
button.grid(row=0, column=1, pady=10)

entry = tk.Entry(root, bg='white')
entry.grid(row=2, column=1, pady=15)
entry.insert(0, "Watermark Text")


def retrieve_file(option='f'):
    data = filedialog.askopenfile()
    filename = data.name.split('/')[len(data.name.split('/')) - 1]
    path = data.name.replace(filename, "")
    print(f'Filename : {filename} & Path : {path}')
    if option == 'f':
        return data.name
    elif option == 'p':
        return path
    elif option == 'f':
        return filename
    else:
        return data.name


root.mainloop()
