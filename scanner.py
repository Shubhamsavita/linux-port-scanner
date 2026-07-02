import socket
import time

# Get target from user
target = input("Enter Targat (Hostname/IP): ")

# Resolve hostname to IP
try:
	ip = socket.gethostbyname(target)
except socket.gaierror:
	print("Invalid hostname or IP address.")
	exit()

# Get port range
start_port = int(input("Enter Start Port : "))
end_port = int(input("Enter End Port : "))


print("\n=======================================")
print("  Linux Network Port Scanner  ")
print("========================================")
print("Target	:", target)
print("IP	:", ip)
print("Range	:", start_port,"-",end_port)
print()

start_time = time.time()

#List to store open ports
open_ports = []

# Create report file
report = open("scan_report.txt", "w")

report.write("===================================\n")
report.write("  Network Port Scanner Report\n")
report.write("==================================\n")
report.write("Target	: {}\n".format(target))
report.write("IP Address: {}\n".format(ip))
report.write("Port Range: {} - {}\n\n".format(start_port,end_port))

# Scan Ports
for port in range(start_port, end_port+1):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.5)

	result = sock.connect_ex((ip, port))

	if result == 0:
		print("Port {} OPEN".format(port))
		open_ports.append(port)
	
	sock.close()

end_time = time.time()
# Print Summary
print("\n=================================")
print("   Scan Completed")
print("==================================")
print("Total Open Ports :", len(open_ports))
print("\nTime Taken : {:.2f} seconds".format(end_time - start_time))
print("Report saved as : scan_report.txt")

# Save Summary To Report
report.write("\n===============================\n")
report.write("  Scan Summary\n")
report.write("================================\n")
report.write("Total Open Ports : {}\n".format(len(open_ports)))
report.write("Time taken 	: {:.2f} seconds \n".format(end_time - start_time))
report.close()






