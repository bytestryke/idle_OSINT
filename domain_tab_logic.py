from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QTextBrowser
import requests
from bs4 import BeautifulSoup

class DomainTabLogic(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Enter the domain name to query:")
        self.entry = QLineEdit()
        self.button = QPushButton("Get Unique Domains")
        self.result_label = QLabel("CRT.sh")
        self.result_browser = QTextBrowser()

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_browser)
        
        # Set the QTextBrowser widget as read-only
        self.result_browser.setOpenExternalLinks(True)  # Enable links, optional
        self.result_browser.setOpenLinks(False)  # Disable navigation, optional

        self.button.clicked.connect(self.get_unique_domains)

    def get_unique_domains(self):
        domain_name = self.entry.text()

        r = requests.get(f"https://crt.sh/?q={domain_name}")
        r_text = r.text

        soup = BeautifulSoup(r_text, 'html.parser')
        td_elements = soup.find_all('td')

        unique_domains = set()

        for td in td_elements:
            domains = [domain.strip() for domain in td.get_text(separator='\n').split('\n') if domain.strip()]
            unique_domains.update(domains)

        result_browser = '\n'.join(domain for domain in unique_domains if domain_name in domain)
        self.result_browser.setPlainText(result_browser)
