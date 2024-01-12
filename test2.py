import sys
import socket


host = "www.google.com"
ip = "8.8.8.8"

# Given a host, find the ip
def lookup(host):
    try:
        ipaddrlist = socket.gethostbyname(host)
        print(ipaddrlist)
    except:
        print("error")
        

lookup(host)



# Given an ip, return the host
def rlookup(ip):
    try:
        address = socket.gethostbyaddr(ip)
        print(address)
    except:
        return 'error'
rlookup(ip)