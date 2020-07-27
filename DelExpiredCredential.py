# -*- encoding: utf-8 -*-
import json
import ovh,datetime
def main():
    client = ovh.Client()
    deloldcred(client)
def deloldcred(client):
    result = client.get('/me/api/credential')
    for i in result:
        CredDetail=client.get('/me/api/credential/'+str(i))
        now = datetime.datetime.now()
        if str(CredDetail['expiration']) != "None":
            #
            expire = datetime.datetime.fromisoformat(str(CredDetail['expiration']))
            expire = expire.replace(tzinfo=None)
            #Est ce que le cred est périmé
            if now>expire:
                print('Delete expired Credential :'+str(i))
                client.delete('/me/api/credential/'+str(i))
if __name__ == "__main__":
    main()