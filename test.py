#!/usr/bin/env python

import csv
import sys
import socket



# Given a host, find the ip
def lookup(host):
    try:
        hostname, aliaslist, ipaddrlist = socket.gethostbyname_ex(host)
        return ipaddrlist
    except:
        return []

# Given an ip, return the host
def rlookup(ip):
    try:
        hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
        return hostname
    except:
        return ''

def main():
    if len(sys.argv) != 3:
        print("Usage: python external_lookup.py [host field] [ip field]")
        sys.exit(1)

    hostfield = sys.argv[1]
    ipfield = sys.argv[2]

    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
    w.writeheader()

    for result in r:
    # Perform the lookup or reverse lookup if necessary
        if result[hostfield] and result[ipfield]:
    # both fields were provided, just pass it along
            w.writerow(result)

        elif result[hostfield]:
            # only host was provided, add ip
            ips = lookup(result[hostfield])
            for ip in ips:
                result[ipfield] = ip
                w.writerow(result)

        elif result[ipfield]:
        # only ip was provided, add host
            result[hostfield] = rlookup(result[ipfield])
            if result[hostfield]:
            w.writerow(result)

main()

