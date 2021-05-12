from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('IMAGE OPEN')

def resize_img(img_name):
    #Resizing image
    basewidth = 300
    img=Image.open(img_name)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize),Image.ANTIALIAS)
    return img

def open_image():
    file_type = (("Jpg files",".jpg"),("All Files","*.*"))
    global img
    root.filename = filedialog.askopenfilename(initialdir="/user/",title="Open Image",filetypes=file_type)
    print(root.filename+"hello")
    img = resize_img(root.filename)
    img = ImageTk.PhotoImage(img)
    Label(image=img).pack()

Button(root, text="Open Image",command=open_image).pack()

root.mainloop()