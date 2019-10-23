def upload_image():

    from tkinter import Tk
    from tkinter import filedialog

    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (filename)