import http.server
import socket
import socketserver
import os
import yaml
import colorama as c

hostyml = open("host.yml")
hostSettings = yaml.load(hostyml.read(), Loader=yaml.Loader)
hostyml.close()

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
    if hostSettings["denylist"].find(str(Handler.client_address)) and hostSettings["use"] == "deny":
            Handler.send_error(403, "Blocked IP", "Ask the host to unblock " + str(Handler.client_address) + " in their host.yml file or PyHost settings.")
            print(c.Fore.YELLOW + "Blocked IP (" + str(Handler.client_address) + ") attempted to connect!" + c.Style.RESET_ALL)

    if not hostSettings["allowlist"].find(str(Handler.client_address)) and hostSettings["use"] == "allow":
        Handler.send_error(403, "Non-whitelisted IP", "Ask the host to allow " + str(Handler.client_address) + " in their host.yml file or PyHost settings.")
        print(c.Fore.YELLOW + "Non-whitelisted (" + str(Handler.client_address) + ") attempted to connect!" + c.Style.RESET_ALL)

    print("\n")
    print("Serving at port", PORT)
    print("Type this in your Browser", IP)
    print("If you are using this device, you can use http://localhost:", PORT, sep="")
    print("\nTo stop sharing the folder, use [CTRL] + [C]\n")
    httpd.serve_forever()