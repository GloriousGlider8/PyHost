# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

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
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open(file, "r") as filep:
            self.wfile.write(bytes(filep.read(), "utf-8"))
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Serving at port", serverPort)
    print("Type this in your Browser", IP + ":" + str(serverPort))
    print("If you are using this device, you can use http://localhost:", str(serverPort), sep="")
    print("\nTo stop sharing the file, use [CTRL] & [C]\n")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()