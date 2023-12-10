import sys
from PySide6.QtWidgets import QMainWindow, QMenuBar, QApplication, QWidget, QVBoxLayout, QTabWidget, QFrame
from PySide6.QtGui import QAction
from ip_tab_logic import IPLocationApp
from domain_tab_logic import DomainTabLogic
from settings_dialog import SettingsDialog


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


        # Create the 'Manage Keys' action globally
        self.settings_action = QAction('Manage Keys', self)
        self.settings_action.triggered.connect(self.open_settings)

        # Create actions for the menu
        self.settings_action = QAction('Manage Keys', self)
        self.settings_action.triggered.connect(self.open_settings)
        
        # Create a frame to contain the menu bar and add a border
        menu_frame = QFrame(self)
        menu_frame.setFrameShape(QFrame.StyledPanel)
        menu_frame.setFrameShadow(QFrame.Sunken)
        # Set the background color of the frame
        menu_frame.setStyleSheet("background-color: #333333;") 

        # Create and set up the menu bar
        menubar = self.create_menu_bar()
        menubar.addAction(self.settings_action)
        main_layout.addWidget(menubar)

        # Add the menu bar to the frame
        menu_layout = QVBoxLayout(menu_frame)
        menu_layout.addWidget(menubar)
        # Add the frame to the main layout
        main_layout.addWidget(menu_frame)

    
    def create_menu_bar(self):
        menubar = QMenuBar(self)
        return menubar


    def open_settings(self):
        settings_dialog = SettingsDialog()
        settings_dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = IPDomainInfoApp()
    widget.setGeometry(100, 100, 600, 400)
    widget.setWindowTitle("Lazy OSINT")
    widget.show()
    sys.exit(app.exec())
