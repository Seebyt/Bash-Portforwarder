import socket
import subprocess

print("**********************")
print("* BASH PORT-FORWARDER*")
print("**********************")
print()
print("Use this to forward incoming traffic to another machine!")
print()

destination = socket.gethostbyname(socket.gethostname())

protocol = input("tcp or udp?").lower()

port = input("port or portrange? (i.e. 22 or 41000-41029)")

todest = input("destination ip?")

print()
print("processing...")
print()

bashCommand = f"sudo iptables -t nat -I PREROUTING 1 -d {destination} -p {protocol} --dport {port} -j DNAT --to-dest {todest}:{port} & sudo iptables -t nat -I POSTROUTING 1 -d {todest} -p {protocol} --dport {port} -j SNAT --to-source {destination} & sudo iptables -I FORWARD 1 -d {todest} -p {protocol} --dport {port} -j ACCEPT & sudo iptables-save"

try:
    subprocess.run(bashCommand, check=True, text=True, shell=True)

except:
    print("Something went wrong, try with sudo")

else:
    print("Rule created successfully!")
    print("Bye Bye!")
    exit()
