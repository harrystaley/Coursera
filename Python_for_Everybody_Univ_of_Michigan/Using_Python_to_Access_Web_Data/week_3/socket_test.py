import socket

new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = 'data.pr4e.org'
port = 80
new_sock.connect((address, port))

req_type = 'GET'
url = 'http://data.pr4e.org/intro-short.txt'
protocol = 'HTTP/1.0'
request = f'{req_type} {url} {protocol}\r\n\r\n'.encode()
new_sock.send(request)

while True:
    data = new_sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

new_sock.close()
