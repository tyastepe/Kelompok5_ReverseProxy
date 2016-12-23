
import socket
import sys
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 8080)

sock.bind(server_address)


sock.listen(1)

def http_get(message_yang_diteruskan,target):
	client_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = target
	client_socket.connect(server_address)
	try:
		message =  message_yang_diteruskan+"\r\n\r\n"
	    	client_socket.sendall(message)
	    	data_respon = ""
	    	data_dari_server = client_socket.recv(32)
		data_respon = data_respon+data_dari_server
	    	while data_dari_server:
			data_dari_server = client_socket.recv(32)
			data_respon = data_respon+data_dari_server
		
	finally:
		client_socket.close()
		return data_respon




def layani_client(koneksi_client,alamat_client):
    try:
	request_message=''
	while True:
           data = koneksi_client.recv(64)
	   data = bytes.decode(data)
           request_message = request_message+data
	   if (request_message[-4:]=="\r\n\r\n"):
		break


       	baris = request_message.split("\r\n")
       	baris_request = baris[0]
       #baris_host = baris[1]
       	a,url,c = baris_request.split(" ")
	url=url[1:]
       	ext=url.split('/')[0]
	target=''
	print url.split('/')
	if ext=='mp3':
		target=('localhost',13001)
	else:	 
		target=('localhost',13000)
       	koneksi_keluar = http_get(request_message,target)
       	respon = koneksi_keluar
	#print respon
       	koneksi_client.send(respon)
    finally:
        
        koneksi_client.close()


while True:
    
    print >>sys.stderr, 'waiting for a connection'
    koneksi_client, alamat_client = sock.accept()
    s = threading.Thread(target=layani_client, args=(koneksi_client,alamat_client))
    s.start()


