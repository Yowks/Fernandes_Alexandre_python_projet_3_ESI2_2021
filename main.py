import sys
from PyQt5.QtWidgets import QLabel, QComboBox, QDoubleSpinBox, QCalendarWidget, QDialog, QApplication, QGridLayout, QPushButton
import module

app = QApplication(sys.argv)
currency_converter = module.MaFenetre()
currency_converter.show()
sys.exit(app.exec_())