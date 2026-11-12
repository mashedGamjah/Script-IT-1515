#write a file
#with open("bcit.txt", "w") as file:
#    file.write("hello")

#read a file
#with open("bcit.txt", "r") as file:
#    data = file.read()
#print(data)

#import pathlib
#pathlib.Path("bcit.txt").write_text("hello")

#from pathlib import Path
#Path("bcit.txt").write_text("hello")

#from http.server import HTTPServer
#("localhost, 8000")
#server = HTTPServer("localhost", 8000)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.wfile.write(b"Hello, World!")


server = HTTPServer(("localhost", 8000), Handler)
servser.serve_forever()
    