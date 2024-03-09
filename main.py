from server import Server

server_config = {
    "host": "127.0.0.1",
    "port": "8080",
}
server = Server(server_config)
server.run()