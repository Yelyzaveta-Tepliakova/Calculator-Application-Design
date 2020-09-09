#####################################################################
## Description:    The program makes unit tests for basic arithmetic
##                 calculations in calculator made by GUI
#####################################################################
## Author:         Yelyzaveta Tepliakova
## Python version: 3.8.
## Date:           09.02.2020
#####################################################################

import unittest
import sys

sys.path.append('C:/Users/HP/PycharmProjects/pythonProject/'
                   'python_files')

from Calculator_2 import Calculator
                    # imports class Calculator with all its methods

class TestCalculator(unittest.TestCase):   # tests Calculation method

    def test_1(self):   # tests calculating with negative numbers
        main.Calculation("AC")
        main.Calculation("\n-\n")
        main.Calculation("290")
        main.Calculation("\n-\n")
        main.Calculation("25")
        main.Calculation("\n+\n")
        main.Calculation("14")
        main.Calculation("\n*\n")
        main.Calculation("3")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = "-273"
        self.assertEqual(actual_result, expected_result)


    def test_2(self):   # tests multiplying by zero
        main.Calculation("AC")
        main.Calculation("22")
        main.Calculation(".")
        main.Calculation("59")
        main.Calculation("\n+\n")
        main.Calculation("56")
        main.Calculation("\n*\n")
        main.Calculation("0")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = "22.59"
        self.assertEqual(actual_result, expected_result)


    def test_3(self):   # tests decimal fraction's calculating
        main.Calculation("AC")
        main.Calculation("45")
        main.Calculation(".")
        main.Calculation("8")
        main.Calculation("\n+\n")
        main.Calculation("9")
        main.Calculation(".")
        main.Calculation("34")
        main.Calculation("\n/\n")
        main.Calculation("0")
        main.Calculation(".")
        main.Calculation("22")
        main.Calculation("\n*\n")
        main.Calculation("3")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = "173.16363636363636"
        self.assertEqual(actual_result, expected_result)


    def test_4(self):   # tests square of a number
        main.Calculation("AC")
        main.Calculation("90")
        main.Calculation("^2")
        main.Calculation("\n*\n")
        main.Calculation("19")
        main.Calculation("\n+\n")
        main.Calculation("6")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = "153906"
        self.assertEqual(actual_result, expected_result)


    def test_5(self):   # tests nth root of a number
        main.Calculation("AC")
        main.Calculation("121")
        main.Calculation("√")
        main.Calculation("\n+\n")
        main.Calculation("84")
        main.Calculation("\n/\n")
        main.Calculation("2")
        main.Calculation("\n-\n")
        main.Calculation("7")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = "46.0"
        self.assertEqual(actual_result, expected_result)


    def test_6(self):   # tests changing of mathematical
                        # operators during calculating
        main.Calculation("AC")
        main.Calculation("264")
        main.Calculation("\n-\n")
        main.Calculation("\n+\n")
        main.Calculation("81")
        main.Calculation("\n+\n")
        main.Calculation("\n*\n")
        main.Calculation("2")
        main.Calculation("\n*\n")
        main.Calculation("\n/\n")
        main.Calculation("4")
        main.Calculation("\n/\n")
        main.Calculation("\n/\n")
        main.Calculation("1")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = "304.5"
        self.assertEqual(actual_result, expected_result)


    def test_7(self):   # tests clearing last symbol
        main.Calculation("AC")
        main.Calculation("\n-\n")
        main.Calculation("98")
        main.Calculation("\n-\n")
        main.Calculation("731")
        main.Calculation("\n+\n")
        main.Calculation("49")
        main.Calculation("C")
        main.Calculation("C")
        main.Calculation("C")
        main.Calculation("\n-\n")
        main.Calculation("40")
        main.Calculation(".")
        main.Calculation("8")
        main.Calculation("C")
        main.Calculation("9")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = "-869.9"
        self.assertEqual(actual_result, expected_result)


    def test_8(self):   # tests equals sign during calculating
        main.Calculation("AC")
        main.Calculation("85")
        main.Calculation("\n/\n")
        main.Calculation("5")
        main.Calculation("\n+\n")
        main.Calculation("77")
        main.Calculation(".")
        main.Calculation("98")
        main.Calculation("=")
        main.Calculation("\n-\n")
        main.Calculation("98")
        main.Calculation("\n*\n")
        main.Calculation("2")
        main.Calculation("=")
        main.Calculation("\n+\n")
        main.Calculation("78")
        main.Calculation(".")
        main.Calculation("8")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = "-22.22"
        self.assertEqual(actual_result, expected_result)


    def test_9(self):  # tests ability to put not mathematical
                       # signs into formula
        main.Calculation("AC")
        main.Calculation("f")
        main.Calculation(",")
        main.Calculation("@")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = ""
        self.assertEqual(actual_result, expected_result)


    def test__10(self):  # tests ability to put nth root of a number
                         # or square of a number during counting
        main.Calculation("AC")
        main.Calculation("8")
        main.Calculation("\n+\n")
        main.Calculation("9")
        main.Calculation("√")
        main.Calculation("\n-\n")
        main.Calculation("2")
        main.Calculation("^2")
        main.Calculation("=")
        actual_result = main.formula
        expected_result = "15"
        self.assertEqual(actual_result, expected_result)


    def test__11(self):   # tests ability to take nth root
                          # of a negative number
        main.Calculation("AC")
        main.Calculation("\n-\n")
        main.Calculation("9")
        main.Calculation("√")
        actual_result = main.formula
        expected_result = "-9"
        self.assertEqual(actual_result, expected_result)


    def test__12(self):   # tests clearing everything by AC
        main.Calculation("AC")
        main.Calculation("9")
        main.Calculation("\n-\n")
        main.Calculation("7")
        main.Calculation("AC")
        actual_result = main.formula
        expected_result = ""
        self.assertEqual(actual_result, expected_result)


    def test__13(self):   # tests clearing everything by C
        main.Calculation("AC")
        main.Calculation("C")
        actual_result = main.formula
        expected_result = ""
        self.assertEqual(actual_result, expected_result)


    def test__14(self):   # tests ability to put digits after
                          # zero and making decimal fraction
        main.Calculation("AC")
        main.Calculation("0")
        main.Calculation("7")
        main.Calculation("9")
        main.Calculation(".")
        main.Calculation("78")
        actual_result = main.formula
        expected_result = "0.78"
        self.assertEqual(actual_result, expected_result)


    def test__15(self):   # tests ability to square
                          # a negative number
        main.Calculation("AC")
        main.Calculation("\n-\n")
        main.Calculation("7")
        main.Calculation("^2")
        actual_result = main.formula
        expected_result = "49"
        self.assertEqual(actual_result, expected_result)


    def test__16(self):   # tests clearing last symbol so
                          # that the whole formula is empty
        main.Calculation("C")
        main.Calculation("C")
        actual_result = main.formula
        expected_result = ""
        self.assertEqual(actual_result, expected_result)


    def test__17(self):   # tests ability to put mathematical
                          # operators after zero
        main.Calculation("0")
        main.Calculation("\n+\n")
        actual_result = main.formula
        expected_result = "0\n+\n"
        self.assertEqual(actual_result, expected_result)

    def test__18(self):   # tests ability to put zero after
                          # zero
        main.Calculation("AC")
        main.Calculation("0")
        main.Calculation("0")
        actual_result = main.formula
        expected_result = "0"
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    main = Calculator()
    unittest.main()

