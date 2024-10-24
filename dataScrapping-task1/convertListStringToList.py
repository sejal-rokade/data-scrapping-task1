import requests

pUrl='https://httpbin.org/patch'

pHeaders={

    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'user-name' : "['ARC','Vigo']"
     }

dresp=requests.patch(url=pUrl,headers=pHeaders)

jresp=dresp.json()

respHeader=jresp['headers']

print('dresp.content',respHeader['User-Name'],'type= ',type(respHeader['User-Name']))

list=respHeader['User-Name'].split()

print('dresp.content',respHeader['User-Name'],'type= ',type(list))








# print('dresp.content',respHeader['User-Name'],'type= ',type([respHeader['User-Name']]))
# print()

# print('dresp.content',respHeader['User-Name'],'type= ',type({respHeader['User-Name']}))