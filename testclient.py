import pynetwork as pn

host = "127.0.0.1"
port = 9090

# Create a "client" object
client = pn.ClientConnection(host, port)
# Connect to the server
client.connect()
# Receive a message
msg = client.recieve_from_server(1024)
# Print it out
print(msg)
# Reply back
msgback = input("Message: ")
client.send_to_server(msgback)
