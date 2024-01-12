import requests


def update_tor():
    get_tor_list = requests.get("https://check.torproject.org/torbulkexitlist")
    tor_list_text = get_tor_list.text
    # Convert newline-separated text to a list
    #it could be left as it is, but i want to use this for other things too
    r_list = tor_list_text.split('\n')
    
    
    with open('tor_exit_node_list_test.txt', 'w') as tor_list:
        for ip in r_list:
            tor_list.write(ip + '\n')


update_tor()