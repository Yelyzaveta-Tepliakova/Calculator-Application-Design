#####################################################################
## Description:    The program makes GUI for calculator that does
##                 basic arithmetic calculations.
#####################################################################
## Author:         Yelyzaveta Tepliakova
## Python version: 3.8.
## Date:           09.01.2020
#####################################################################

import tkinter as tk

class Calculator():

    def __init__(self):
        """
        The function sets calculator's size and title
        """
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry('200x520')
        self.task = ""
        self.widget_formula = ""
        self.formula = ""
        self.root.resizable(False, False)


    def Calculation(self, text):
        """
        The method makes all mathematical operations that
        can be used in calculator
        """
        if text.isdigit() or text == "\n-\n"\
                or text == "." and len(self.formula) != 0 \
                or text == "\n+\n" and len(self.formula) != 0 \
                or text == "\n*\n" and len(self.formula) != 0\
                or text == "\n/\n" and len(self.formula) != 0\
                or text == "=" and len(self.formula) != 0\
                or text == "√" and len(self.formula) != 0\
                or text == "^2" and len(self.formula) != 0\
                or text == "C" or text == "AC":
            # checks if symbols which are entered are digits and
            # appropriate mathematical operators and does not
            # allow to put mathematical operators at the beginning,
            # except of "-"

            if text == "\n-\n" and len(self.formula) == 0:
                                    # allows to put negative number
                text = text.replace("\n", "")

            if text == "√":   # counts nth root of a number
                if "\n+\n" not in self.formula and\
                    "\n-\n" not in self.formula and\
                    "\n*\n" not in self.formula and\
                    "\n/\n" not in self.formula:
                    # does not allow to put nth root of a number
                    # during counting
                    if self.formula[0] != "-":
                        self.formula = \
                            eval(self.formula + "**0.5")
                        self.formula = str(self.formula)

            elif text == "^2":   # counts square of a number
                if "\n+\n" not in self.formula and\
                    "\n-\n" not in self.formula and\
                    "\n*\n" not in self.formula and\
                    "\n/\n" not in self.formula:
                    # does not allow to put square of a number
                    # during counting
                    if self.formula[0] == "-":
                        self.formula = self.formula[1:]
                        self.formula = \
                            eval(self.formula + "**2")
                        self.formula = str(self.formula)

                    else:
                        self.formula = \
                            eval(self.formula + "**2")
                        self.formula = str(self.formula)

            elif text == "AC":   # all clear (clears the whole
                                 # formula)
                self.formula = ""

            elif text == "C":   # clears last symbol
                if len(self.formula) == 0:
                                          # clears the whole
                                          # formula
                                          # if there are no symbols
                                          # in the formula
                    self.formula = ""

                elif len(self.formula) != 0:
                                            # clears last symbol in
                                            # the formula
                                            # if formula
                                            # is not empty
                    if "\n" in self.formula:
                        self.formula = \
                            self.formula.replace("\n", "")
                    self.formula = self.formula[:-1]

                    if "+" or "-" or "*" or "/" \
                            in self.formula:
                        # while clearing last symbol makes
                        # mathematical operators to stay
                        # on the next string
                        self.formula =\
                            "\n+\n".join(self.formula.rsplit
                                                 ("+", 100))
                        self.formula =\
                            "\n-\n".join(self.formula.rsplit
                                                 ("-", 100))
                        self.formula =\
                            "\n*\n".join(self.formula.rsplit
                                                 ("*", 100))
                        self.formula =\
                            "\n/\n".join(self.formula.rsplit
                                                 ("/", 100))

            else:   # counts if symbols are digits,
                    # "+", "-", "*", "/", ".", "="
                if len(self.formula) == 1 and \
                        self.formula[0] == "0":
                                    # checks if there is zero at
                                    # the begining of formula
                    if text == "\n+\n" or text == "\n-\n" \
                        or text == "\n*\n0" or text == "\n/\n0":
                        self.formula += text

                    if text == "0":   # does not allow to put zero
                                      # if the first digit in
                                      # formula is zero
                        pass

                    elif text == ".":   # allows to put point after
                                        # first zero which means
                                        # decimal fraction
                        self.formula += text

                        if text == "=":
                            if "\n" in self.formula:
                                self.formula = \
                                    self.formula.\
                                        replace("\n","")
                                self.formula = \
                                    str(eval(self.
                                             formula[:-1]))

                else:   # puts digits, mathematical operator
                        # and point
                    if text == "\n+\n" or text == "\n-\n" \
                            or text == "\n*\n" or text == "\n/\n":
                        # checks if the symbol is "+", "-", "*", "/"

                        if len(self.formula) > 2 and \
                                self.formula[-2] == "+":
                            # does not allow to put mathematical
                            # operator after "+"
                            self.formula = \
                                self.formula[:-3]
                            self.formula += text

                        elif len(self.formula) > 2 and \
                                self.formula[-2] == "-":
                            # does not allow to put mathematical
                            # operator after "-"
                            self.formula = \
                                self.formula[:-3]
                            self.formula += text

                        elif len(self.formula) > 2 and \
                                self.formula[-2] == "*":
                            # does not allow to put mathematical
                            # operator after "*"
                            self.formula = \
                                self.formula[:-3]
                            self.formula += text

                        elif len(self.formula) > 2 and \
                                self.formula[-2] == "/":
                            # does not allow to put mathematical
                            # operator after "/"
                            self.formula = \
                                self.formula[:-3]
                            self.formula += text

                        else:
                            # allows to put mathematical operators
                            # after digits
                            self.formula += text

                    else:   #allows to put digits in formula
                        self.formula += text

                        if text == "=":
                            if "\n" in self.formula:
                                self.formula = \
                                    self.formula.\
                                        replace("\n", "")
                                self.formula = \
                                    str(eval(self.
                                             formula[:-1]))


    def ShowInWidget(self, text):
        """
        The method puts digits and mathematical operators into
        Entry Widget
        """
        if text.isdigit() or text == "\n-\n"\
                or text == "." and len(self.widget_formula) != 0 \
                or text == "\n+\n" and len(self.widget_formula) != 0 \
                or text == "\n*\n" and len(self.widget_formula) != 0\
                or text == "\n/\n" and len(self.widget_formula) != 0\
                or text == "=" and len(self.widget_formula) != 0\
                or text == "√" and len(self.widget_formula) != 0\
                or text == "^2" and len(self.widget_formula) != 0\
                or text == "C" or text == "AC":
            # checks if symbols which are entered are digits and
            # appropriate mathematical operators and does not
            # allow to put mathematical operators at the beginning,
            # except of "-"

            if text == "\n-\n" and len(self.widget_formula) == 0:
                                    # allows to put negative number
                text = text.replace("\n", "")

            if text == "√":   # counts nth root of a number
                self.TextEntry.delete(1.0, tk.END)
                self.TextEntry.insert(2.0, self.formula)

            elif text == "^2":   # counts square of a number
                self.TextEntry.delete(1.0, tk.END)
                self.TextEntry.insert(2.0, self.formula)

            elif text == "AC":   # all clear (clears the whole
                                 # widget_formula)
                self.widget_formula = ""

            elif text == "C":   # clears last symbol
                if len(self.widget_formula) == 0:
                                          # clears the whole
                                          # widget_formula
                                          # if there are no symbols
                                          # in the widget_formula
                    self.widget_formula = ""

                elif len(self.widget_formula) != 0:
                                            # clears last symbol in
                                            # the widget_formula
                                            # if widget_formula
                                            # is not empty
                    self.TextEntry.delete(1.0, tk.END)
                    self.widget_formula = self.formula

                    if "+" or "-" or "*" or "/" \
                            in self.widget_formula:
                        # while clearing last symbol makes
                        # mathematical operators to stay
                        # on the next string
                        self.TextEntry.insert(1.0,
                                              self.formula)

            else:   # counts if symbols are digits,
                    # "+", "-", "*", "/", ".", "="
                if len(self.widget_formula) == 1 and \
                        self.widget_formula[0] == "0":
                                    # checks if there is zero at
                                    # the begining of widget_formula
                    if text == "\n+\n" or text == "\n-\n" \
                        or text == "\n*\n0" or text == "\n/\n0":
                        self.TextEntry.insert(300.0, text)
                        self.widget_formula += text

                    if text == "0":   # does not allow to put zero
                                      # if the first digit in
                                      # widget_formula is zero
                        pass

                    elif text == ".":   # allows to put point after
                                        # first zero which means
                                        # decimal fraction
                        self.TextEntry.insert(300.0, text)
                        self.widget_formula += text

                        if text == "=":
                            if "\n" in self.widget_formula:
                                self.TextEntry.delete(1.0, tk.END)
                                self.TextEntry.insert(2.0, self.
                                                      formula)

                else:   # puts digits, mathematical operator
                        # and point
                    if text == "\n+\n" or text == "\n-\n" \
                            or text == "\n*\n" or text == "\n/\n":
                        # checks if the symbol is "+", "-", "*", "/"

                        if len(self.widget_formula) > 2 and \
                                self.widget_formula[-2] == "+":
                            # does not allow to put mathematical
                            # operator after "+"
                            self.TextEntry.delete(1.0, tk.END)
                            self.TextEntry.insert(300.0,
                                                  self.
                                                  formula)

                        elif len(self.widget_formula) > 2 and \
                                self.widget_formula[-2] == "-":
                            # does not allow to put mathematical
                            # operator after "-"
                            self.TextEntry.delete(1.0, tk.END)
                            self.TextEntry.insert(300.0,
                                                  self.
                                                  formula)

                        elif len(self.widget_formula) > 2 and \
                                self.widget_formula[-2] == "*":
                            # does not allow to put mathematical
                            # operator after "*"
                            self.TextEntry.delete(1.0, tk.END)
                            self.TextEntry.insert(300.0,
                                                  self.
                                                  formula)

                        elif len(self.widget_formula) > 2 and \
                                self.widget_formula[-2] == "/":
                            # does not allow to put mathematical
                            # operator after "/"
                            self.TextEntry.delete(1.0, tk.END)
                            self.TextEntry.insert(300.0,
                                                  self.
                                                  formula)

                        else:
                            # allows to put mathematical operators
                            # after digits
                            self.TextEntry.insert(300.0, text)
                            self.widget_formula += text

                    else:   #allows to put digits in widget_formula
                        self.TextEntry.insert(300.0, text)
                        self.widget_formula += text

                        if text == "=":
                            if "\n" in self.widget_formula:
                                self.TextEntry.delete(1.0, tk.END)
                                self.TextEntry.insert(2.0,
                                                      self.
                                                      formula)


    def InitCalculator(self):
        """
        The function sets Entry Widget's size; also sets buttons'
        size, location, design and functions
        """
        self.TextEntry = tk.Text(self.root, height=11,
                                            width=30,
                                            font='50')
                            # sets Entry Widget's size
        self.TextEntry.bind("<Key>", lambda e: "break")
                     # disables any input from keyboard
        self.TextEntry.pack()

        button_zero = tk.Button(self.root, text="0",
                                           bg="black",
                                           fg="white",
                                           font="50",
                           command=lambda: (self.Calculation("0"),
                                            self.ShowInWidget("0")))
        button_zero.place(x = 0, y = 470, height = 50, width = 50)

        button_one = tk.Button(self.root, text="1",
                                          bg="black",
                                          fg="white",
                                          font="50",
                  command=lambda: (self.Calculation("1"),
                                   self.ShowInWidget("1")))
        button_one.place(x=0, y=420, height=50, width=50)

        button_two = tk.Button(self.root, text="2",
                                          bg="black",
                                          fg="white",
                                          font='50',
                   command=lambda: (self.Calculation("2"),
                                   self.ShowInWidget("2")))
        button_two.place(x=50, y=420, height=50, width=50)

        button_three = tk.Button(self.root, text='3',
                                            bg="black",
                                            fg="white",
                                            font='50',
                      command=lambda: (self.Calculation("3"),
                                   self.ShowInWidget("3")))
        button_three.place(x=100, y=420, height=50, width=50)

        button_four = tk.Button(self.root, text='4',
                                           bg="black",
                                           fg="white",
                                           font='50',
                   command=lambda: (self.Calculation("4"),
                                   self.ShowInWidget("4")))
        button_four.place(x=0, y=370, height=50, width=50)

        button_five = tk.Button(self.root, text='5',
                                           bg="black",
                                           fg="white",
                                           font='50',
                    command=lambda: (self.Calculation("5"),
                                   self.ShowInWidget("5")))
        button_five.place(x=50, y=370, height=50, width=50)

        button_six = tk.Button(self.root, text='6',
                                          bg="black",
                                          fg="white",
                                          font='50',
                    command=lambda: (self.Calculation("6"),
                                   self.ShowInWidget("6")))
        button_six.place(x=100, y=370, height=50, width=50)

        button_seven = tk.Button(self.root, text='7',
                                            bg="black",
                                            fg="white",
                                            font='50',
                    command=lambda: (self.Calculation("7"),
                                   self.ShowInWidget("7")))
        button_seven.place(x=0, y=320, height=50, width=50)

        button_eight = tk.Button(self.root, text='8',
                                            bg="black",
                                            fg="white",
                                            font='50',
                     command=lambda: (self.Calculation("8"),
                                   self.ShowInWidget("8")))
        button_eight.place(x=50, y=320, height=50, width=50)

        button_nine = tk.Button(self.root, text='9',
                                           bg="black",
                                           fg="white",
                                           font='50',
                     command=lambda: (self.Calculation("9"),
                                   self.ShowInWidget("9")))
        button_nine.place(x=100, y=320, height=50, width=50)

        button_point = tk.Button(self.root, text='.',
                                            bg="black",
                                            fg="white",
                                            font='50',
                     command=lambda: (self.Calculation("."),
                                   self.ShowInWidget(".")))
        button_point.place(x=50, y=470, height=50, width=50)

        button_addition = tk.Button(self.root, text='+',
                                               bg="orange",
                                               fg="black",
                                               font='50',
                     command=lambda: (self.Calculation("\n+\n"),
                                   self.ShowInWidget("\n+\n")))
        button_addition.place(x=150, y=320, height=50, width=50)

        button_subtraction = tk.Button(self.root, text = '-',
                                                  bg="orange",
                                                  fg="black",
                                                  font='50',
                         command=lambda: (self.Calculation("\n-\n"),
                                   self.ShowInWidget("\n-\n")))
        button_subtraction.place(x=150, y=370, height=50, width=50)

        button_division = tk.Button(self.root, text = '/',
                                               bg="orange",
                                               fg="black",
                                               font='50',
                      command=lambda: (self.Calculation("\n/\n"),
                                   self.ShowInWidget("\n/\n")))
        button_division.place(x=150, y=470, height=50, width=50)

        button_multiplication = tk.Button(self.root, text = '*',
                                                     bg="orange",
                                                     fg="black",
                                                     font='50',
                            command=lambda: (self.Calculation("\n*\n"),
                                   self.ShowInWidget("\n*\n")))
        button_multiplication.place(x=150, y=420, height=50, width=50)

        button_square_root = tk.Button(self.root, text = '√',
                                                  bg="orange",
                                                  fg="black",
                                                  font='50',
                         command = lambda: (self.Calculation("√"),
                                   self.ShowInWidget("√")))
        button_square_root.place(x=100, y=270, height=50, width=50)

        button_square = tk.Button(self.root, text = '^2',
                                             bg="orange",
                                             fg="black",
                                             font='50',
                    command = lambda: (self.Calculation("^2"),
                                   self.ShowInWidget("^2")))
        button_square.place(x=150, y=270, height=50, width=50)

        button_equals = tk.Button(self.root, text = '=',
                                             bg="black",
                                             fg="white",
                                             font='50',
                       command=lambda: (self.Calculation("="),
                                   self.ShowInWidget("=")))
        button_equals.place(x=100, y=470, height=50, width=50)

        button_delete_all = tk.Button(self.root, text = 'AC',
                                                 bg="orange",
                                                 fg="black",
                                                 font='50',
                        command=lambda: (self.Calculation("AC"),
                                         self.ShowInWidget("AC"),
                            self.TextEntry.delete(1.0, tk.END)))
        button_delete_all.place(x=0, y=270, height=50, width=50)

        button_delete = tk.Button(self.root, text = 'C',
                                             bg="orange",
                                             fg="black",
                                             font='50',
                    command = lambda: (self.Calculation("C"),
                                   self.ShowInWidget("C")))
        button_delete.place(x=50, y=270, height=50, width=50)

if __name__ == "__main__":
    main = Calculator()
    main.InitCalculator()
    main.root.mainloop()

