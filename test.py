from tkinter import *

root = Tk()
root.configure(bg='black')
root.geometry('1280x720')
root.title("Comic Page Creator")

canvas = Canvas(root, height=720, width=720, bg='white', highlightthickness=0)

x0 = y0 = x1 = y1 = click_num = 0

# This covers both rectangles as well as polygons. The reason they are in the same method is to make it easier switch between the two
def draw_shape(point):
	global x0, y0, x1, y1, click_num

	if click_num == 0:
		x0, y0 = point.x, point.y
		click_num += 1
	else:
		x1, y1 = point.x, point.y
		click_num -= 1
		canvas.create_rectangle(x0, y0, x1, y1, width=5)

def draw(point):
	if canvas.old_coords:
		x0, y0 = canvas.old_coords
		canvas.create_line(x0, y0, point.x, point.y)
	canvas.old_coords = point.x, point.y

def draw_cross(point):
	if canvas.old_coords:
		x0, y0 = canvas.old_coords
		canvas.create_line(x0, y0, point.x, y0)
		canvas.create_line(x0, y0, x0, point.y)
	else:
		canvas.old_coords = point.x, point.y

def main():
	canvas.old_coords = None
	# canvas.bind('<Button-1>', draw_shape)
	# canvas.bind('<B1-Motion>', draw)
	canvas.bind('<B1-Pressed>', draw_cross)
	canvas.pack()

	root.mainloop()

main()
