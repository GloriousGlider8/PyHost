import http.server
import socket
import socketserver
import os

PORT = int(input("Port number: "))
os.environ['USERPROFILE']

desktop = input("Folder: ")
os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("\n")
    print("Serving at port", PORT)
    print("Type this in your Browser", IP)
    print("If you are using this device, you can use http://localhost:", PORT, sep="")
    print("\nTo stop sharing the folder, use [CTRL] + [C]\n")
    httpd.serve_forever()