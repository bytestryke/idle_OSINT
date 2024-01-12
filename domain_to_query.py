from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextBrowser

class masterDomain(QWidget):
    def __init__(self):
        super().__init__()
        self.master_domain_entry = QLineEdit()
