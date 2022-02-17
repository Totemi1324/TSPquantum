from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from base64 import b64encode

from modules import GraphCanvas, LogWindow

class GraphToHMatrix:
    global DESC_PADDING
    DESC_PADDING = 30

    def __init__(self, root):
        # Basic options
        self._root = root
        self._root.title("Graph to Matrix - TSPQ")
        self._root.option_add('*tearOff', FALSE)
        self._generated = StringVar(value="Generated: - n.a. -")

        # Create menu bar
        menubar = Menu(self._root)
        root['menu'] = menubar
        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Edit')
        menu_file.add_command(label='Clear', command=self._clearCanvas)
        menu_file.add_command(label='Open...', command=self._openFile)
        menu_file.add_command(label='Exit', command=self._exitProgram)
        menu_edit.add_command(label='Undo', command=self._undo)
        menu_edit.add_command(label='Redo', command=self._redo)

        # Title
        ttk.Label(self._root, text="Draw on the canvas to set vertices.").grid(column=1, row=1, sticky=W)

        # Logging window
        self._log = LogWindow(self._root, width=40, height=5, background="white", wrap="none", state="normal")
        # Canvas
        self._c = GraphCanvas(self._root, self._log, width=500, height=350, background="white")

        # Labels and buttons
        ttk.Label(self._root, text="Click to generate the distances\nand the Hamilton matrix.\nThis can take a few moments,\ndepending on the number of\nvertices drawn.", justify="center").grid(column=2, row=2, padx=DESC_PADDING)
        ttk.Button(self._root, text="Generate", command=self._generateHamiltonian).grid(column=2, row=3)
        ttk.Label(self._root, textvariable=self._generated).grid(column=2, row=4)
        ttk.Button(self._root, text="Save Hamiltonian...", command=self._saveHamil).grid(column=2, row=5)
        ttk.Button(self._root, text="Save Config...", command=self._saveConfig).grid(column=2, row=6)

        self._log.insertToGrid()
        # Key bindings and shortcuts
        self._root.bind_all("<Control-z>", self._undo)
        self._root.bind_all("<Control-y>", self._redo)

    def _generateHamiltonian(self):
        self._log.logMsg("Generating Hamiltonian...", "warning")

    def _saveHamil(self):
        pass

    def _saveConfig(self):
        if len(self._c) == 0:
            self._log.logMsg("Unable to save configuration file. No vertices set (%d)" % len(self._c), "error")
            return
        
        filename = filedialog.asksaveasfilename(defaultextension=".config", filetypes=(("Configuration File", "*.config"),("All Files", "*.*"))) 
        if not filename:
            self._log.logMsg("Unable to save configuration file. No save location specified", "error")
            return
        self._log.logMsg("Saving configuration file in: {0}".format(filename))
        vertices = self._c.getStackSnapshot()
        content = str(b64encode(vertices.stringify().encode("utf-8")), "utf-8")
        f = open(filename, "w")
        f.write(content)
        f.close()
        self._log.logMsg("Saving complete!")
        
    
    # Menubar functions
    def _clearCanvas(self):
        for _ in range(len(self._c)):
            self._c.deleteLast()

    def _openFile(self):
        pass

    def _exitProgram(self):
        self._root.destroy()

    def _undo(self, e=None):
        self._c.deleteLast()

    def _redo(self, e=None):
        self._c.restoreLast()
    

if __name__ == "__main__":
    root = Tk()
    window = GraphToHMatrix(root)
    root.mainloop()

# Export with: pyinstaller.exe --onefile --icon=myicon.ico main.py
# Base64 encode/decode: https://www.base64encoder.io/python/
