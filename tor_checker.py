from ip_address_to_query import masterIP
import requests


class TorChecker:
    def __init__(self, master_ip_instance):
        self.master_ip_instance = masterIP()
        self.ip_address_to_query = self.master_ip_instance.master_ip_entry.text()
    

    def check_tor(self):
        with open("tor_exit_node_list.txt", "r") as file:
            tor_exit_nodes = file.read().splitlines()

        if self.ip_address_to_query in tor_exit_nodes:
            is_tor = "Is a Tor Exit Node"

        else:
            is_tor = "Is not a Tor Exit Node"
        
        return is_tor