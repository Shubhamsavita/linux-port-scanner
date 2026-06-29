import socket

target = input("Enter IP address or hostname: ")

ports = [21,22,23,25,53,80,110,143,443]

print("\nScanning :", target)

print("-" * 30)

for port in ports:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)

	result = sock.connect_ex((target, port))

	if result == 0:
		print("Port", port, "OPEN")
	else:
		print("Port", port, "CLOSED")
	
	sock.close()





