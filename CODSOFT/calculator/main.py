import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x600")
        self.master.resizable(False, False)

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry_frame = tk.Frame(self.master)
        entry_frame.pack(pady=20)

        entry = tk.Entry(entry_frame, textvariable=self.result_var, font=("Helvetica", 24), bd=10, insertwidth=4, width=14, justify="right")
        entry.grid(row=0, column=0, ipadx=8, ipady=8, columnspan=4)

        button_frame = tk.Frame(self.master)
        button_frame.pack()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(button_frame, text=button, padx=20, pady=20, font=("Helvetica", 18), command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button == 'C':
            self.result_var.set('')
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
