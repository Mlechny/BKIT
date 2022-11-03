from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from PyQt6.QtWidgets import QApplication, QPushButton

import sys

def main():
    r = Rectangle ("синего", 21, 21)
    c = Circle ("синего", 21)
    s = Square ("красного", 21)
    print(r)
    print(c)
    print(s)

    app = QApplication(sys.argv)
    window = QPushButton("Wagwan, my bruddas")
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
