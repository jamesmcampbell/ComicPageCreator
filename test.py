from tkinter import *

window = Tk()
window.configure(bg='purple')
window.geometry('1280x720')
window.title("Comic Page Creator")

canvas = Canvas(window, height=720, width=720, bg='blue', highlightthickness=0)
canvas.create_rectangle(0,0,720,720, width=30)
canvas.pack()

window.mainloop()
