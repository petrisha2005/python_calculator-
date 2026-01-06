import tkinter as tk
from tkinter import messagebox
import math
import os

HISTORY_FILE = "history.txt"

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Ultimate Python GUI Calculator")
root.minsize(800, 650)

# ---------------- THEME ----------------
dark_mode = False

def apply_theme():
    bg = "#1e1e1e" if dark_mode else "#f2f2f2"
    fg = "#ffffff" if dark_mode else "#000000"
    root.configure(bg=bg)
    for widget in root.winfo_children():
        try:
            widget.configure(bg=bg, fg=fg)
        except:
            pass

# ---------------- MEMORY ----------------
memory = 0

# ---------------- HISTORY ----------------
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            for line in f:
                history_box.insert(tk.END, line.strip())

def save_history(text):
    with open(HISTORY_FILE, "a") as f:
        f.write(text + "\n")

# ---------------- INPUT ----------------
entry = tk.Entry(root, font=("Arial", 18))
entry.pack(fill="x", padx=10, pady=10)

result_label = tk.Label(root, text="Result:", font=("Arial", 16))
result_label.pack(pady=5)

# ---------------- HISTORY BOX ----------------
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

history_box = tk.Listbox(frame, font=("Arial", 13), yscrollcommand=scroll.set)
history_box.pack(fill="both", expand=True)
scroll.config(command=history_box.yview)

# ---------------- CORE FUNCTIONS ----------------
def update_result(text):
    result_label.config(text=f"Result: {text}")
    history_box.insert(tk.END, text)
    save_history(text)

def evaluate_expression():
    try:
        expr = entry.get()
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        update_result(f"{expr} = {result}")
    except:
        messagebox.showerror("Error", "Invalid expression")

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")

# ---------------- MEMORY FUNCTIONS ----------------
def memory_add():
    global memory
    memory += float(entry.get())

def memory_sub():
    global memory
    memory -= float(entry.get())

def memory_recall():
    entry.delete(0, tk.END)
    entry.insert(0, str(memory))

def memory_clear():
    global memory
    memory = 0

# ---------------- UNIT CONVERTER ----------------
def cm_to_m():
    try:
        v = float(entry.get())
        update_result(f"{v} cm = {v/100} m")
    except:
        messagebox.showerror("Error", "Invalid input")

def c_to_f():
    try:
        v = float(entry.get())
        update_result(f"{v}°C = {(v*9/5)+32}°F")
    except:
        messagebox.showerror("Error", "Invalid input")

# ---------------- DARK MODE ----------------
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

# ---------------- KEYBOARD SHORTCUTS ----------------
root.bind("<Return>", lambda e: evaluate_expression())
root.bind("<Control-l>", lambda e: clear())
root.bind("<Control-h>", lambda e: history_box.delete(0, tk.END))

# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

buttons = [
    ("Eval", evaluate_expression),
    ("√", lambda: entry.insert(tk.END, "math.sqrt(")),
    ("^", lambda: entry.insert(tk.END, "**")),
    ("Clear", clear),
    ("Dark Mode", toggle_theme),
    ("M+", memory_add),
    ("M-", memory_sub),
    ("MR", memory_recall),
    ("MC", memory_clear),
    ("cm→m", cm_to_m),
    ("°C→°F", c_to_f)
]

for i, (text, cmd) in enumerate(buttons):
    tk.Button(btn_frame, text=text, width=10, command=cmd).grid(row=i//4, column=i%4, padx=5, pady=5)

apply_theme()
load_history()
root.mainloop()
