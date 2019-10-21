import tensorflow as tf
from tkinter import *
from upload import upload_image
 
#window
main = Tk()
main.title('Identification of Tumor')
#favicon
main.call('wm', 'iconphoto', main._w, PhotoImage(file='images/tdiFavicon.png'))

#open file
Button(main, text='Upload Photo', command=upload_image).grid(row=0)

Label(main, text = "Select your gender:").grid(row=1)

mainloop()