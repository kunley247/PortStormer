import socket

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
    
def get_ip_address(domain_or_ip):
    try:
        ip_address = socket.gethostbyname(domain_or_ip)
        return ip_address
    except socket.gaierror:
        print(f"Could not resolve the input '{domain_or_ip}' to an IP address.")
        return None
    

def is_valid_url(url):
    try:
        socket.gethostbyname(url)
        return True
    except socket.gaierror:
        return False
    

def is_valid_port(port):
    try:
        port = int(port)
        if 0 < port <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False