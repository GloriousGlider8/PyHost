from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import yaml
import colorama as c

hostyml = open("host.yml")
hostSettings = yaml.load(hostyml.read(), Loader=yaml.Loader)
hostyml.close()

hostName = "localhost"
serverPort = int(input("Port: "))
if serverPort == 80:
    raise Exception("Port: 80 is reserved")
file = input("File: ")

hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(serverPort)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        if hostSettings["denylist"].find(str(self.client_address)) and hostSettings["use"] == "deny":
            self.send_error(403, "Blocked IP", "Ask the host to unblock " + str(self.client_address) + " in their host.yml file or PyHost settings.")
            print(c.Fore.YELLOW + "Blocked IP (" + str(self.client_address) + ") attempted to connect!" + c.Style.RESET_ALL)

        if not hostSettings["allowlist"].find(str(self.client_address)) and hostSettings["use"] == "allow":
            self.send_error(403, "Non-whitelisted IP", "Ask the host to allow " + str(self.client_address) + " in their host.yml file or PyHost settings.")
            print(c.Fore.YELLOW + "Non-whitelisted (" + str(self.client_address) + ") attempted to connect!" + c.Style.RESET_ALL)

        self.send_response(hostSettings.get("code"))
        self.send_header("Content-type", hostSettings.get("type"))
        self.end_headers()

        with open(file, "r") as filep:
            self.wfile.write(bytes(filep.read(), "utf-8"))

webServer = HTTPServer((hostName, serverPort), MyServer)
print("Serving at port", serverPort)
print("Type this in your Browser", IP + ":" + str(serverPort))
print("If you are using this device, you can use http://localhost:", str(serverPort), sep="")
print("\nTo stop sharing the file, use [CTRL] + [C]\n")

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()