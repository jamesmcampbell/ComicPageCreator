from tkinter import *

window = Tk()
window.configure(bg='purple')
window.geometry('1280x720')
window.title("Comic Page Creator")

canvas = Canvas(window, height=720, width=720, bg='blue')
canvas.create_line(0,0,720,720, width=50)
canvas.create_rectangle(0,0,720,720, width=50)
canvas.pack()

# label = Label(canvas, text="Test Label")
# label.configure(bg='blue', fg='white')
# label.pack()

window.mainloop()
