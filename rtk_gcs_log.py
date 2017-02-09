import socket  
from time import gmtime, strftime 
import matplotlib.pyplot as plt   
import time

filename = raw_input(">>> image name: ") ## customise path here 
filename = filename+ '.png'
x =  []
y =  [] 
s = socket.socket()         
port = 9000                
ip = "192.168.42.1"  #replace with server's ip address
s.connect((ip, port))
print s.recv(1024)

i = 1
a = time.time()

while True:
    try:
        print('receiving data...')
        data = s.recv(1024)
        b = time.time()
        y.append(b-a)
        x.append(i)
        a = b 
        i += 1    
        if not data:
            print("NO DATA RECEIVED")
            break
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime())) 
    except KeyboardInterrupt:   ##windows use Ctrl+c 
        break
s.close()    

plt.plot(x,y)
plt.savefig(filename)
plt.show()
