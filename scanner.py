
import socket
from datetime import datetime

# Target configuration
target = input("Enter target IP address: ")

# Scan configuration
start_port = 11430
end_port = 11440

print("\n" + "=" * 55)
print(f"TARGET: {target}")
print(f"PORT RANGE: {start_port}-{end_port}")
print(f"STARTED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 55)

open_ports = []

try:
    # Scan ports
    for port in range(start_port, end_port + 1):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Unknown"

            print(f"[+] Port {port:<6} OPEN | Service: {service}")
            open_ports.append(port)

        sock.close()

except KeyboardInterrupt:
    print("\n[!] Scan interrupted by user.")

except socket.gaierror:
    print("[!] Hostname could not be resolved.")

except socket.error as error:
    print(f"[!] Connection error: {error}")

# Results
print("\n" + "=" * 55)
print(f"SCAN COMPLETED")
print(f"Open ports found: {len(open_ports)}")
print("=" * 55)

if open_ports:
    print("Open ports:", ", ".join(map(str, open_ports)))
else:
    print("No open ports found.")
