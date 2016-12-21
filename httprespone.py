import sys
import socket

def resOkHTML(data):
	panjang=len(data)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/plain\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}".format(panjang,data)

	return hasil
