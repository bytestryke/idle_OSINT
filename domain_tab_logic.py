from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QTextBrowser
import requests
from bs4 import BeautifulSoup
from domain_to_query import masterDomain

class DomainTabLogic(QWidget):
    def __init__(self):
        super().__init__()

        #Create an instance of masterDomain
        self.masterDomain_instance = masterDomain()

        #Create Widgets
        self.label = QLabel("Enter the domain name to query:")
        self.domain_entry = self.masterDomain_instance.master_domain_entry
        self.button = QPushButton("Submit Domain")
        self.crt_result_label = QLabel("crt.sh")
        self.crt_result_browser = QTextBrowser()
        self.shodan_result_label = QLabel("Shodan")
        self.shodan_result_browser = QTextBrowser()
        self.whois_result_label = QLabel("Whois")
        self.whois_result_browser = QTextBrowser()
        self.dnsdumpster_result_label = QLabel("DNSDumpster")
        self.dnsdumpster_result_browser = QTextBrowser()

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.domain_entry)
        layout.addWidget(self.button)
        layout.addWidget(self.crt_result_label)
        layout.addWidget(self.crt_result_browser)
        layout.addWidget(self.shodan_result_label)
        layout.addWidget(self.shodan_result_browser)
        layout.addWidget(self.whois_result_label)
        layout.addWidget(self.whois_result_browser)
        layout.addWidget(self.dnsdumpster_result_label)
        layout.addWidget(self.dnsdumpster_result_browser)
        
        #####Create action when button is clicked
        self.button.clicked.connect(self.domain_info_submit_button_click)

    def get_unique_domains(self, domain_to_query):
        r = requests.get(f"https://crt.sh/?q={domain_to_query}")
        r_text = r.text
        #use beautiful soup to scrape
        soup = BeautifulSoup(r_text, 'html.parser')
        td_elements = soup.find_all('td')
        #make a set of unique domain names scraped. set is an ADT with unique contents
        unique_domains = set()

        for td in td_elements:
            domains = [domain.strip() for domain in td.get_text(separator='\n').split('\n') if domain.strip()]
            unique_domains.update(domains)

        result_browser = '\n'.join(domain for domain in unique_domains if domain_to_query in domain)
        self.crt_result_browser.setText(result_browser)

    #def check_virus_total(self, domain_to_query):


##############################################################################################################
#### submit button click
    def domain_info_submit_button_click(self):
        domain_to_query = self.domain_entry.text()
        self.get_unique_domains(domain_to_query)
        #self.check_tor(ip_address_to_query)
        #self.shodan_check(ip_address_to_query)
        