import os

def nmap_scan(target):
    command = f"nmap -sV {target}"
    os.system(command)

if __name__ == "__main__":
    target = input("Enter target IP/Domain: ")
    nmap_scan(target)