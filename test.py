from tkinter import *

root = Tk()
root.configure(bg='black')
root.geometry('1280x720')
root.title("Comic Page Creator")

canvas = Canvas(root, height=720, width=720, bg='white', highlightthickness=0)

x1 = y1 = x2 = y2 = click_num = 0

# This covers both rectangles as well as polygons. The reason they are in the same method is to make it easier switch between the two
def draw_shape(point):
	global x1, y1, x2, y2, click_num

	if click_num == 0:
		x1 = point.x
		y1 = point.y
		click_num += 1
	else:
		x2 = point.x
		y2 = point.y
		click_num -= 1
		canvas.create_rectangle(x1, y1, x2, y2, width=5)

def main():
	canvas.bind('<Button-1>', draw_shape)
	canvas.pack()

	root.mainloop()

main()
