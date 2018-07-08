#!/usr/bin/env python
import threading, time, socket, sys, random
import SocketServer
from base64 import b64encode

flag       = "MNZ{64IsTheBestBase==}"
notTheFlag = "Better luck next time!"
CHUNKS     = 20
CHANCE     = 0.15
PORT       = 6646
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def setup(self):
        print("Connected TO {}".format(self.client_address))
        try:
            fh = open("/dev/urandom","rb")
            chunk = random.randint(1, CHUNKS)
            for i in range(0, CHUNKS):
                output = b64encode(fh.read(22))
                self.request.sendall("{}\n".format(output))
                if i == chunk:
                    rand = random.random()
                    output = flag if rand < CHANCE else notTheFlag
                    print output
                    output = b64encode(output)
                    self.request.sendall("{}\n".format(output))
                time.sleep(0.1)
        except socket.error as e:
            print "Socket error {} - {}".format(e.errno, self.client_address)
        finally:
            fh.close()
    def handle(self):
       pass 
    def finish(self):
        print "Closed connection to {}".format(self.client_address)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST = "0.0.0.0"

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
    #server.shutdown()
    #server.server_close()
    while ( True ):
        server.handle_request()
        try:    
            server.get_request()
        except KeyboardInterrupt:
	    print "Server Stopping"
            server.shutdown()
            server.server_close()
            break
