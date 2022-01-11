import sys
from PyQt6 import QtWidgets
from myWidgets import QmyReserveForm

app = QtWidgets.QApplication(sys.argv)

form = QmyReserveForm()
form.show()

sys.exit(app.exec())