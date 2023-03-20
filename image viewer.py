from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.geometry("600x600")
root.title("Image Viewer")
root.configure(background="black")

lbl=Label(root, highlightthickness=5, borderwidth=2, relief=SOLID, bg="yellow")
lbl.place(relx=0.5, rely=0.6, anchor=CENTER)
img_path=""

def openimage():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Image File", filetypes=[("Image Files", "*.jpg *.gif *.png *.jpeg")])
    print(img_path)
    img1=Image.open(img_path)
    img_e=ImageTk.PhotoImage(img1)
    lbl["image"]=img_e
    img_e.close()

def rotate_img():
    global img_path
    im=Image.open(img_path)
    img=ImageTk.PhotoImage(im.rotate(180))
    lbl["image"]=img
    img.close()

btn_rotate=Button(root, text="Rotate Image", command=rotate_img, font=("Lucida Sans Unicode", 20, "bold"), bg="gray")    
btn_open=Button(root, text="Open Image", command=openimage, font=("Lucida Sans Unicode", 20, "bold"), bg="gray")
btn_open.place(relx=0.5, rely=0.1, anchor=CENTER)
btn_rotate.place(relx=0.5, rely=0.3, anchor=CENTER)
root.mainloop()