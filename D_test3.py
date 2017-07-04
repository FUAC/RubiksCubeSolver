import os,sys,json
import time


path_to_library = os.path.join(os.path.dirname(__file__),"httplib2/python2")
sys.path.append(path_to_library)

import httplib2
import kociemba



def stepper(str):

        http = httplib2.Http()
        url_json = "http://192.168.1.102/stepper"
        headers = {"Content-Type":"application/json; charset=UTF-8"}
        data = {"cube":str}
        response,content = http.request(url_json,"POST",headers=headers,body=json.dumps(data))
        return



													#file = open("output",'r')
#x = open("output",'r')
													#x = file.read(54)

													#y= kociemba.solve(x)
#y="D2 R' D' F2 B D R2 D2 R' F2 D' F2 U' B2 L2 U2 D R2 U"
y="U' R2 D' U2 L2 B2 U F2 D F2 R D2 R2 D' B' F2 D R D2"
#y=" B2"
print y

#time.sleep(1)
stepper(y)

														#file.close()



