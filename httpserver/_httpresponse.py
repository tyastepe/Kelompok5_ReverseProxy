import sys
import socket

def resOKHTML(data):
	panjang=len(data)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/html\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}".format(panjang,data)

	return hasil

def res404():
	data=open('html/404.html').read()

	panjang=len(data)
	hasil = "HTTP/1.1 404 Not Found\r\n" \
		"Content-Type: text/html\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}".format(panjang,data)
	return hasil

def resOKFile(data,tipe):
	panjang=len(data)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/{}\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}".format(tipe,panjang,data)

	return hasil

def resOKGambar(data,tipe):
	panjang=len(data)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: image/{}\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}".format(tipe,panjang,data)

	return hasil
