import tkinter as tk
from src.base_auto_gui import BaseAutoGui

def main():
    root = tk.Tk()
    base_auto_gui = BaseAutoGui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
