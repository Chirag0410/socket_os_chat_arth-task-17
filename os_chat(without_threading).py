import socket
import os
import time

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("!!!!!!!--------!!!!!!!!!----------------!!!!!!!!!------------------!!!!!!!\n")
print("\t\t my Chat Application without multithreading")
print("!!!!!!!--------!!!!!!!!!----------------!!!!!!!!!------------------!!!!!!!\n")
print("hey!!!!..... This is chirag os\n")            
ip=input("Enter your IP: ")
port=int(input("Enter your port number: "))
send_ip=input("Enter sender IP: ")
send_port=int(input("Enter sender port number: "))
s.bind((ip,port))
while True:
  i=input("send message:")
  s.sendto(i.encode(), (send_ip,send_port))
  x=s.recvfrom(1024)
  clientip=x[1][0]

  data=x[0].decode()

  print('\t\t\t\t\t recv message' + clientip + " : " + data)
  if data.decode() == "quit":
            print("Partner is Offline!")
            os._exit(1)
