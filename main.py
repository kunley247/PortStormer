#!/usr/bin/python3

import argparse
from libraries import *

def parse_arguments():
    parser = argparse.ArgumentParser(description="Retrieve IP address and port number.")
    parser.add_argument('--host', '-H', required=True, help="Specify the host (URL or IP address).")
    parser.add_argument('--port', '-p', required=True, help="Specify the port number.")
    return parser.parse_args()

def main():
    args = parse_arguments()

    ip_address = args.host
    port_input = args.port

    if is_valid_ip(ip_address):
        pass
    elif is_valid_url(ip_address):
        resolved_ip = get_ip_address(ip_address)
        if resolved_ip is not None:
            ip_address = resolved_ip
        else:
            print(f"Could not resolve the host '{args.host}' to an IP address.")
            return
    else:
        print(f"The host '{ip_address}' is not a valid IP address or URL.")
        return

    if is_valid_port(port_input):
        port_number = int(port_input)
        print(f"The IP address is: {ip_address}")
        print(f"The port number is: {port_number}")
    else:
        print(f"The input '{port_input}' is not a valid port number.")

if __name__ == "__main__":
    main()