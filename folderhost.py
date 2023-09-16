# import necessary modules
 
# for implementing the HTTP Web servers
import http.server
 
# provides access to the BSD socket interface
import socket

# a framework for network servers
import socketserver

# to access operating system control
import os

# assigning the appropriate port value
PORT = int(input("Port number: "))
# this finds the name of the computer user
os.environ['USERPROFILE']


# changing the directory to access the files desktop
# with the help of os module
desktop = input("Folder: ")
os.chdir(desktop)
 
 
# creating a http request
Handler = http.server.SimpleHTTPRequestHandler
# returns, host name of the system under
# which Python interpreter is executed
hostname = socket.gethostname()
 
  
# finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP
 
# continuous stream of data between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("\n")
    print("Serving at port", PORT)
    print("Type this in your Browser", IP)
    print("If you are using this device, you can use http://localhost:", PORT, sep="")
    print("\nTo stop sharing the folder, use [CTRL] & [C]\n")
    httpd.serve_forever()