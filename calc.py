import tkinter as tk
from tkinter import messagebox
import math

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Advanced Python GUI Calculator")
root.minsize(600, 600)

# allow resize
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# ---------- INPUTS ----------
num1 = tk.Entry(root, font=("Arial", 16))
num1.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

num2 = tk.Entry(root, font=("Arial", 16))
num2.grid(row=0, column=3, columnspan=3, padx=10, pady=10, sticky="nsew")

result_label = tk.Label(root, text="Result:", font=("Arial", 16))
result_label.grid(row=1, column=0, columnspan=6, pady=10)

# ---------- HISTORY ----------
history_frame = tk.Frame(root)
history_frame.grid(row=5, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

history_scroll = tk.Scrollbar(history_frame)
history_scroll.pack(side=tk.RIGHT, fill=tk.Y)

history_box = tk.Listbox(
    history_frame,
    font=("Arial", 13),
    yscrollcommand=history_scroll.set
)
history_box.pack(fill=tk.BOTH, expand=True)

history_scroll.config(command=history_box.yview)

# ---------- FUNCTIONS ----------
def update_result(text):
    result_label.config(text=f"Result: {text}")
    history_box.insert(tk.END, text)

def get_two():
    try:
        return float(num1.get()), float(num2.get())
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")
        return None, None

def add():
    a, b = get_two()
    if a is not None:
        update_result(f"{a} + {b} = {a+b}")

def sub():
    a, b = get_two()
    if a is not None:
        update_result(f"{a} - {b} = {a-b}")

def mul():
    a, b = get_two()
    if a is not None:
        update_result(f"{a} × {b} = {a*b}")

def div():
    a, b = get_two()
    if a is not None:
        if b == 0:
            messagebox.showerror("Error", "Division by zero")
            return
        update_result(f"{a} ÷ {b} = {a/b}")

def power():
    a, b = get_two()
    if a is not None:
        update_result(f"{a} ^ {b} = {a**b}")

def sqrt():
    try:
        a = float(num1.get())
        if a < 0:
            raise ValueError
        update_result(f"√{a} = {math.sqrt(a)}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid number")

def clear():
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    result_label.config(text="Result:")

# ---------- BUTTONS ----------
buttons = [
    ("+", add), ("-", sub), ("×", mul),
    ("÷", div), ("xʸ", power), ("√", sqrt),
    ("Clear", clear)
]

row, col = 2, 0
for text, cmd in buttons:
    btn = tk.Button(root, text=text, font=("Arial", 14), command=cmd)
    btn.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
    col += 1
    if col == 3:
        row += 1
        col = 0

root.mainloop()
