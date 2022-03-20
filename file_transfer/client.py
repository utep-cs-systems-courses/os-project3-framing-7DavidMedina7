import socket

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


def send(msg):
    # ~PROTOCOL~
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    # Padding the message so that it is 64 bytes
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello OS!")
input()
send("Hello David!")
input()
send(DISCONNECT_MESSAGE)