import socket
import threading
from rich.console import Console
from rich.panel import Panel

# Server configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

# Flag to control client loop
running = True

def receive_messages(client_socket):
    console = Console()
    while running:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')

            # Check if server is closing
            if message == 'q':
                print('Server has closed. Exiting...')
                running = False
                break

            # Display the message in a rich panel
            panel = Panel(message, style="bold blue", expand=False)
            console.print(panel)

            # Check if message is "bye" to exit client script
            if message.lower() == 'bye':
                print('Server has closed. Exiting...')
                running = False
                break
        except:
            # Server has disconnected
            client_socket.close()
            break

def start_client():
    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Prompt user for a nickname
    nickname = input("Enter your nickname: ")
    client_socket.send(nickname.encode('utf-8'))

    # Start a new thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while running:
        # Send message to server
        message = input()

        # Check if user wants to exit
        if message
