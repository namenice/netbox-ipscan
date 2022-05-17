#!/usr/bin/python
import networkscan
import ipaddress

from netaddr import *
from netbox import NetBox

netbox = NetBox(host='192.168.10.22', port=8000, use_ssl=False, auth_token='428b27160235093fae5f06da3e6e233af32ae5c0')

my_network = "192.168.10.0/24"
my_scan = networkscan.Networkscan(my_network)
my_scan.run()


#print (dir(netbox.ipam))

a_network = my_scan.list_of_hosts_found
for ip in ipaddress.IPv4Network(my_network).hosts():
    if str(ip) in a_network:
        ip_netbox = netbox.ipam.get_ip_addresses(address=str(ip))
        if str(len(ip_netbox)) == "1":
            print ("Already have IP : ", ip)
        else:
            netbox.ipam.create_ip_address(str(ip))
            print ("Add IP : ", ip)
    else:
        ip_netbox = netbox.ipam.get_ip_addresses(address=str(ip))
        if str(ip_netbox) != "[]":
            netbox.ipam.delete_ip_address(str(ip))
            print ("Remove ip : " , ip)
        print ("It not use ip : ", ip)

