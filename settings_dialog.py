# settings_dialog.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from config import Config

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manage Keys")
        self.setGeometry(200, 200, 400, 200)

        self.label_shodan = QLabel("Shodan API Key:")
        self.entry_shodan = QLineEdit()
        self.label_virus_total = QLabel("VirusTotal API Key:")
        self.entry_virus_total = QLineEdit()
        self.save_button = QPushButton("Save")

        layout = QVBoxLayout(self)
        layout.addWidget(self.label_shodan)
        layout.addWidget(self.entry_shodan)
        layout.addWidget(self.label_virus_total)
        layout.addWidget(self.entry_virus_total)
        layout.addWidget(self.save_button)

        self.save_button.clicked.connect(self.save_settings)

    def save_settings(self):
        shodan_api_key = self.entry_shodan.text()
        virus_total_api_key = self.entry_virus_total.text()

        if shodan_api_key or virus_total_api_key:
            Config.set_api_keys(shodan_api_key, virus_total_api_key)
            Config.save()  # Save the configuration to the file

        self.close()
