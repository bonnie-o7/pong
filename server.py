import socketserver
from random import randint
import string

alphabet = list(string.ascii_lowercase)

class MyTCPHandler(socketserver.BaseRequestHandler):
    rooms = {}

    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        pass
    
    def create_code(self):
        while True:
            dig1 = randint(0, 25)
            dig2 = randint(0, 9)
            dig3 = randint(0, 25)
            dig4 = randint(0, 9)

            code = alphabet[dig1] + str(dig2) + alphabet[dig3] + str(dig4)
            if code not in self.rooms:
                break

        return code

if __name__ == "__main__":
    HOST, PORT = "localhost", 65432

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
