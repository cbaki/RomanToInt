import sys
from PyQt5 import QtWidgets

roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class RomanNumeralsConverter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Roman Numerals Converter')

        label = QtWidgets.QLabel('Enter a Roman numeral or an integer:')
        self.entry = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton('Convert', clicked=self.convert)
        self.result_label = QtWidgets.QLabel()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(label)
        v_box.addWidget(self.entry)
        v_box.addWidget(self.button)
        v_box.addWidget(self.result_label)

        self.entry.returnPressed.connect(self.button.click)
        self.button.setAutoDefault(True)

        self.setLayout(v_box)

        self.setFixedSize(500, 250)
        screen_center = QtWidgets.QDesktopWidget().screenGeometry().center()
        widget_center = self.geometry().center()
        self.move(screen_center - widget_center)

    def convert(self):
        input_text = self.entry.text()

        try:
            input_number = int(input_text)
            result = IntToRoman(input_number)
        except ValueError:
            try:
                input_roman = input_text.upper()
                for char in input_roman:
                    if char not in roman.keys():
                        raise ValueError("Invalid Input")
                result = RomanToInt(input_roman)
            except ValueError:
                result = "Invalid Input"

        self.result_label.setText(str(result))

def RomanToInt(s):
    s = s.upper()
    value = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i-1]]:
            value += roman[s[i]] - 2 * roman[s[i-1]]
        else:
            value += roman[s[i]]
    return value

def IntToRoman(num):
    if not isinstance(num, int) or num <= 0:
        return "Invalid Input"

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ""
    for value, numeral in roman_numerals.items():
        count = num // value
        result += numeral * count
        num -= value * count
    return result

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RomanNumeralsConverter()
    window.show()
    sys.exit(app.exec_())
