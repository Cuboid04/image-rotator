from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.geometry("600x600")
root.title("Image Viewer")
root.configure(background="black")

lbl=Label(root, highlightthickness=5, borderwidth=2, relief=SOLID, bg="yellow")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
img_path=""

def openimage():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Image File", filetypes=[("Image Files", "*.jpg *.gif *.png *.jpeg")])
    print(img_path)
    img=Image.open(img_path)
    img_e=ImageTk.PhotoImage(img)
    lbl["image"]=img_e
    img_e.close()
    
btn=Button(root, text="Open Image", command=openimage, font=("Lucida Sans Unicode", 20, "bold"), bg="gray")
btn.place(relx=0.5, rely=0.1, anchor=CENTER)

root.mainloop()