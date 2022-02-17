from tkinter import *
from tkinter import ttk
from datetime import datetime

from datastructs import VertexStack


class GraphCanvas(Canvas):
    _CROSS_SIZE = 7
    _LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, parent, log, **kwargs):
        super().__init__(parent, **kwargs)
        self.grid(column=1, rowspan=5, sticky=(N, S, E, W))
        self.create_rectangle(4, 4, 500, 350, outline="dim gray", width=2, fill="white")
        self.bind("<Button-1>", self.addVertex)
        self.bind("<Control-z>", self.deleteLast)
        self._log = log

        self._vertex_count = 0
        self._vertices = VertexStack()
        self._last_action = []

    def addVertex(self, event):
        x, y = event.x, event.y
        if self._vertex_count >= len(self._LABELS):
            self._log.logMsg("ERROR: Maximum number of vertices (%d) reached! Last entry will not be saved." % len(self._LABELS), "error")
            return
        l1 = self.create_line((x-self._CROSS_SIZE, y, x+self._CROSS_SIZE, y), fill="red", width=3)
        l2 = self.create_line((x, y-self._CROSS_SIZE, x, y+self._CROSS_SIZE), fill="red", width=3)
        t = self.create_text((x+self._CROSS_SIZE, y-self._CROSS_SIZE), text=self._LABELS[self._vertex_count], anchor="sw", font="TkMenuFont", fill="dim gray")
        
        self._log.logMsg("Added vertex at: x = {0}, y = {1}".format(x, y))
        if self._vertex_count == 8:
            self._log.logMsg("Computational limit of D-Wave 2000Q (8) exceeded. Are you sure you want to add more vertices?", "warning")
        self._vertices.push([l1, l2, t, x, y])
        self._vertex_count += 1
    
    def deleteLast(self):
        d = self._vertices.pop()
        if not d:
            self._log.logMsg("Cannot perform undo action. Canvas already empty", "warning")
            return
        self._last_action = d[:]
        
        self.delete(d[0])
        self.delete(d[1])
        self.delete(d[2])
        self._vertex_count -= 1

    def restoreLast(self):
        if len(self._last_action) == 0:
            return

        x, y = self._last_action[3], self._last_action[4]
        l1 = self.create_line((x-self._CROSS_SIZE, y, x+self._CROSS_SIZE, y), fill="red", width=3)
        l2 = self.create_line((x, y-self._CROSS_SIZE, x, y+self._CROSS_SIZE), fill="red", width=3)
        t = self.create_text((x+self._CROSS_SIZE, y-self._CROSS_SIZE), text=self._LABELS[self._vertex_count], anchor="sw", font="TkMenuFont", fill="dim gray")
        
        self._vertices.push([l1, l2, t, x, y])
        self._vertex_count += 1
        self._last_action = []

    def getStackSnapshot(self):
        return self._vertices
    
    def __len__(self):
        return len(self._vertices)
        
    

class LogWindow(Text):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Configure tags
        self.tag_configure("warning", foreground="#e0ba1f")
        self.tag_configure("error", foreground="#e0291f")
        self.tag_configure("notification", foreground="black")

        self.insert('end', "--- GRAPH TO MATRIX - TSPQ (v.1.0.0) ---\n")
        self.insert('end', "[" + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "] START LOG")

        self['state'] = "disabled"
    
    def insertToGrid(self):
        self.grid(columnspan=3, row=7, sticky=(N, S, E, W), padx=10, pady=10)

    def logMsg(self, msg, msg_type="notification"):
        msg_types = ["notification", "warning", "error"]
        if msg_type not in msg_types:
            raise ValueError("Invalid message type. Expected one of: %s" % msg_types)

        numlines = int(self.index('end - 1 line').split('.')[0])
        self['state'] = 'normal'
        if numlines == 24:
            self.delete(1.0, 2.0)
        if self.index('end-1c') != '1.0':
            self.insert('end', '\n')

        self.insert('end', "[" + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "] " + msg, (msg_type))
        self.see('end')
        self['state'] = 'disabled'


if __name__ == "__main__":
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    gc = GraphCanvas(root, None)
    gc.grid(column=0, row=0, sticky=(N, W, E, S))

    root.mainloop()
