#integrate nmap
#import system operating system
import os

#defining operation
def traceroute(destination):
    #stating operation to be done
    response = os.system(f'tracert -d -h 20 -w 1000 {destination}')

def ping(dest_ip):
    response = os.system(f'ping -n 5 -w 1 {dest_ip}')

def scan(dest_ip):
    response = os.system(f'nmap -p- -sV {dest_ip}')

#for iteration purpose
i = 1
while i < 3:
    #entering the address or ip
    destination = input ('Enter Destination Address: ') 
    dest_ip = input ('Enter Ping IP: ')

    #Calling the functions for operation
    ping(dest_ip)
    scan(dest_ip)
    traceroute(destination)