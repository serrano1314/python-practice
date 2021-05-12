from tkinter import *
from PIL import ImageTk,Image
# import tkFont

def forward():
    global img_id
    global img_list
    global img
    img_id+=1
    if img_id == len(img_list):
        img_id=0
    img = resize_img(img_list[img_id])
    display()
    
def back():
    global img_id
    global img_list
    global img
    img_id-=1
    if img_id < 0:
        img_id=len(img_list)-1
        
    img = resize_img(img_list[img_id])
    display()

def resize_img(img_name):
    #Resizing image
    basewidth = 300
    img=Image.open(img_name)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize),Image.ANTIALIAS)
    return img
    
def display():
    global img
    img = ImageTk.PhotoImage(img)
    label = Label(root, image=img)
    label.grid(row=0,column=0,columnspan=2)

root = Tk()
root.title('Photo Viewer')
#root.iconbitmap('ico/adobe-xd.ico')
img_list = ('img/iu.jpg','img/iu2.jpg','img/iu3.jpg','img/iu4.jpg','img/iu5.jpg')
img_id = 0


forward_btn = Button(root,text=">>",command=forward)
back_btn = Button(root,text="<<",command=back)
# print(type(label))
img=resize_img(img_list[img_id])
display()
back_btn.grid(row=1,column=0)
forward_btn.grid(row=1,column=1)
root.mainloop()