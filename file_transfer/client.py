import socket
import os
from file_archiver import *


# Limit of bytes a single stream will hold (64 bytes)
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Disconnecting from server..."
# Obtains the IP address of the local device running on a local network
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# ~Setting up the configuration of the server~
# FAMILY - AF_INET: Accept over the internet
# TYPE - SOCK_STREAM: Stream data over the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting the client to the server
client.connect(ADDR)


# Function that will send the file to the server
def send(msg):
    # ~PROTOCOL~
    # Checking for DISCONNECT_MESSAGE
    if msg == DISCONNECT_MESSAGE:
        msg = msg.encode()

    # message = msg.encode(FORMAT)
    message_length = len(msg)
    send_length = str(message_length).encode(FORMAT)
    # Padding the message so that it is 64 bytes
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)
    print(client.recv(2048).decode(FORMAT))


# Function that sends the name of the file to the server
def send_name_of_file_to_server(name_of_file):
    return name_of_file


# ~BEGINNING OF THE PROGRAM (CLIENT SIDE)~
SEND_ANOTHER_FILE = True
while SEND_ANOTHER_FILE:
    # Asking the user what text file they wish to send
    path_of_text_file = input("\nEnter the name of the text file you want to send: ")
    print("This is the text file you want to send:", path_of_text_file)

    # Checking that the file entered exists
    if os.path.exists(path_of_text_file):
        # Encoding the text file
        encoded_file = archive_file(path_of_text_file)

        # Obtaining the size of the file to be sent
        size_of_file = len(encoded_file)

        # Sending the encoded file to the server
        send(encoded_file)

    # Prompting the user if they wish to continue sending files to the server
    user_response = input("\nDo you wish to send another file? (Y/N)")
    if user_response == "Y":
        SEND_ANOTHER_FILE = True
    elif user_response == "N":
        SEND_ANOTHER_FILE = False
        # Disconnect this particular client from the server
        send(DISCONNECT_MESSAGE)