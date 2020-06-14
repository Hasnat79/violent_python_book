import socket
socket.setdefaulttimeout(2)
s=socket.socket()
s.connect(("192.168.0.100",52595))
ans=s.recv(1024)
print(ans)
#result from mobile ftp is: b'220 SwiFTP V1-200506 ready\r\n'