import sys
import PyQt6
##import main_ui

from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QFontDatabase

app = QApplication([])

# Load the font from your system
font_id = QFontDatabase.addApplicationFont("path/to/your/font.ttf")
font_families = QFontDatabase.applicationFontFamilies(font_id)

label = QLabel("1")
if font_families:
    label.setFont(QFont(font_families[0], 12))  # Set the font size as desired

label.show()
app.exec()