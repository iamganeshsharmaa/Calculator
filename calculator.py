import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


app = tk.Tk()
app.title("Simple Calculator")


entry = tk.Entry(app, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]


row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(app, text=button, padx=40, pady=20, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(app, text=button, padx=40, pady=20, command=clear_entry).grid(row=row, column=col)
    else:
        tk.Button(app, text=button, padx=40, pady=20, command=lambda value=button: button_click(value)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1


app.mainloop()
