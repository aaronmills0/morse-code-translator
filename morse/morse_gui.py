import tkinter as tk
from tkinter import font
import random
from tkinter.constants import FLAT, GROOVE, LEFT, RAISED, RIDGE, SUNKEN
import morse
from PIL import Image, ImageTk

m = morse.Morse()
morse_string = [""]
counter = [0]
cursors = [
    "hand2",
    "arrow",
    "boat",
    "box_spiral",
    "center_ptr",
    "circle",
    "clock",
    "coffee_mug",
    "crosshair",
    "diamond_cross",
    "dot",
    "dotbox",
    "fleur",
    "ibeam",
    "hand1",
    "heart",
    "icon",
    "left_ptr",
    "man",
    "mouse",
    "pencil",
    "pirate",
    "plus",
    "question_arrow",
    "right_ptr",
    "sailboat",
    "shuttle",
    "spider",
    "spraycan",
    "star",
    "target",
    "top_left_arrow",
    "trek",
    "umbrella",
    "watch",
    "X_cursor"
]
cur_title_icon = ['./icons/components/morse_code_translator_icon.png']
cur_title_icon_size = [(368, 368)]
def main():
    root = tk.Tk()
    root.configure(bg="#FFFFFF")
    root.title('Morse Code Translator')
    root.iconbitmap('./icons/morse_code_icon.ico')
    root.minsize(width=512, height=256)
    root.maxsize(width=512, height=256)
    home_page(root)

def home_page(root):
    clear(root)
    encode_icon = Image.open('./icons/components/abc_to_abc_morse.png')
    encode_icon = encode_icon.resize((256,256))
    encode_icon = ImageTk.PhotoImage(encode_icon)
    decode_icon = Image.open('./icons/components/abc_morse_to_abc.png')
    decode_icon = decode_icon.resize((256,256))
    decode_icon = ImageTk.PhotoImage(decode_icon)
    title_icon = Image.open('./icons/components/morse_code_translator_icon.png')
    title_icon = title_icon.resize((368, 368))
    title_icon = ImageTk.PhotoImage(title_icon)
    encode_button = tk.Button(root, image=encode_icon, activebackground="#7AFF8E", bd=0, bg="#7AFF8E", command=lambda: click_encode(root), height=208, width=256, cursor=cursors[0])
    decode_button = tk.Button(root, image=decode_icon, activebackground="#FF6D6D", bd=0, bg="#FF6D6D", command=lambda: click_decode(root), height=208, width=256, cursor=cursors[0])
    title_button = tk.Button(root, image=title_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=lambda: click_title(root, title_button, encode_button, decode_button), height=48, width=512, cursor=cursors[1])
    if not (title_button is None or encode_button is None or decode_button is None):
        title_button.grid(row=0, column=0, columnspan=2)
        encode_button.grid(row=1, column=0)
        decode_button.grid(row=1, column=1)
    title_icon = Image.open(cur_title_icon[0])
    title_icon = title_icon.resize(cur_title_icon_size[0])
    title_icon = ImageTk.PhotoImage(title_icon)
    title_button.config(image=title_icon)
    root.mainloop()

def click_title(root, title_button, encode_button, decode_button):
    global counter
    if counter[0] == 0 :
        title_icon = Image.open('./icons/components/egg_morse_icon.png')
        title_icon = title_icon.resize((40, 40))
        title_icon = ImageTk.PhotoImage(title_icon)
        title_button.config(image=title_icon)
        cur_title_icon[0] = './icons/components/egg_morse_icon.png'
        cur_title_icon_size[0] = (40, 40)
        counter[0] = 1
    elif counter[0] == 1:
        title_icon = Image.open('./icons/components/egg_icon.png')
        title_icon = title_icon.resize((36, 36))
        title_icon = ImageTk.PhotoImage(title_icon)
        title_button.config(image=title_icon)
        cur_title_icon[0] = './icons/components/egg_icon.png'
        cur_title_icon_size[0] = (36, 36)
        counter[0] = 2
    elif counter[0] == 2 or counter[0] == 3:
        title_icon = Image.open('./icons/components/egg_cracked_icon.png')
        title_icon = title_icon.resize((36, 36))
        title_icon = ImageTk.PhotoImage(title_icon)
        title_button.config(image=title_icon)
        if counter[0] == 3:
            shuffle()
            title_button.config(cursor=cursors[1])
            encode_button.config(cursor=cursors[0])
            decode_button.config(cursor=cursors[0])
        cur_title_icon[0] = './icons/components/egg_cracked_icon.png'
        cur_title_icon_size[0] = (36, 36)
        counter[0] = 3
    root.mainloop()

def click_encode(root):
    clear(root)
    text_font = font.Font(family='Courier', size=12)
    text_font_morse = font.Font(family='Courier', size=6)
    text_font_lg = font.Font(family='Courier', size=18, weight=font.BOLD)
    text = tk.Text(root, bg="#7AFF8E", bd=0, height=8, width=25, font=text_font, cursor=cursors[0], padx=5, pady=1)
    result_text = tk.Text(root, bg="#FF6D6D", bd=0, cursor=cursors[1], font=text_font_morse, height=18, width=50, state='disabled', padx=5, pady=1)
    text_title = tk.Label(root, bg="#FFFFFF", bd=0, cursor=cursors[1], font=text_font_lg, height=2, width=13, text="TEXT")
    morse_title = tk.Label(root, bg="#FFFFFF", bd=0, cursor=cursors[1], font=text_font_lg, height=2, width=13, text="MORSE")
    text.bind("<KeyRelease>", lambda event: get_morse(event, root, text, result_text))
    return_icon = Image.open('./icons/components/back_arrow_icon.png')
    return_icon = return_icon.resize((48, 48))
    return_icon = ImageTk.PhotoImage(return_icon)
    return_button = tk.Button(root, image=return_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=lambda: home_page(root), height=48, width=512, cursor=cursors[0])
    
    if not (return_button is None or text is None or result_text is None or text_title is None or morse_title is None):
        text_title.grid(row=0, column=0)
        morse_title.grid(row=0, column=1)
        text.grid(row=1, column=0)
        result_text.grid(row=1, column=1)
        return_button.grid(row=2, column=0, columnspan=2)
    
    root.mainloop()

def get_morse(event, root, text, result_text):
    t = text.get("1.0", "end-1c")
    t = t.lower()
    result = ""
    for char in t:
        if ord(char) != 32 and (ord(char) < 97 or ord(char) > 122):
            result = "invalid input"
    if len(result) == 0:
        result = m.encode(t)
    result_text.configure(state='normal')
    result_text.delete(1.0, 'end')
    result_text.insert('end', result)
    result_text.configure(state='disabled')

def click_decode(root):
    clear(root)

def clear(root):
    objs = root.grid_slaves()
    for o in objs:
        o.destroy()

def shuffle():
    random.shuffle(cursors)


if __name__ == '__main__':
    main()