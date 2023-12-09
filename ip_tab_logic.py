import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextBrowser
import requests

class IPLocationApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.label = QLabel("Enter the IP address to query:")
        self.entry = QLineEdit()
        self.button = QPushButton("Get Location")
        self.result_label = QLabel("IPLcocation.net")
        self.result_browser = QTextBrowser()

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_browser)

        # Connect button click event to method
        self.button.clicked.connect(self.iplocation_button_click)

    def get_ip_location(self, ip_address):
        url = f"https://api.iplocation.net/?ip={ip_address}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

            # Parse the JSON content into a dictionary
            response_dict = response.json()

            # Display information in the result_label
            self.result_browser.setText(
                f'IP: {response_dict["ip"]}\n'
                f'Country: {response_dict["country_name"]} (Code: {response_dict["country_code2"]})\n'
                f'ISP: {response_dict["isp"]}'
            )
        except requests.RequestException as e:
            self.result_browser.setText(f"Request failed: {e}")

    def iplocation_button_click(self):
        ip_address_to_query = self.entry.text()
        self.get_ip_location(ip_address_to_query)

if __name__ == '__main__':
    # Create the Qt application
    app = QApplication(sys.argv)

    # Create an instance of your custom widget
    widget = IPLocationApp()

    # Set up the main window
    widget.setGeometry(100, 100, 400, 300)
    widget.setWindowTitle("IP Location Lookup")

    # Show the widget
    widget.show()

    # Start the application event loop
    sys.exit(app.exec_())
