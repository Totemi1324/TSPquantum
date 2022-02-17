from tkinter import *
from tkinter import ttk

'''Definition of custom stack object'''

class Empty(Exception):
    pass


class VertexStack:
    class _Element:
        def __init__(self, data):
            if len(data) != 5:
                raise ValueError("Invalid data entry. Expected structure: [line1, line2, text, x, y]")
            self._data = data
        def __str__(self):
            return "(L1: {0} L2: {1}, T: {2}, X: {3}, Y: {4})".format(self._data[0], self._data[1], self._data[2], self._data[3], self._data[4])
        def get(self):
            return self._data


    def __init__(self): 
        self._data = [] 
    def __len__(self): 
        return len(self._data) 
    def is_empty(self): 
        return len(self._data) == 0 
    def push(self, d):
        self._data.append(self._Element(d))
    def top(self): 
        if self.is_empty(): 
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self): 
        if self.is_empty(): 
            return None
        d = self._data[-1].get()
        self._data.pop()
        return d
    def stringify(self):
        result = ""
        for d in self._data:
            c = d.get()
            result += str(c[3]) + " " + str(c[4]) + "\n"
        return result
