import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display
        self.display = tk.Entry(master, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create the buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            "7", "8", "9", "*",
            "4", "5", "6", "/",
            "1", "2", "3", "+",
            "0", ".", "=", "-"
        ]

        for i, button in enumerate(buttons):
            cmd = lambda x=button: self.button_click(x)
            tk.Button(self.master, text=button, padx=40, pady=20, command=cmd).grid(row=i // 4 + 1, column=i % 4)

    def button_click(self, button):
        if button == "=":
            # Evaluate the expression and display the result
            result = eval(self.display.get())
            self.display.delete(0, "end")
            self.display.insert(0, result)
        elxif button == "C":
            # Clear the display
            self.display.delete(0, "end")
        else:
            # Add the button text to the display
            self.display.insert("end", button)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()