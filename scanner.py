import socket
import time

# Get target
target = input("Enter Targat (Hostname/IP): ")

# Resolve hostname
try:
	ip = socket.gethostbyname(target)
except socket.gaierror:
	print("Invalid hostname or IP address.")
	exit()

# Get port range
start_port = int(input("Enter Start Port : "))
end_port = int(input("Enter End Port : "))


print("\n===============================")
print(" Linux Netwrok Port Scanner  ")
print("================================")
print("Target	:", target)
print("IP	:", ip)
print("Range	:", start_port,"-",end_port)
print()
start_time = time.time()

open_ports = []

for port in range(start_port, end_port+1):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.5)

	result = sock.connect_ex((ip, port))

	if result == 0:
		print("Port {} OPEN".format(port))
		open_ports.append(port)
	
	sock.close()

end_time = time.time()

print("\n=================================")
print("Scan Completed")
print("==================================")
print("Open Ports :", len(open_ports))
print("\nTime Taken : {:.2f} seconds".format(end_time - start_time))






