
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=25, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            self.create_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, width=5, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, pady=2)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, char)

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
