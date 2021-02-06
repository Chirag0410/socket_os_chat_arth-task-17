import socket as s
import threading as thd
import os
print("!!!!!!!!!!!!--------welcome here--------!!!!!!!!!!!")
print("-!-!-!-!-!-!-! i am chirag -----------------!!!!!!!!!!")
# Create a Socket and Bind IP and PORT to It
skt = s.socket(s.AF_INET, s.SOCK_DGRAM)
localIP = input("Enter Your IP: ")
port= int(input("enter port :"))
skt.bind((localIP, port))

# Get Partner's IP to chat with
usrIP = input("Enter Partner IP: ")
usrport=int(input("enter user port :"))
print()

# Function to Recieve and Print the Message
def recv_msg():
    while True:
        msgRcv = skt.recvfrom(1024)
        if msgRcv[0].decode() == "quit":
            print("Partner is Offline!")
            os._exit(1)
        print(msgRcv[1][0] + ": " + msgRcv[0].decode())

# Function to Send the Message
def send_msg():
    while True:
        data = input().encode()
        msgSent = skt.sendto(data, (usrIP, usrport))
        if data.decode() == "quit":
            os._exit(1)

# Thread for Send Message Function
send_thd = thd.Thread(target=send_msg)

# Threads for Recieve Message Function
rcv_thd = thd.Thread(target=recv_msg)

# Starting Threads
send_thd.start()
rcv_thd.start()
