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
        self.label_censys = QLabel("Censys API Key:")
        self.entry_censys = QLineEdit()
        self.label_alienvault_otx = QLabel("AlienVault OTX API Key:")
        self.entry_alienvault_otx = QLineEdit()
        self.save_button = QPushButton("Save")

        layout = QVBoxLayout(self)
        layout.addWidget(self.label_shodan)
        layout.addWidget(self.entry_shodan)
        layout.addWidget(self.label_virus_total)
        layout.addWidget(self.entry_virus_total)
        layout.addWidget(self.label_censys)
        layout.addWidget(self.entry_censys)
        layout.addWidget(self.label_alienvault_otx)
        layout.addWidget(self.entry_alienvault_otx)
        layout.addWidget(self.save_button)

        self.save_button.clicked.connect(self.save_settings)

    def save_settings(self):
        shodan_api_key = str(self.entry_shodan.text())
        virus_total_api_key = str(self.entry_virus_total.text())
        censys_api_key = str(self.entry_censys.text())
        alienvault_otx_api_key = str(self.entry_alienvault_otx.text())

        if shodan_api_key or virus_total_api_key or censys_api_key or alienvault_otx_api_key:
            Config.set_api_keys(shodan_api_key, virus_total_api_key, censys_api_key, alienvault_otx_api_key)
            Config.save()  # Save the configuration to the file

        self.close()
