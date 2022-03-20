import socket
import threading


PORT = 5050
# Limit of bytes a single stream will hold (64 bytes)
HEADER = 64
# Obtains the IP address of the local device running on a local network
SERVER = socket.gethostbyname(socket.gethostname())
print("This is the name of the my local device:", socket.gethostname())
print("This is the IP address of my local device:", SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Disconnecting from server..."

# ~Setting up the configuration of the server~
# FAMILY - AF_INET: Accept over the internet
# TYPE - SOCK_STREAM: Stream data over the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding the address to the server
server.bind(ADDR)


# Function that will handle the connection between 1 singular client and the sever
def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")

    connected = True

    while connected:
        # Wait to receive information from the client
        # ~PROTOCOL~
        # Obtaining the length of the message and decoding it from bytes --> utf-8 (string format)
        message_length = connection.recv(HEADER).decode(FORMAT)

        # Checking that the message length actually contains content and isn't empty
        if message_length:
            # Converting the string length into a integer
            message_length = int(message_length)
            # Obtaining the actual message in a string
            message = connection.recv(message_length).decode(FORMAT)
            # Check if client is still connected to the server
            if message == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{address}] {message}")
            connection.send("Message received.".encode(FORMAT))
    # Disconnect client from server
    connection.close()


# Function that will start the server and connections to the client(s)
def start():
    # Listening for new connections
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # |Blocking state|
        # Whenever a new connection is found,
        # 1) Store the address of the new connection
        # 2) Store the object of.....
        connection, address = server.accept()

        # Starting a new thread
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


# ~BEGINNING OF THE PROGRAM~
# Starting the server
print("\n[STARTING] server is starting...")
start()