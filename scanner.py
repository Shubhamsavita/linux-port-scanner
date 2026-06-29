import socket
import time

target = input("Enter IP address or hostname: ")

try:
	ip = socket.gethostbyname(target)
except socket.gaierror:
	print("Invalid hostname or IP address.")
	exit()

ports = [21,22,23,25,53,80,110,143,443]

services = {
21: "FTP",
22: "SSH",
23: "TELNET",
25: "SMTP",
53: "DNS",
80: "HTTP",
110: "POP3",
143: "IMAP",
443: "HTTPS"
}

print("\n===============================")
print("  Netwrok Port Scanner  ")
print("================================")
print("Target	:", target)
print("IP	:", ip)
print()

start = time.time()

for port in ports:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)

	result = sock.connect_ex((ip, port))

	status = "OPEN" if result == 0 else "CLOSED"
	
	print(f"{port:<5} {services[port]:<10} {status}")
	
	sock.close()

end = time.time()

print("\nScan Completed in {:.2f} seconds".format(end - start))






