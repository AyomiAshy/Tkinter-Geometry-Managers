# Import tkinter
import tkinter as tk
# Setup the window
window = tk.Tk()
# Title
window.title("Number Pad")
# Height and width
window.geometry("300x400")
# Create a function to display the numbers
def button_click(number):
    entry.insert(tk.END, str(number))
def clear_entry():
    entry.delete(0, tk.END)
def call_action(action):
    number = entry.get()
    print(f"Calling {number}")
    entry.delete(0, tk.END)
def create_button_click_handler(num):
    def handler():
        button_click(num)
    return handler
# Create the widgets
entry = tk.Entry(window, font=("Arial", 24), justify='center')
entry.grid(row = 0, column = 0, columnspan = 3, pady = 10, padx = 10)
# Number Pad
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '*', '0', '#',
    ]
for index, button in enumerate(buttons):
    row_val = (index // 3) + 1
    col_val = index % 3
    btn = tk.Button(window, text=button, font=("Arial", 18), width = 5, height = 2, command = create_button_click_handler(button))
    btn.grid(row = row_val, column = col_val, padx= 5, pady= 5)
# Clear Button
tk.Button(window, text='Clear', font=("Arial", 18), width = 10, command=clear_entry).grid(row=4, column=0, columnspan=3, pady=10)
tk.Button(window, text='Call', font=("Arial", 18), width = 10, command = call_action).grid(row=5, column=0, columnspan=3, pady=10)
# Run Application
window.mainloop()