#####################################################################
## Description:    The program makes GUI for calculator that does
##                 basic arithmetic calculations.
#####################################################################
## Author:         Yelyzaveta Tepliakova
## Python version: 3.8.
## Date:           09.01.2020
#####################################################################
print("test print")
import tkinter as tk

class Calculator():

    def __init__(self):
        """
        The function sets calculator's size and title
        """
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry('200x400')
        self.task = ""


    def Calculation(self, text):
        """
        The method puts digits and mathematical operators into
        Entry Widget and makes all mathematical operations that
        can be used in calculator
        """


    def SetTextInput(self, text):
        """
        The function puts digits and mathematical operators into
        Entry Widget and makes all mathematical operations that
        can be used in calculator
        """

        if text.isdigit() or text == "." and len(self.task) != 0 \
                or text == "\n+\n" and len(self.task) != 0 \
                or text == "\n-\n" and len(self.task) != 0\
                or text == "\n*\n" and len(self.task) != 0\
                or text == "\n/\n" and len(self.task) != 0\
                or text == "=" and len(self.task) != 0\
                or text == "√" and len(self.task) != 0\
                or text == "^2" and len(self.task) != 0\
                or text == "C" or text == "AC":
            # checks if symbols in Entry Widget are digits and
            # appropriate mathematical operators

            if text == "√":   # counts nth root of a number

                self.task = eval(self.task + "**0.5")
                self.TextEntry.delete(1.0, tk.END)
                self.task = str(self.task)
                self.TextEntry.insert(2.0, self.task)

            elif text == "^2":   # counts square of a number

                self.task = eval(self.task + "**2")
                self.TextEntry.delete(1.0, tk.END)
                self.task = str(self.task)
                self.TextEntry.insert(2.0, self.task)

            elif text == "AC":   # all clear (clears the whole task)

                self.task = ""

            elif text == "C":   # clears last symbol

                if len(self.task) == 0:   # clears the whole task if there are
                                          # no symbols in task
                    self.task = ""

                elif len(self.task) != 0:   # clears last symbol in the task
                                            # if task is not empty
                    if "\n" in self.task:
                        self.task = self.task.replace("\n", "")

                    self.TextEntry.delete(1.0, tk.END)
                    self.task = self.task[:-1]

                    if "+" or "-" or "*" or "/" in self.task:
                        # while clearing last symbol makes mathematical
                        # operators to stay on the next string
                        self.task = "\n+\n".join(self.task.rsplit("+", 100))
                        self.task = "\n-\n".join(self.task.rsplit("-", 100))
                        self.task = "\n*\n".join(self.task.rsplit("*", 100))
                        self.task = "\n/\n".join(self.task.rsplit("/", 100))
                        self.TextEntry.insert(1.0, self.task)

            else:   # counts if symbols are digits, "+", "-", "*", "/", ".", "="

                if len(self.task) == 1 and self.task[0] == "0":
                                      # checks if there is zero at the
                                      # begining of task

                    if text == "0":   # does not allow to put zero if
                                      # the first digit in task is zero
                        pass

                    elif text == ".":   # allows to put point after first zero
                                        # which means decimal fraction
                        self.TextEntry.insert(300.0, text)
                        self.task += text

                        if text == "=":
                            if "\n" in self.task:
                                self.TextEntry.delete(1.0, tk.END)
                                self.task = self.task.replace("\n", "")
                                self.task = str(eval(self.task[:-1]))
                                self.TextEntry.insert(2.0, self.task)

                    else:   # counts if zeros are part of number
                        self.TextEntry.insert(300.0, text)
                        self.task += text

                elif "\n+\n0." in self.task or "\n-\n0." in self.task\
                        or "\n*\n0." in self.task or "\n/\n0." in self.task:
                                        # allows to put digits after point
                                        # which means decimal fraction
                    self.TextEntry.insert(300.0, text)
                    self.task += text

                    if text == "=":
                        if "\n" in self.task:
                            self.TextEntry.delete(1.0, tk.END)
                            self.task = self.task.replace("\n", "")
                            self.task = str(eval(self.task[:-1]))
                            self.TextEntry.insert(2.0, self.task)

                elif "\n+\n0" in self.task or "\n-\n0" in self.task\
                        or "\n*\n0" in self.task or "\n/\n0" in self.task:
                                      # if the first digit after
                                      # mathematical operator is zero

                    if text == ".":   # allows to put point after zero
                                      # which means decimal fraction
                        self.TextEntry.insert(300.0, text)
                        self.task += text

                        if text == "=":
                            if "\n" in self.task:
                                self.TextEntry.delete(1.0, tk.END)
                                self.task = self.task.replace("\n", "")
                                self.task = str(eval(self.task[:-1]))
                                self.TextEntry.insert(2.0, self.task)

                    else:   # does not allow to put any digits after zero
                            # if it is not decimal fraction
                        pass

                else:   # puts digits, mathematical operator and point
                    if text == "\n+\n" or text == "\n-\n" \
                            or text == "\n*\n" or text == "\n/\n":
                        # checks if the symbol is "+", "-", "*", "/"

                        if len(self.task) > 2 and self.task[-2] == "+":
                            # does not allow to put mathematical operator
                            # after "+"
                            self.task = self.task[:-3]
                            self.TextEntry.delete(1.0, tk.END)
                            self.TextEntry.insert(300.0, self.task)
                            self.TextEntry.insert(300.0, text)
                            self.task += text

                        elif len(self.task) > 2 and self.task[-2] == "-":
                            # does not allow to put mathematical operator
                            # after "-"
                            self.task = self.task[:-3]
                            self.TextEntry.delete(1.0, tk.END)
                            self.TextEntry.insert(300.0, self.task)
                            self.TextEntry.insert(300.0, text)
                            self.task += text

                        elif len(self.task) > 2 and self.task[-2] == "*":
                            # does not allow to put mathematical operator
                            # after "*"
                            self.task = self.task[:-3]
                            self.TextEntry.delete(1.0, tk.END)
                            self.TextEntry.insert(300.0, self.task)
                            self.TextEntry.insert(300.0, text)
                            self.task += text

                        elif len(self.task) > 2 and self.task[-2] == "/":
                            # does not allow to put mathematical operator
                            # after "/"
                            self.task = self.task[:-3]
                            self.TextEntry.delete(1.0, tk.END)
                            self.TextEntry.insert(300.0, self.task)
                            self.TextEntry.insert(300.0, text)
                            self.task += text

                        else:
                            # allows to put mathematical operators after digits
                            self.TextEntry.insert(300.0, text)
                            self.task += text

                            # if text == "=":
                            #     if "\n" in self.task:
                            #         self.TextEntry.delete(1.0, tk.END)
                            #         self.task = self.task.replace("\n", "")
                            #         self.task = str(eval(self.task[:-1]))
                            #         self.TextEntry.insert(2.0, self.task)

                    else:   #allows to put digits in task
                        self.TextEntry.insert(300.0, text)
                        self.task += text

                        if text == "=":
                            if "\n" in self.task:
                                self.TextEntry.delete(1.0, tk.END)
                                self.task = self.task.replace("\n", "")
                                self.task = str(eval(self.task[:-1]))
                                self.TextEntry.insert(2.0, self.task)


    def InitCalculator(self):
        """
        The function sets Entry Widget's size; also sets buttons' size, location,
        design and functions
        """

        self.TextEntry = tk.Text(self.root, height=15, width=30, font='50')
                             # sets Entry Widget's size

        self.TextEntry.bind("<Key>", lambda e: "break")   # disables any input
                                                          # from keyboard
        self.TextEntry.pack()

        button_zero = tk.Button(self.root, text="0", bg="black",
                                                     fg="white",
                                                     font="50",
                                command=lambda: self.SetTextInput("0"))
        button_zero.place(x = 0,y = 350, height = 50, width = 50)

        button_one = tk.Button(self.root, text="1", bg="black",
                                                    fg="white",
                                                    font="50",
                               command=lambda: self.SetTextInput("1"))
        button_one.place(x=0, y=300, height=50, width=50)

        button_two = tk.Button(self.root, text="2", bg="black",
                                                    fg="white",
                                                    font='50',
                               command=lambda: self.SetTextInput("2"))
        button_two.place(x=50, y=300, height=50, width=50)

        button_three = tk.Button(self.root, text='3', bg="black",
                                                      fg="white",
                                                      font='50',
                                 command=lambda: self.SetTextInput("3"))
        button_three.place(x=100, y=300, height=50, width=50)

        button_four = tk.Button(self.root, text='4', bg="black",
                                                     fg="white",
                                                     font='50',
                                command=lambda: self.SetTextInput("4"))
        button_four.place(x=0, y=250, height=50, width=50)

        button_five = tk.Button(self.root, text='5', bg="black",
                                                     fg="white",
                                                     font='50',
                                command=lambda: self.SetTextInput("5"))
        button_five.place(x=50, y=250, height=50, width=50)

        button_six = tk.Button(self.root, text='6', bg="black",
                                                    fg="white",
                                                    font='50',
                               command=lambda: self.SetTextInput("6"))
        button_six.place(x=100, y=250, height=50, width=50)

        button_seven = tk.Button(self.root, text='7', bg="black",
                                                      fg="white",
                                                      font='50',
                                 command=lambda: self.SetTextInput("7"))
        button_seven.place(x=0, y=200, height=50, width=50)

        button_eight = tk.Button(self.root, text='8', bg="black",
                                                      fg="white",
                                                      font='50',
                                 command=lambda: self.SetTextInput("8"))
        button_eight.place(x=50, y=200, height=50, width=50)

        button_nine = tk.Button(self.root, text='9', bg="black",
                                                     fg="white",
                                                     font='50',
                                command=lambda: self.SetTextInput("9"))
        button_nine.place(x=100, y=200, height=50, width=50)

        button_point = tk.Button(self.root, text='.', bg="black",
                                                      fg="white",
                                                      font='50',
                                 command=lambda: self.SetTextInput("."))
        button_point.place(x=50, y=350, height=50, width=50)

        button_addition = tk.Button(self.root, text='+', bg="orange",
                                                         fg="black",
                                                         font='50',
                                    command=lambda: self.SetTextInput("\n+\n"))
        button_addition.place(x=150, y=200, height=50, width=50)

        button_subtraction = tk.Button(self.root, text = '-', bg="orange",
                                                              fg="black",
                                                              font='50',
                                command=lambda:self.SetTextInput("\n-\n"))
        button_subtraction.place(x=150, y=250, height=50, width=50)

        button_division = tk.Button(self.root, text = '/', bg="orange",
                                                           fg="black",
                                                           font='50',
                                 command=lambda:self.SetTextInput("\n/\n"))
        button_division.place(x=150, y=350, height=50, width=50)


        button_multiplication = tk.Button(self.root, text = '*', bg="orange",
                                                                 fg="black",
                                                                 font='50',
                                   command=lambda:self.SetTextInput("\n*\n"))
        button_multiplication.place(x=150, y=300, height=50, width=50)

        button_square_root = tk.Button(self.root, text = '√', bg="orange",
                                                              fg="black",
                                                              font='50',
                                    command = lambda: self.SetTextInput("√"))
        button_square_root.place(x=100, y=150, height=50, width=50)

        button_square = tk.Button(self.root, text = '^2', bg="orange",
                                                          fg="black",
                                                          font='50',
                                  command = lambda: self.SetTextInput("^2"))
        button_square.place(x=150, y=150, height=50, width=50)

        button_equals = tk.Button(self.root, text = '=', bg="black",
                                                         fg="white",
                                                         font='50',
                                 command=lambda: self.SetTextInput("="))
        button_equals.place(x=100, y=350, height=50, width=50)

        button_delete_all = tk.Button(self.root, text = 'AC', bg="orange",
                                                              fg="black",
                                                              font='50',
                                     command=lambda: (self.SetTextInput("AC"),
                                     self.TextEntry.delete(1.0, tk.END)))
        button_delete_all.place(x=0, y=150, height=50, width=50)

        button_delete = tk.Button(self.root, text = 'C', bg="orange",
                                                         fg="black",
                                                         font='50',
                                  command = lambda: self.SetTextInput("C"))
        button_delete.place(x=50, y=150, height=50, width=50)


if __name__ == "__main__":
    main = Calculator()
    main.InitCalculator()
    main.root.mainloop()

