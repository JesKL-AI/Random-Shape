import tkinter as tk
import turtle
import random

from tkinter import *

colours = ['purple', 'red','blue', 'yellow', 'green', 'orange']

def fn_validate_entry(x):
    if x!='':
        return x.isdigit()
    return True

def fn_calculate_angle(sides):
    return 360 / sides

def fn_draw_polygon_fill(sides, size, colour):
    pen.fillcolor(colour)
    pen.begin_fill()
    angle = fn_calculate_angle(sides)
    for i in range(sides):
        pen.forward(size)
        pen.right(angle)
    pen.end_fill()

def fn_draw_shapes():
    num_shapes = int(num_shapes_entry.get())
    min_sides = int(min_sides_entry.get())
    max_sides = int(max_sides_entry.get())
    
    if min_sides < 3 or min_sides > max_sides:
        return 0

    for i in range(num_shapes):
        random_shape = random.randint(min_sides, max_sides)
        random_colour = random.choice(colours)
        random_angle = random.randint(0,180)
        random_size = random.randint(10, 200)
        random_forward = random.randint(10, 360)
        pen.penup()
        pen.right(random_angle)
        pen.forward(random_forward)
        pen.pendown()
        fn_draw_polygon_fill(random_shape, random_size, random_colour)

main_window = tk.Tk()
main_window.title('Draw shapes!')

second_window = tk.Tk()
second_window.title('Your Shapes')
canvas = tk.Canvas(master = second_window, width = 800, height = 800)
canvas.config(bg = 'white')
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
pen = turtle.RawTurtle(canvas)
validate_entry = main_window.register(fn_validate_entry)

frame = tk.Frame()
frame.config(bg = 'white')
frame.grid(column = 0, row = 0, padx = 20, pady = 20)

header = tk.Label(frame, text = 'Draw a shape')
header.config(font = ('Calibri bold', 40), width = 20, borderwidth = 2, relief = 'solid', height = 2)
header.grid(column = 0, row = 0, sticky = 'ew', columnspan = 2)

label = tk.Label(frame, text = "Enter no. of Shapes")
label.config(font = ("Calibri",32), width = 15, borderwidth = 2, relief = 'solid')
label.grid(column = 0, row = 1, pady = 20, sticky = 'w')

num_shapes_entry = tk.Entry(frame)
num_shapes_entry.config(font = ('Calibri', 36), justify = 'center', width = 4,
                        validate = 'key', validatecommand = (validate_entry, '%P'))
num_shapes_entry.grid(column = 1, row = 1, sticky = 'e')

label = tk.Label(frame, text = "Max no. of Sides")
label.config(font = ("Calibri",32), width = 15, borderwidth = 2, relief = 'solid')
label.grid(column = 0, row = 2, pady = 20, sticky = 'w')

max_sides_entry = tk.Entry(frame)
max_sides_entry.config(font = ('Calibri', 36), justify = 'center', width = 4,
                        validate = 'key', validatecommand = (validate_entry, '%P'))
max_sides_entry.grid(column = 1, row = 2, sticky = 'e')

label = tk.Label(frame, text = "Min no. of Sides")
label.config(font = ("Calibri",32), width = 15, borderwidth = 2, relief = 'solid')
label.grid(column = 0, row = 3, pady = 20, sticky = 'w')

min_sides_entry = tk.Entry(frame)
min_sides_entry.config(font = ('Calibri', 36), justify = 'center', width = 4,
                        validate = 'key', validatecommand = (validate_entry, '%P'))
min_sides_entry.grid(column = 1, row = 3, sticky = 'e')

enter_button = tk.Button(frame, text = "Press me to draw tings Bruv")
enter_button.config(font = ('Calibri bold', 32), height = 2, bg = 'Red', fg = 'White', command = fn_draw_shapes)
enter_button.grid(column = 0, row = 4, columnspan = 2, sticky = 'ew')

tk.mainloop()
