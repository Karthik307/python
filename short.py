from tkinter import *
import pyshorteners as p
import pyqrcode
import png 
import PIL.Image
import pyperclip

top = Tk()
top.geometry("300x300")
top.title("URL Shorter")
top.configure(bg="#000000")
url=StringVar()
url_address=StringVar()
is_on=False

def urlsh():
    s=url.get()
    y=p.Shortener()
    op=y.tinyurl.short(s)
    url_address.set(op)
def urlcopy():
    y=url_address.get()
    pyperclip.copy(y)
def qrcode():
    qr_data =url.get()
    y=p.Shortener()
    op=y.tinyurl.short(qr_data)
    u= pyqrcode.create(op)
    u.png('url.png', scale = 8)
    img =PIL.Image.open('url.png')
    img.show()
def them():
    global is_on
    if is_on:
        top.configure(bg="#000000")
        is_on=False
    else:
        top.configure(bg="#ffffff")
        is_on=True
Entry(top,textvariable=url).pack(pady=5)
Button(top,text="Shorten URL",command=urlsh).pack(pady=7)
Entry(top,textvariable=url_address).pack(pady=5)
Button(top,text="create QR code",command=qrcode).pack(pady=5)
Button(top,text="Copy",command=urlcopy).pack(pady=5)
Button(top,text="Switch Theme ☀",command=them).pack(pady=5)
top.mainloop()