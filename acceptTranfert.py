# -*- encoding: utf-8 -*-
import sys, argparse, json, ovh, re, datetime,configparser
from urllib import parse
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--url','-u', help='Url recu par email du type https://www.ovh.com/manager/#/useraccount/contacts/123456?tab=REQUESTS&token=monsupertoken')
    args = parser.parse_args()
    print(decodeUrl(args.url))
    client= ovh.Client()
    updateck(client)
    idurl = decodeUrl(args.url)["id"]
    tokenurl = decodeUrl(args.url)["token"]
    #Test if ID is ready to accept
    idstatus = client.get('/me/task/contactChange/{}'.format(idurl))
    if idstatus["state"] == "validatingByCustomers":
        result = client.post('/me/task/contactChange/{}/accept'.format(idurl),token=tokenurl)
        print(result)
    else:
        print("La tache de changeContact : "+str(idurl)+" est en état "+idstatus["state"])
def decodeUrl(url=""):
    # Decode the URL for Id and token for contactChange task
    result = parse.parse_qs(parse.urlsplit(url).fragment)
    id = re.findall('\d+',list(result.keys())[0])[0]
    token = result["token"][0]
    return({'id': str(id), 'token': str(token)})
def getConsumerKey(client):
    #Obtain Consumer Key for script 
    ck = client.new_consumer_key_request()
    ck.add_recursive_rules(ovh.API_READ_WRITE, '/')
    validation = ck.request()
    print("Please visit %s to authenticate" % validation['validationUrl'])
    input("and press Enter to continue...")
    # Print nice welcome message
    print("Welcome", client.get('/me')['firstname'])
    return validation['consumerKey']
def updateck(client):
    #Mise à jour de la CK dans le fichier si besoin
    config = configparser.ConfigParser()
    config.read('ovh.conf')
    endpoint = config["default"]["endpoint"]
    try:
        client.get("/me")
    except (ovh.exceptions.NotCredential,ovh.exceptions.InvalidCredential): # Si la clef CK est non valide alors on en recupere une nouvelle
        config[endpoint]["consumer_key"]= getConsumerKey(client)
        with open('ovh.conf', 'w') as configfile:
            config.write(configfile)
    except :
        print("Erreur non lié à l'autentification de la CK\nVérifier le fichier ovh.conf")
        quit   
    else:
        print("Welcome", client.get('/me')['firstname'])
        return True
if __name__ == "__main__":
   main(sys.argv[1:])