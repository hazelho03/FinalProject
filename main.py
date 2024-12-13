import tkinter as tk
from tkinter import messagebox
import csv
import view

def main():
    root = tk.Tk()
    root.title("Score Calculator")
    view.cal_avg()
    root.mainloop()

if __name__ == '__main__':
    main()