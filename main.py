import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
import random
from functools import partial

Image.MAX_IMAGE_PIXELS = None  # Remove the DecompressionBombWarning limit size

root = tk.Tk()
root.title("Watermarker")
root.geometry('800x800')
root.configure(bg='grey')
I1 = ''
next_color = 'black'
current_image = ''

canvas = tk.Canvas(width=700, height=700, bg='white')
canvas.grid(row=1, column=0, padx=50, pady=(0, 0), columnspan=3)


def save(img):
    name = "Images/Watermarked/" + str(random.randint(1000, 999999)) + '.png'
    print(f'Image save {name}')
    img.save(name)
    tkinter.messagebox.showinfo(title='Image saved', message=f'You image have been saved as {name}.')


def drawing(image):
    global entry, next_color
    text = entry.get()
    # Call draw Method to add 2D graphics in an image
    global I1
    I1 = ImageDraw.Draw(image)
    # Use custom font
    myFont = ImageFont.truetype("arial.ttf", 15)
    # Add Text to an image
    I1.text((10, 10), text=text, font=myFont, fill=next_color)
    if next_color == 'black':
        next_color = 'white'
    else:
        next_color = 'black'


def change_color():
    add_watermark(2)


def add_watermark(option=1):
    global canvas, img  # Global img allow to keep an external reference and avoid being clean by garbage collector
    max_size = (700, 700)
    if option == 2:
        img = Image.open(current_image)
    else:
        img = Image.open(retrieve_file())

    if img.size[0] >= max_size[0] or img.size[1] >= max_size[1]:
        img.thumbnail(max_size)
    drawing(img)
    button3.configure(command=partial(save, img))
    img = ImageTk.PhotoImage(img)
    canvas.create_image(350, 350, anchor='center', image=img)
    canvas.update()


# --------------- Graphic interface --------------

button = tk.Button(command=add_watermark, text='Open image', bg='white')
button.grid(row=0, column=1, pady=10)

frame = tk.Frame(root)
frame.grid(row=0, column=0)
button1 = tk.Button(frame, command=change_color, text='Black/White', bg='white')
button1.grid(row=0, column=0)
# Not implemented yet
# button2 = tk.Button(frame, command='', text='Change position', bg='white')
# button2.grid(row=0, column=1)

button3 = tk.Button(text='Save', bg='white')
button3.grid(row=0, column=2)

entry = tk.Entry(root, bg='white')
entry.grid(row=2, column=0, columnspan=3, pady=15)
entry.insert(0, "Watermark Text")


def retrieve_file(option='f'):
    global current_image
    data = filedialog.askopenfile()
    filename = data.name.split('/')[len(data.name.split('/')) - 1]
    path = data.name.replace(filename, "")
    print(f'Filename : {filename} & Path : {path}')
    current_image = data.name
    if option == 'f':
        return data.name
    elif option == 'p':
        return path
    elif option == 'f':
        return filename
    else:
        return data.name


root.mainloop()
