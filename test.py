from tkinter import *

root = Tk()
root.configure(bg='black')
root.geometry('1280x720')
root.title("Comic Page Creator")

canvas = Canvas(root, height=720, width=720, bg='white', highlightthickness=0)

click_num = 0

# This covers both rectangles as well as polygons. The reason they are in the same method is to make it easier switch between the two
def draw_shape(click):
	global x1, y1, x2, y2, click_num
	x1 = y1 = x2 = y2 = 0

	if click_num == 0:
		x1 = click.x
		y1 = click.y
		click_num += 1
	else:
		x2 = click.x
		y2 = click.y
		click_num -= 1
		canvas.create_rectangle(x1, y1, x2, y2, width=5)

def main():
	# global click_num
	canvas.bind('<Button-1>', draw_shape)
	# click_num = 0
	canvas.pack()

	root.mainloop()

main()
