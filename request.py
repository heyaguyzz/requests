import tkinter
import inspect

print(inspect.ismodule(tkinter))  # True
tkinter_classes = [name for name, obj in inspect.getmembers(tkinter, inspect.isclass)]
print(tkinter_classes)
tkinter_functions = [name for name, obj in inspect.getmembers(tkinter, inspect.isfunction)]
print(tkinter_functions)
print(inspect.getmodule(tkinter.Tk))
print(inspect.signature(tkinter.Tk))
import sys
print('tkinter' in sys.modules)
print(sys.modules['tkinter'].__file__)
print(dir(tkinter))
