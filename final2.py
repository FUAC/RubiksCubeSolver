import os,sys,json
import time


path_to_library = os.path.join(os.path.dirname(__file__),"httplib2/python2")
sys.path.append(path_to_library)

import httplib2
import kociemba



def stepper(str):

        http = httplib2.Http()
        url_json = "http://192.168.43.44/stepper"
        headers = {"Content-Type":"application/json; charset=UTF-8"}
        data = {"cube":str}
        response,content = http.request(url_json,"POST",headers=headers,body=json.dumps(data))
        return



file = open("output",'r')
#x = open("output",'r')
x = file.read(54)

y= kociemba.solve(x)

print y

#time.sleep(1)
stepper(y)

file.close()



