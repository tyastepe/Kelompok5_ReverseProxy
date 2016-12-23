import os.path
import _httpresponse

ext_audio=['mp3']

def index(url):
	f=open('html/index.html').read()
	return _httpresponse.resOKHTML(f)

def resource(url):
	url=url[1:]
	print url
	tipe=url.split('/')[0]

	if os.path.isfile('html/'+url):
		f=open('html/'+url).read()

		if tipe in ext_audio:
			return _httpresponse.resOKMp3(f)
		else:
			return _httpresponse.resOKFile(f,tipe)
	else:
		return _httpresponse.res404()
