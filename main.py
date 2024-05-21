import socket
 
 
def scan_ports(target_host):
   try:
       target_ip = socket.gethostbyname(target_host)
   except socket.gaierror:
       print("Could not find IP address for the hostname.")
       return []
 
 
   open_ports = []
 
 
   for target_port in range(1, 1025):
       try:
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.bind((target_ip, target_port))
           sock.close()
       except socket.error:
           open_ports.append(target_port)
           print("open port", target_port)
 
 
   return open_ports
 
 
def main():
   target_host = input("Please enter the target host to scan: ")
   open_ports = scan_ports(target_host)
 
 
   print("Open ports:")
   if open_ports:
       print(open_ports)
   else:
       print("None")
 
 
if __name__ == "__main__":
   main()
