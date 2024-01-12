from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextBrowser

class masterIP(QWidget):
    def __init__(self):
        super().__init__()
        self.master_ip_entry = QLineEdit()
