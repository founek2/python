#!/usr/bin/python
# -'''- coding: utf-8 -'''-
import sys
from PySide2.QtWidgets import QApplication, QPushButton


def say_hello():
    print("Button clicked, Hello!")


# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()
# Run the main Qt loop
app.exec_()