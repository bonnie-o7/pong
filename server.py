import socketserver
from random import randint
import string
import pickle

alphabet = list(string.ascii_lowercase)

class MyTCPHandler(socketserver.BaseRequestHandler):
    rooms = {}
    clients = {}

    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def create_client_id(self):
        while True:
            dig1 = randint(0, 25)
            dig2 = randint(0, 9)

            id = alphabet[dig1] + str(dig2)
            if id not in self.clients:
                break

        return id

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            self.data = pickle.loads(self.data)

            if self.data['type'] == 'register client':
                id = self.create_client_id()
                self.clients[id] = self.request
                return_message = {'type': 'client id', 'id': id}
                converted_message = pickle.dumps(return_message)
                self.request.sendall(converted_message)
            if self.data['type'] == 'create room':
                code = self.create_code()
                self.rooms[code] = (self.data['client'])
                return_message = {'type': 'room code', 'room code': code}
                converted_message = pickle.dumps(return_message)
                self.request.sendall(converted_message)
    
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
    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
