import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextBrowser
import requests
from ip_address_to_query import masterIP
from shodan import Shodan
import configparser

class IPLocationApp(QWidget):
    def __init__(self):
        super().__init__()

        #create  instance of masterIP
        self.masterIP_instance = masterIP()
        # Create widgets
        self.label = QLabel("Enter the IP address to query:")
        self.ip_entry = self.masterIP_instance.master_ip_entry
        self.button = QPushButton("Submit IP")
        self.ip_location_result_label = QLabel("IPLocation.net")
        self.tor_result_label = QLabel("Tor Exit Node Check")
        self.ip_location_result_browser = QTextBrowser()
        self.tor_result_browser = QTextBrowser()
        self.shodan_result_label = QLabel("Shodan")
        self.shodan_result_browser = QTextBrowser()
        self.censys_result_label = QLabel("Censys")
        self.censys_result_browser = QTextBrowser()
        self.virus_total_result_label = QLabel("VirusTotal")
        self.virus_total_result_browser = QTextBrowser()
        self.alienvault_otx_result_label = QLabel("AlienVault OTX")
        self.alienvault_otx_result_browser = QTextBrowser()

        

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.ip_entry)
        layout.addWidget(self.button)
        layout.addWidget(self.ip_location_result_label)
        layout.addWidget(self.ip_location_result_browser)
        layout.addWidget(self.tor_result_label)
        layout.addWidget(self.tor_result_browser)
        layout.addWidget(self.shodan_result_label)
        layout.addWidget(self.shodan_result_browser)
        layout.addWidget(self.censys_result_label)
        layout.addWidget(self.censys_result_browser)
        layout.addWidget(self.virus_total_result_label)
        layout.addWidget(self.virus_total_result_browser)
        layout.addWidget(self.alienvault_otx_result_label)
        layout.addWidget(self.alienvault_otx_result_browser)

        # Connect button click event to method
        self.button.clicked.connect(self.ip_info_submit_button_click)
##############################################################################################################
#### Get IP Location
    def get_ip_location(self, ip_address_to_query):
        url = f"https://api.iplocation.net/?ip={ip_address_to_query}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

            # Parse the JSON content into a dictionary
            response_dict = response.json()

            # Display information in the result_label
            self.ip_location_result_browser.setText(
                f'IP: {response_dict["ip"]}\n'
                f'Country: {response_dict["country_name"]} (Code: {response_dict["country_code2"]})\n'
                f'ISP: {response_dict["isp"]}'
            )
        except requests.RequestException as e:
            self.ip_location_result_browser.setText(f"Request failed: {e}")
##############################################################################################################
#### Check is IP is a Tor Exit Node
    def check_tor(self, ip_address_to_query):
        with open("tor_exit_node_list.txt", "r") as file:
            tor_exit_nodes = file.read().splitlines()

        if ip_address_to_query in tor_exit_nodes:
            is_tor = "Is a Tor Exit Node"
        else:
            is_tor = "Is not a Tor Exit Node"
        
        self.tor_result_browser.setText(is_tor)

##############################################################################################################
#### Shodan
    def shodan_check(self, ip_address_to_query):
        # Create a ConfigParser object and read the config.ini file
        config = configparser.ConfigParser()
        config.read('config.ini')
        # Retrieve a value from a specific section and key
        shodan_api_key = config.get('APIKeys', 'shodan_api_key')
    
        try:
            # Initialize Shodan object with the API key
            shodan_api = Shodan(shodan_api_key)
            # Query Shodan for information about the IP address
            ip_hostname_request = shodan_api.host(ip_address_to_query)

        
            # Set the result in the result browser
            self.shodan_result_browser.setText(f"Location: {ip_hostname_request['city']}, {ip_hostname_request['region_code']} {ip_hostname_request['country_name']}  |  lat/lon: {ip_hostname_request['longitude']}, {ip_hostname_request['latitude']}")
        except Exception as e:
            self.shodan_result_browser.setText(f"Request failed: {e}")

##############################################################################################################
#####check virus total
    def virus_total_check(self, ip_address_to_query):
        # Create a ConfigParser object and read the config.ini file
        config = configparser.ConfigParser()
        config.read('config.ini')
        # Retrieve a value from a specific section and key
        virus_total_api_key = config.get('APIKeys', 'virus_total_api_key')

        ip = ip_address_to_query
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
        headers = {"accept": "application/json", "x-apikey": f"{virus_total_api_key}"}
        response = requests.get(url, headers=headers)
        self.virus_total_result_browser.setText(response.text)

##############################################################################################################
#####check alienvault otx
    def alienvault_otx_check(self, ip_address_to_query):
        # Create a ConfigParser object and read the config.ini file
        config = configparser.ConfigParser()
        config.read('config.ini')
        # Retrieve a value from a specific section and key
        alienvault_otx_api_key = config.get('APIKeys', 'alienvault_otx_api_key')
        sections = ["reputation", "geo", 'malware', 'url_list', 'passive_dns']  # Replace with the desired section
        for section in sections:
            url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip_address_to_query}/{section}"
            headers = {'X-OTX-API-KEY': alienvault_otx_api_key}
            response = requests.get(url, headers=headers)
            current_text = self.alienvault_otx_result_browser.toPlainText()
            new_text = current_text + "\n" + response.text
            self.alienvault_otx_result_browser.setPlainText(new_text)
        
        
##############################################################################################################
#### submit button click
    def ip_info_submit_button_click(self):
        ip_address_to_query = self.ip_entry.text()
        self.get_ip_location(ip_address_to_query)
        self.check_tor(ip_address_to_query)
        self.shodan_check(ip_address_to_query)
        self.virus_total_check(ip_address_to_query)
        #self.alienvault_otx_check(ip_address_to_query)
        