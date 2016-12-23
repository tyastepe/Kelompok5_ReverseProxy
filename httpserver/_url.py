import _maincontrol
import _httpresponse

pattern={}
pattern['/']=_maincontrol.index
pattern['res']=_maincontrol.resource
pattern['404']=_httpresponse.res404()

