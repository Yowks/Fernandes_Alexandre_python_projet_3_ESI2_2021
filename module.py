from PyQt5.QtWidgets import QLabel, QComboBox, QDoubleSpinBox, QCalendarWidget, QDialog, QApplication, QGridLayout, QPushButton
from currency_converter import CurrencyConverter

# Create, display and refresh UI
class MaFenetre(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        c = CurrencyConverter()
        allCurrency = c.currencies

        # initialize currencies
        self.currencies = []

        for i in allCurrency : 
            self.currencies.append(i)

        # initialize widgets
        self.from_currency_label = QLabel("From currency:")
        self.from_currency = QComboBox()
        self.from_currency.addItems(self.currencies)
        self.to_currency_label = QLabel("To currency:")
        self.to_currency = QComboBox()
        self.to_currency.addItems(self.currencies)
        self.invert = QPushButton ('Invert', self)
        self.from_amount_label = QLabel("Amount to convert:")
        self.from_amount = QDoubleSpinBox()
        self.from_amount.setRange(0.01, 100000000.00)
        self.from_amount.setValue(1.00)
        self.to_amount_label = QLabel("Converted value: ")
        self.to_amount = QLabel("%.02f" % 1.00)

        # set widgets into layout
        grid = QGridLayout()
        grid.addWidget(self.from_currency_label, 0, 0)
        grid.addWidget(self.from_currency, 0, 1)
        grid.addWidget(self.invert, 0, 2)
        grid.addWidget(self.to_currency_label, 0, 3)
        grid.addWidget(self.to_currency, 0, 4)
        grid.addWidget(self.from_amount_label, 1, 0)
        grid.addWidget(self.from_amount, 1, 1)
        grid.addWidget(self.to_amount_label, 1, 2)
        grid.addWidget(self.to_amount, 1, 3)
        self.setLayout(grid)
        self.setWindowTitle("Converter")

        # set event when input change (refresh ui)
        self.from_currency.currentIndexChanged.connect(self.update_ui)
        self.to_currency.currentIndexChanged.connect(self.update_ui)
        self.from_amount.valueChanged.connect(self.update_ui)
        
        self.invert.clicked.connect(self.invert_currency)

    # Refresh all the window
    def update_ui(self):
        c = CurrencyConverter()
        try:
            # get the currency
            from_cur = self.from_currency.currentText()
            to_cur = self.to_currency.currentText()
            amount = self.from_amount.value()

            # get converted value
            result = str(round(c.convert(amount, from_cur, to_cur),2))
            
            self.to_amount.setText(result)
        except Exception as e:
            print(e)
    
    def invert_currency(self):
        old_from_cur = self.from_currency.currentText()
        old_to_cur = self.to_currency.currentText()
        print(old_from_cur)
        print(old_to_cur)
        self.from_currency.setCurrentText(old_to_cur)
        self.to_currency.setCurrentText(old_from_cur) 
