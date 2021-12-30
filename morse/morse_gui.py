import tkinter as tk
from tkinter import font
import random
from tkinter.constants import FLAT, GROOVE, LEFT, RAISED, RIDGE, SUNKEN
import morse
from PIL import Image, ImageTk

m = morse.Morse()
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
cur_title_icon = ['./icons/components/morse_code_icon.png']
cur_title_icon_size = [(64, 64)]
def main():
    root = tk.Tk()
    root.configure(bg="#FFFFFF")
    root.title('Morse Code Translator')
    root.iconbitmap('./icons/morse_code_icon.ico')
    root.minsize(width=1024, height=512)
    root.maxsize(width=1024, height=512)
    home_page(root)

def home_page(root):
    clear(root)
    encode_icon = Image.open('./icons/components/abc_to_abc_morse.png')
    encode_icon = encode_icon.resize((512,512))
    encode_icon = ImageTk.PhotoImage(encode_icon)
    decode_icon = Image.open('./icons/components/abc_morse_to_abc.png')
    decode_icon = decode_icon.resize((512,512))
    decode_icon = ImageTk.PhotoImage(decode_icon)
    title_icon = Image.open('./icons/components/morse_code_icon.png')
    title_icon = title_icon.resize((64, 64))
    title_icon = ImageTk.PhotoImage(title_icon)
    encode_button = tk.Button(root, image=encode_icon, activebackground="#7AFF8E", bd=0, bg="#7AFF8E", command=lambda: click_encode(root), height=416, width=512, cursor=cursors[0])
    decode_button = tk.Button(root, image=decode_icon, activebackground="#FF6D6D", bd=0, bg="#FF6D6D", command=lambda: click_decode(root), height=416, width=512, cursor=cursors[0])
    title_button = tk.Button(root, image=title_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=lambda: click_title(root, title_button, encode_button, decode_button), height=96, width=1024, cursor=cursors[1])
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
        title_icon = title_icon.resize((72, 72))
        title_icon = ImageTk.PhotoImage(title_icon)
        title_button.config(image=title_icon)
        cur_title_icon[0] = './icons/components/egg_morse_icon.png'
        cur_title_icon_size[0] = (72, 72)
        counter[0] = 1
    elif counter[0] == 1:
        title_icon = Image.open('./icons/components/egg_icon.png')
        title_icon = title_icon.resize((64, 64))
        title_icon = ImageTk.PhotoImage(title_icon)
        title_button.config(image=title_icon)
        cur_title_icon[0] = './icons/components/egg_icon.png'
        cur_title_icon_size[0] = (64, 64)
        counter[0] = 2
    elif counter[0] == 2 or counter[0] == 3:
        title_icon = Image.open('./icons/components/egg_cracked_icon.png')
        title_icon = title_icon.resize((64, 64))
        title_icon = ImageTk.PhotoImage(title_icon)
        title_button.config(image=title_icon)
        if counter[0] == 3:
            shuffle()
            title_button.config(cursor=cursors[1])
            encode_button.config(cursor=cursors[0])
            decode_button.config(cursor=cursors[0])
        cur_title_icon[0] = './icons/components/egg_cracked_icon.png'
        cur_title_icon_size[0] = (64, 64)
        counter[0] = 3
    root.mainloop()

def click_encode(root):
    clear(root)
    
    text_font = font.Font(family='Courier', size=18)
    text_font_morse = font.Font(family='Courier', size=12)
    text = tk.Text(root, bg="#7AFF8E", bd=0, height=14, width=34, font=text_font, cursor=cursors[0], padx=19, pady=18)
    result_text = tk.Text(root, bg="#FF6D6D", bd=0, cursor=cursors[1], font=text_font_morse, height=21, width=47, state='disabled', padx=22, pady=18)
    text.bind("<KeyRelease>", lambda event: get_morse(event, text, result_text))
    
    text_icon = Image.open('./icons/components/abc_custom.png')
    text_icon = text_icon.resize((72, 72))
    text_icon = ImageTk.PhotoImage(text_icon)
    text_title = tk.Label(root, bg="#FFFFFF", bd=0, cursor=cursors[1], height=48, width=512, image=text_icon)
    morse_icon = Image.open('./icons/components/abc_morse_icon.png')
    morse_icon = morse_icon.resize((48, 48))
    morse_icon = ImageTk.PhotoImage(morse_icon)
    morse_title = tk.Label(root, bg="#FFFFFF", bd=0, cursor=cursors[1], height=48, width=512, image=morse_icon)
    
    return_icon = Image.open('./icons/components/back_arrow_icon.png')
    return_icon = return_icon.resize((56, 56))
    return_icon = ImageTk.PhotoImage(return_icon)
    return_button = tk.Button(root, image=return_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=lambda: home_page(root), height=52, width=1024, cursor=cursors[0])
    
    if not (return_button is None or text is None or result_text is None or text_title is None or morse_title is None):
        text_title.grid(row=0, column=0)
        morse_title.grid(row=0, column=1)
        text.grid(row=1, column=0)
        result_text.grid(row=1, column=1)
        return_button.grid(row=2, column=0, columnspan=2)
    
    root.mainloop()

def click_decode(root):
    clear(root)

    text_icon = Image.open('./icons/components/abc_custom.png')
    text_icon = text_icon.resize((72, 72))
    text_icon = ImageTk.PhotoImage(text_icon)
    text_title = tk.Label(root, bg="#FFFFFF", bd=0, cursor=cursors[1], height=48, width=512, image=text_icon)
    morse_icon = Image.open('./icons/components/abc_morse_icon.png')
    morse_icon = morse_icon.resize((48, 48))
    morse_icon = ImageTk.PhotoImage(morse_icon)
    morse_title = tk.Label(root, bg="#FFFFFF", bd=0, cursor=cursors[1], height=48, width=512, image=morse_icon)
    
    text_font = font.Font(family='Courier', size=18)
    text_font_morse = font.Font(family='Courier', size=12)
    result_text = tk.Text(root, bg="#FF6D6D", bd=0, cursor=cursors[1], font=text_font, height=12, width=34, state='disabled', padx=23, pady=18)
    morse_text = tk.Text(root, bg="#7AFF8E", bd=0, cursor=cursors[0], font=text_font_morse, height=18, width=47, padx=23, pady=18)
    morse_text.bind("<KeyRelease>", lambda event: get_text(event, morse_text, result_text))

    dot_icon = Image.open('./icons/components/dot_custom.png')
    dot_icon = dot_icon.resize((24, 24))
    dot_icon = ImageTk.PhotoImage(dot_icon)
    dot_button = tk.Button(root, image=dot_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=None, height=44, width=256, cursor=cursors[0])
    dot_button.bind("<1>", lambda event: append_dot(event, morse_text, result_text))

    dash_icon = Image.open('./icons/components/dash_custom.png')
    dash_icon = dash_icon.resize((64, 64))
    dash_icon = ImageTk.PhotoImage(dash_icon)
    dash_button = tk.Button(root, image=dash_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=None, height=44, width=256, cursor=cursors[0])
    dash_button.bind("<1>", lambda event: append_dash(event, morse_text, result_text))

    slash_icon = Image.open('./icons/components/forwardslash_icon.png')
    slash_icon = slash_icon.resize((36, 36))
    slash_icon = ImageTk.PhotoImage(slash_icon)
    slash_button = tk.Button(root, image=slash_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=None, height=44, width=256, cursor=cursors[0])
    slash_button.bind("<1>", lambda event: append_slash(event, morse_text, result_text))

    backspace_icon = Image.open('./icons/components/backspace_icon.png')
    backspace_icon = backspace_icon.resize((32, 32))
    backspace_icon = ImageTk.PhotoImage(backspace_icon)
    backspace_button = tk.Button(root, image=backspace_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=None, height=44, width=256, cursor=cursors[0])
    backspace_button.bind("<1>", lambda event: pop_char(event, morse_text, result_text))

    return_icon = Image.open('./icons/components/back_arrow_icon.png')
    return_icon = return_icon.resize((56, 56))
    return_icon = ImageTk.PhotoImage(return_icon)
    return_button = tk.Button(root, image=return_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=lambda: home_page(root), height=48, width=256, cursor=cursors[0])
    
    space_icon = Image.open('./icons/components/space_icon.png')
    space_icon = space_icon.resize((48, 48))
    space_icon = ImageTk.PhotoImage(space_icon)
    space_button = tk.Button(root, image=space_icon, activebackground="#FFFFFF", bd=0, bg="#FFFFFF", command=None, height=44, width=256, cursor=cursors[0])
    space_button.bind("<1>", lambda event: append_space(event, morse_text, result_text))

    if not (return_button is None or slash_button is None or space_button is None or dot_button is None or dash_button is None or backspace_button is None or morse_text is None or result_text is None or text_title is None or morse_title is None):
        text_title.grid(row=0, column=0, columnspan=2)
        morse_title.grid(row=0, column=2, columnspan=2)
        return_button.grid(row=2, rowspan=2, column=0)
        space_button.grid(row=3, column=1)
        slash_button.grid(row=3, column=2)
        backspace_button.grid(row=2, rowspan=2, column=3)
        dot_button.grid(row=2, column=1)
        dash_button.grid(row=2, column=2)
        morse_text.grid(row=1, column=0, columnspan=2)
        result_text.grid(row=1, column=2, columnspan=2)
    
    root.mainloop()

def get_morse(event, text, result_text):
    t = text.get("1.0", "end-1c")
    t = t.lower()
    result = ""
    for char in t:
        if ord(char) != 32 and not(char in m.mapping):
            result = "invalid input"
    if len(result) == 0:
        result = m.encode(t)
    result_text.configure(state='normal')
    result_text.delete(1.0, 'end')
    result_text.insert('end', result)
    result_text.configure(state='disabled')

def get_text(event, morse_text, result_text):
    morse = morse_text.get("1.0", "end-1c")
    result = ""
    for char in morse:
        if ord(char) != 32 and ord(char) != 45 and ord(char) != 46 and ord(char) != 47:
            result = "invalid input"
    if len(result) == 0:
        try:
            result = m.decode(morse)
        except Exception as e:
            result = "invalid input"

    result_text.configure(state='normal')
    result_text.delete(1.0, 'end')
    result_text.insert('end', result)
    result_text.configure(state='disabled')

def append_space(event, morse_text, result_text):
    append_char(event, morse_text, result_text, ' ')

def append_dot(event, morse_text, result_text):
    append_char(event, morse_text, result_text, '.')

def append_dash(event, morse_text, result_text):
    append_char(event, morse_text, result_text, '-')

def append_slash(event, morse_text, result_text):
    append_char(event, morse_text, result_text, '/')

def append_char(event, morse_text, result_text, c):
    morse = morse_text.get("1.0", "end-1c")
    result = ""
    for char in morse:
        if ord(char) != 32 and ord(char) != 45 and ord(char) != 46 and ord(char) != 47:
            result = "invalid input"
    morse += c
    morse_text.delete(1.0, 'end')
    morse_text.insert('end', morse)
    if len(result) == 0:
        try:
            result = m.decode(morse)
        except Exception as e:
            result = "invalid input"
    result_text.configure(state='normal')
    result_text.delete(1.0, 'end')
    result_text.insert('end', result)
    result_text.configure(state='disabled')

def pop_char(event, morse_text, result_text):
    morse = morse_text.get("1.0", "end-1c")
    if len(morse) == 0:
        return
    result = ""
    for char in morse:
        if ord(char) != 32 and ord(char) != 45 and ord(char) != 46 and ord(char) != 47:
            result = "invalid input"
    morse = morse[:-1]
    morse_text.delete(1.0, 'end')
    morse_text.insert('end', morse)
    if len(result) == 0:
        try:
            result = m.decode(morse)
        except Exception as e:
            result = "invalid input"
    result_text.configure(state='normal')
    result_text.delete(1.0, 'end')
    result_text.insert('end', result)
    result_text.configure(state='disabled')

def clear(root):
    objs = root.grid_slaves()
    for o in objs:
        o.destroy()

def shuffle():
    random.shuffle(cursors)


if __name__ == '__main__':
    main()