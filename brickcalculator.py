import tkinter as tk
from tkinter import ttk


def calculate_bricks_needed():
    brick_length = float(brick_length_var.get())
    brick_width = float(brick_width_var.get())
    brick_height = float(brick_height_var.get())
    wall_length = float(wall_length_var.get())
    wall_width = float(wall_width_var.get())
    wall_height = float(wall_height_var.get())
    mortar_thickness = float(mortar_thickness_var.get())

    brick_length += mortar_thickness
    brick_height += mortar_thickness

    brick_volume = brick_length * brick_width * brick_height
    wall_volume = wall_length * wall_width * wall_height
    bricks_needed = int(wall_volume // brick_volume)

    result_var.set(f"Number of bricks needed to build the wall: {bricks_needed}")


root = tk.Tk()
root.title("Bricks Calculator by hossein bagheri")

brick_length_var = tk.StringVar()
brick_width_var = tk.StringVar()
brick_height_var = tk.StringVar()
wall_length_var = tk.StringVar()
wall_width_var = tk.StringVar()
wall_height_var = tk.StringVar()
mortar_thickness_var = tk.StringVar()
result_var = tk.StringVar()

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

ttk.Label(frame, text="Enter the length of the brick:").grid(row=0, column=0, sticky="W")
ttk.Entry(frame, textvariable=brick_length_var).grid(row=0, column=1)

ttk.Label(frame, text="Enter the width of the brick:").grid(row=1, column=0, sticky="W")
ttk.Entry(frame, textvariable=brick_width_var).grid(row=1, column=1)

ttk.Label(frame, text="Enter the height of the brick:").grid(row=2, column=0, sticky="W")
ttk.Entry(frame, textvariable=brick_height_var).grid(row=2, column=1)

ttk.Label(frame, text="Enter the length of the wall:").grid(row=3, column=0, sticky="W")
ttk.Entry(frame, textvariable=wall_length_var).grid(row=3, column=1)

ttk.Label(frame, text="Enter the width of the wall:").grid(row=4, column=0, sticky="W")
ttk.Entry(frame, textvariable=wall_width_var).grid(row=4, column=1)

ttk.Label(frame, text="Enter the height of the wall:").grid(row=5, column=0, sticky="W")
ttk.Entry(frame, textvariable=wall_height_var).grid(row=5, column=1)

ttk.Label(frame, text="Enter the mortar thickness:").grid(row=6, column=0, sticky="W")
ttk.Entry(frame, textvariable=mortar_thickness_var).grid(row=6, column=1)

ttk.Button(frame, text="Calculate", command=calculate_bricks_needed).grid(row=7, column=0, columnspan=2, pady="10")

ttk.Label(frame, textvariable=result_var).grid(row=8, column=0, columnspan=2, pady="5")

root.mainloop()
