import sys
from PySide6.QtWidgets import QMainWindow, QMenuBar, QApplication, QWidget, QVBoxLayout, QTabWidget, QFrame
from PySide6.QtGui import QAction, QPalette, QColor
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



        # Create actions for the menu
        self.manage_keys = QAction('Manage Keys', self)
        self.manage_keys.triggered.connect(self.open_settings)
        self.light_mode_action = QAction('Light Mode', self)
        self.light_mode_action.triggered.connect(self.set_light_mode)
        self.dark_mode_action = QAction('Dark Mode', self)
        self.dark_mode_action.triggered.connect(self.set_dark_mode)
        self.update_ip_intel = QAction('Update Tor', self)
        
        # Create a frame to contain the menu bar and add a border
        menu_frame = QFrame(self)
        menu_frame.setFrameShape(QFrame.StyledPanel)
        menu_frame.setFrameShadow(QFrame.Sunken)
        # Set the background color of the frame
        menu_frame.setStyleSheet("background-color: #D3D3D3;") 

        # Create and set up the menu bar
        menubar = self.create_menu_bar()
        menubar.addAction(self.manage_keys)
        main_layout.addWidget(menubar)
        
        # Create a 'Mode' menu
        mode_menu = menubar.addMenu('Color Mode')
        mode_menu.addAction(self.light_mode_action)
        mode_menu.addAction(self.dark_mode_action)

        #Create a 'Update Tor' menu
        tor_menu = menubar.addMenu('Update Tor')
        tor_menu.addAction(self.update_ip_intel)


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

    def set_light_mode(self):
        self.set_app_theme(QPalette.Light)

    def set_dark_mode(self):
        self.set_app_theme(QPalette.Dark)

    def set_app_theme(self, theme):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255) if theme == QPalette.Light else QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0) if theme == QPalette.Light else QColor(255, 255, 255))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = IPDomainInfoApp()
    widget.setGeometry(200, 200, 800, 500)
    widget.setWindowTitle("idle OSINT")
    widget.show()
    sys.exit(app.exec())
