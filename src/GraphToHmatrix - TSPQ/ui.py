from tkinter import *
from tkinter import ttk

from numpy import pad


# Initialize root component
root = Tk()
root.title("Graph to Matrix - TSPQ")
root.option_add('*tearOff', FALSE)


def clearCanvas():
    pass


def openFile():
    pass


def exitProgram():
    pass


def undo():
    pass


def redo():
    pass


# Create menu bar
menubar = Menu(root)
root['menu'] = menubar
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')
menu_file.add_command(label='Clear', command=clearCanvas)
menu_file.add_command(label='Open...', command=openFile)
menu_file.add_command(label='Exit', command=exitProgram)
menu_edit.add_command(label='Undo', command=undo)
menu_edit.add_command(label='Redo', command=redo)

ttk.Label(root, text="Draw on the canvas to set points.").grid(
    column=1, row=1, sticky=W)
canvas = Canvas(root, width=500, height=400, background="white")
canvas.grid(column=1, rowspan=5, sticky=(N, S, E, W))
canvas.create_rectangle(
    4, 4, 500, 400, outline="dim gray", width=2, fill="white")

ttk.Label(root, text="Click to generate the distances\nand the Hamilton matrix.\nThis can take a few moments,\ndepending on the number of\nvertices drawn.", justify="center").grid(
    column=2, row=2, padx=30)
ttk.Button(root, text="Generate").grid(column=2, row=3)
matrix_label = StringVar(value="Generated:")
ttk.Label(root, textvariable=matrix_label).grid(
    column=2, row=4)
ttk.Label(root, text="Export to a .TXT file").grid(
    column=2, row=5)
ttk.Button(root, text="Save as...").grid(
    column=2, row=6)

# Logging window
# Create a passthrough function for logging
# Format: [time_and_date] Message
# Classes: Notification (black), Warning (yellow), Error (red, bold)
log = Text(root, width=40, height=5, background="white",
           wrap="none", state="disabled")
log.grid(columnspan=3, row=7, sticky=(N, S, E, W), padx=10, pady=10)
ys = ttk.Scrollbar(log, orient='vertical', command=log.yview)
xs = ttk.Scrollbar(log, orient='horizontal', command=log.xview)
log['yscrollcommand'] = ys.set
log['xscrollcommand'] = xs.set

root.mainloop()

''' UI MODEL:
                                  - MENU BAR -
+----------------------------------------------------------------------------+
| Draw on the canvas to set points.                                          |
| +--------------------------------------------+    Click to generate the    |
| |                                            | distances and the Hamilton- |
| |                                            | Matrix. This can take a few |
| |                                            |  moments, depending on the  |
| |                                            |  number of vertices drawn.  |
| |                                            |                             |
| |                - CANVAS -                  |        [ Generate ]         |
| |                                            |   Generated matrix: -NAME-  | ROWS: 7
| |                                            |                             |
| |                                            |    Export to a .TXT-file    |
| |                                            |                             |
| |                                            |       [ Save as... ]        |
| +--------------------------------------------+                             |
| +------------------------------------------------------------------------+ |
| |                            - LOG WINDOW -                              | |
| +------------------------------------------------------------------------+ |
+----------------------------------------------------------------------------+
                                   COLUMNS: 2
'''
