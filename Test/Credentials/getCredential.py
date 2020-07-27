# -*- encoding: utf-8 -*-
import json
import ovh,datetime

client = ovh.Client()
result = client.get('/me/api/credential')

# Pretty print
#print(result)
for i in client.get('/me/api/credential'):
    CredDetail=client.get('/me/api/credential/'+str(i))
    now = datetime.datetime.now()
    print('CredentiallID : '+str(CredDetail['credentialId']))
#    print('Application : '+str(CredDetail['applicationId'])+'\n')

    try:
        appliname = client.get('/me/api/application/'+str(CredDetail['applicationId']))["name"]
    except:
        appliname = "Application externe"
    finally:
        print('Application : '+appliname,end='\n\n')
        
    

    