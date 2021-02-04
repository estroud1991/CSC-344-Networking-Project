import http.server
import socketserver

#Creats a port and handler to handle simple HTTP request
PORT = int(input("Enter a port to use: "))
Handler = http.server.SimpleHTTPRequestHandler


#Opens the TCP port and hosts the contents of the folder this file is contained in
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
