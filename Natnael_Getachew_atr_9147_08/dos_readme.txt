This program was implemented using the HTTP flood attack method which floods the server with unwithstandable amount
of requests, so that the server cannot respond to actual requests from clients because it's too busy responding to
the requests from the attack.

The program is saved under the file name 'dos.py'.

To start the attack, I have created a bat file called 'start_attack.bat' which contains the command line arguments to
execute the attack. 

The attack is carried out on a node server with a file name 'server.js'. you can start the server by typing
'node server.js' on a command line. 

WARNING: the server depends on Express and the dependency package for Express must be installed on the
device the server is ran on. Otherwise the programm won't work.



Natnael Getachew
ATR/9147/08