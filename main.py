from tkinter import *

root = Tk()
root.configure(bg='purple')
root.geometry('1280x720')
root.title("Comic Page Creator")

canvas = Canvas(root, height=720, width=720, bg='blue', highlightthickness=0)
# canvas.create_line(0,0,720,720, width=50)
canvas.create_rectangle(0,0,720,720, width=30)
canvas.pack()

# label = Label(canvas, text="Test Label")
# label.configure(bg='blue', fg='white')
# label.pack()

root.mainloop()
