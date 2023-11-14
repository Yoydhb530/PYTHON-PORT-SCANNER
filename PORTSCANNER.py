import socket
import sys
from datetime import datetime

 
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

ag = sys.argv
tr = socket.gethostbyname(sys.argv[1]) 
print(f'''{GREEN}
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{RESET}
                                                                                      {RED}  by NotYou{RESET}               

''')
print(f"{RED}════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
print(f'start scaning On : {tr}')
print("Scanning started at : " + str(datetime.now()))
print("For stop type : ^C")
print(f"{RED}════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")

if len(sys.argv) == 2:
     
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid amount of Argument")
 
try:
    for port in range(1,65535):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        res = soc.connect_ex((ag[1], port))
        if res ==0:
            print(f"{GREEN}{port} : [OPEN] {socket.getservbyport(port)}{RESET}")
        soc.close()

except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()