import tkinter as tk
from tkinter import messagebox
import math

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if entry2.get() else 0

        if operation == 'add':
            result.set(num1 + num2)
        elif operation == 'subtract':
            result.set(num1 - num2)
        elif operation == 'multiply':
            result.set(num1 * num2)
        elif operation == 'divide':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result.set(num1 / num2)
        elif operation == 'square':
            result.set(num1 ** 2)
        elif operation == 'sqrt':
            if num1 < 0:
                messagebox.showerror("Error", "Cannot take square root of a negative number")
                return
            result.set(math.sqrt(num1))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Beautiful Tkinter Calculator")
root.geometry("350x360")
root.config(bg="#f0f0f0")

LABEL_FONT = ("Helvetica", 12)
ENTRY_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 10, "bold")

result = tk.StringVar()

tk.Label(root, text="Simple Calculator", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=5)

tk.Label(input_frame, text="First Number:", font=LABEL_FONT, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry1 = tk.Entry(input_frame, font=ENTRY_FONT, width=15)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Second Number:", font=LABEL_FONT, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry2 = tk.Entry(input_frame, font=ENTRY_FONT, width=15)
entry2.grid(row=1, column=1, padx=10, pady=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", font=BUTTON_FONT, bg="#4CAF50", fg="white", width=10,
          command=lambda: calculate('add')).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Subtract", font=BUTTON_FONT, bg="#2196F3", fg="white", width=10,
          command=lambda: calculate('subtract')).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Multiply", font=BUTTON_FONT, bg="#FF9800", fg="white", width=10,
          command=lambda: calculate('multiply')).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Divide", font=BUTTON_FONT, bg="#f44336", fg="white", width=10,
          command=lambda: calculate('divide')).grid(row=1, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Square", font=BUTTON_FONT, bg="#9C27B0", fg="white", width=10,
          command=lambda: calculate('square')).grid(row=2, column=0, padx=5, pady=5)
tk.Button(button_frame, text="√", font=BUTTON_FONT, bg="#00BCD4", fg="white", width=10,
          command=lambda: calculate('sqrt')).grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Result:", font=LABEL_FONT, bg="#f0f0f0").pack()
tk.Entry(root, textvariable=result, font=ENTRY_FONT, state='readonly', justify='center', width=20).pack(pady=5)

root.mainloop()
