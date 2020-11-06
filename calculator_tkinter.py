import tkinter as tk
from math import *

# Light gray buttom parameters
b_pr = {
    'padx': 16,
    'pady': 4,
    'bd': 4,
    'fg': '#738678',
    'bg': '#CFCFCF',
    'font': ('graduate', 16),
    'width': 2,
    'height': 2,
    'relief': 'flat',
}

# Dark gray buttom parameters
n_pr = {
    'padx': 16,
    'pady': 4,
    'bd': 4,
    'fg': '#738678',
    'bg': '#4d4d4d',
    'font': ('graduate', 16),
    'width': 2,
    'height': 2,
    'relief': 'flat',
}


class calc:
    def __init__(self, master):
        self.expression = ""
        self.text_input = tk.StringVar()
        self.master = master

        top_frame = tk.Frame(master, bg='#666666', bd=2, relief='flat')
        top_frame.pack(side=tk.TOP)

        bottom_frame = tk.Frame(master, bd=2, relief='flat', bg='#666666')
        bottom_frame.pack(side=tk.BOTTOM)

        my_item = tk.Label(top_frame,
                           text="Minimum Numbers", font=('graduate', 10),
                           fg='#F4F0EC', width=16, bg='#666666')
        my_item.pack()

        txt_display = tk.Entry(
            top_frame, font=('graduate', 18), relief='flat',
            bg='#666666', fg='#F4F0EC', textvariable=self.text_input,
            width=100, bd=12, justify='right')
        txt_display.pack()

        self.btn_clear = tk.Button(
            bottom_frame, b_pr, text="C", command=self.btn_clear_all)
        self.btn_clear.grid(row=0, column=0)

        self.btn_delete = tk.Button(
            bottom_frame, b_pr, text="D", command=self.btn_clear1)
        self.btn_delete.grid(row=0, column=1)

        self.btn_left_bracket = tk.Button(
            bottom_frame, b_pr, text="(", command=lambda: self.btn_click('('))
        self.btn_left_bracket.grid(row=0, column=2)

        self.btn_right_bracket = tk.Button(
            bottom_frame, b_pr, text=")", command=lambda: self.btn_click(')'))
        self.btn_right_bracket.grid(row=0, column=3)

        self.btn_div = tk.Button(
            bottom_frame, b_pr, text="÷", command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=0, column=4)

        self.btn_sqrt = tk.Button(
            bottom_frame, b_pr, text="√",
            command=lambda: self.btn_click('sqrt('))
        self.btn_sqrt.grid(row=1, column=0)

        self.btn_7 = tk.Button(
            bottom_frame, n_pr, text="7", command=lambda: self.btn_click(7))
        self.btn_7.grid(row=1, column=1)

        self.btn_8 = tk.Button(
            bottom_frame, n_pr, text="8", command=lambda: self.btn_click(8))
        self.btn_8.grid(row=1, column=2)

        self.btn_9 = tk.Button(
            bottom_frame, n_pr, text="9", command=lambda: self.btn_click(9))
        self.btn_9.grid(row=1, column=3)

        self.btn_multiply = tk.Button(
            bottom_frame, b_pr, text="×", command=lambda: self.btn_click('*'))
        self.btn_multiply.grid(row=1, column=4)

        self.btn_power = tk.Button(
            bottom_frame, b_pr, text="x^y",
            command=lambda: self.btn_click('**'))
        self.btn_power.grid(row=2, column=0)

        self.btn_4 = tk.Button(
            bottom_frame, n_pr, text="4", command=lambda: self.btn_click(4))
        self.btn_4.grid(row=2, column=1)

        self.btn_5 = tk.Button(
            bottom_frame, n_pr, text="5", command=lambda: self.btn_click(5))
        self.btn_5.grid(row=2, column=2)

        self.btn_6 = tk.Button(
            bottom_frame, n_pr, text="6", command=lambda: self.btn_click(6))
        self.btn_6.grid(row=2, column=3)

        self.btnSub = tk.Button(
            bottom_frame, b_pr, text="-", command=lambda: self.btn_click('-'))
        self.btnSub.grid(row=2, column=4)

        self.btn_sqr = tk.Button(
            bottom_frame, b_pr, text=u"x\u00B2",
            command=lambda: self.btn_click('**2'))
        self.btn_sqr.grid(row=3, column=0)

        self.btn_1 = tk.Button(
            bottom_frame, n_pr, text="1", command=lambda: self.btn_click(1))
        self.btn_1.grid(row=3, column=1)

        self.btn_2 = tk.Button(
            bottom_frame, n_pr, text="2", command=lambda: self.btn_click(2))
        self.btn_2.grid(row=3, column=2)

        self.btn_3 = tk.Button(
            bottom_frame, n_pr, text="3", command=lambda: self.btn_click(3))
        self.btn_3.grid(row=3, column=3)

        self.btn_add = tk.Button(
            bottom_frame, b_pr, text="+", command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=3, column=4)

        self.cube = tk.Button(
            bottom_frame, b_pr, text=u"x\u00B3",
            command=lambda: self.btn_click('**3'))
        self.cube.grid(row=4, column=0)

        self.btn_0 = tk.Button(
            bottom_frame, n_pr, text="0          ",
            command=lambda: self.btn_click(0))
        self.btn_0.configure(width=7)
        self.btn_0.grid(row=4, column=1, columnspan=2)

        self.btn_dec = tk.Button(
            bottom_frame, b_pr, text=".", command=lambda: self.btn_click('.'))
        self.btn_dec.grid(row=4, column=3)

        self.btn_eq = tk.Button(
            bottom_frame, b_pr, text="=", command=self.btn_equal)
        self.btn_eq.grid(row=4, column=4)

    def btn_click(self, expression_val):
        if len(self.expression) >= 21:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)

    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up


root = tk.Tk()
root.title("Calculator")
root.geometry("364x460+80+80")
root.resizable(False, False)

calc(root)
root.mainloop()
