import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from ip_tab_logic import IPLocationApp
from domain_tab_logic import DomainTabLogic

class IPDomainInfoApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create a tab widget
        self.tab_widget = QTabWidget(self)

        # Create tabs for IP and Domain sections
        self.ip_tab_logic = IPLocationApp()
        self.domain_tab_logic = DomainTabLogic()

        # Add tabs to the tab widget
        self.tab_widget.addTab(self.ip_tab_logic, "IP Address Info")
        self.tab_widget.addTab(self.domain_tab_logic, "Domain Info")

        # Set up the main layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.tab_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = IPDomainInfoApp()
    widget.setGeometry(100, 100, 600, 400)
    widget.setWindowTitle("Lazy OSINT")
    widget.show()
    sys.exit(app.exec())
