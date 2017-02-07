import socket  
from time import gmtime, strftime             

s = socket.socket()         
port = 12345                
ip = "192.168.420"
s.connect(ip, port)
print s.recv(1024)
## write the incoming message to a file 
with open('received_file.txt', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime())+': data=%s',(data))      
        if not data:
        	print("NO DATA RECEIVED")
        	break
        # write data to a file
        f.write(data)

print('Successfully get the file')

s.close()    
 