import socket
import sys
import threading

#inisialisasi
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#proses binding
server_address = ('localhost', 13000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#listening
sock.listen(1)

def layani_client(koneksi_client,alamat_client):
	try:
		
		request_message = ''
       		while True:
           		data = koneksi_client.recv(64)
	   		data = bytes.decode(data)
           		request_message = request_message+data
	   		if (request_message[-4:]=="\r\n\r\n"):
				break

       		baris = request_message.split("\r\n")
       		baris_request = baris[0]
       		#print baris_request
 	
       		a,url,c = baris_request.split(" ")
       
       		print a
		print url
		print c


       #koneksi_client.send(respon)
	finally:
        # Clean up the connection
        	koneksi_client.close()


while True:
    # Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	koneksi_client, alamat_client = sock.accept()
	s = threading.Thread(target=layani_client, args=(koneksi_client,alamat_client))
    	s.start()
