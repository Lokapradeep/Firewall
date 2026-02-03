import os

# -------------------------------
# Read blocked IPs
# -------------------------------
with open("blocked_ips.txt", "r") as ip_file:
    blocked_ips = [line.strip() for line in ip_file]

# -------------------------------
# Read blocked ports
# -------------------------------
with open("blocked_ports.txt", "r") as port_file:
    blocked_ports = [int(line.strip()) for line in port_file]


def firewall(ip, port, protocol):
    print("\n Checking Packet...")

    if ip in blocked_ips and port in blocked_ports:
        return False, "BLOCKED: IP and Port are blocked"

    elif ip in blocked_ips:
        return False, "BLOCKED: IP is blocked"

    elif port in blocked_ports:
        return False, "BLOCKED: Port is blocked"

    elif protocol in ["TCP", "UDP"]:
        return True, "Firewall Access Allowed"

    else:
        return False, "BLOCKED: Rule not matched"


# -------------------------------
# MAIN PROGRAM
# -------------------------------
print("File-Based Firewall Security System")

ip = input("Enter Source IP Address: ")
port = int(input("Enter Destination Port: "))
protocol = input("Enter Protocol (TCP/UDP): ").upper()

allowed, message = firewall(ip, port, protocol)
print(message)

# If firewall allows, move to authentication
if allowed:
    print("\n Redirecting to Authentication System...\n")
    os.system("py authentication.py")
