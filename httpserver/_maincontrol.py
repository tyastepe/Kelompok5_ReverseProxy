import os.path
import _httpresponse

ext_gambar=['jpg','png']

def index(url):
	f=open('html/index.html').read()
	return _httpresponse.resOKHTML(f)

def resource(url):
	url=url[1:]
	print url
	tipe=url.split('/')[0]

	if os.path.isfile('html/'+url):
		f=open('html/'+url).read()

		if tipe in ext_gambar:
			return _httpresponse.resOKGambar(f,tipe)
		else:
			return _httpresponse.resOKFile(f,tipe)
	else:
		return _httpresponse.res404()
