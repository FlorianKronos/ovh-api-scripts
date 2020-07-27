# -*- encoding: utf-8 -*-
import json,sys,configparser,ovh
def main(argv):
    client = ovh.Client()
    updateck(client)
#
# #
def getConsumerKey(client):
    ck = client.new_consumer_key_request()
    ck.add_recursive_rules(ovh.API_READ_WRITE, '/')
    #ck.add_rules(ovh.API_READ_ONLY, "/me")
    # Request token
    validation = ck.request()
    print("Please visit %s to authenticate" % validation['validationUrl'])
    input("and press Enter to continue...")
    # Print nice welcome message
    print("Welcome", client.get('/me')['firstname'])
    return validation['consumerKey']


#Verification si la CK fournise est OP
def updateck(client):
    config = configparser.ConfigParser()
    config.read('ovh.conf')
    endpoint = config["default"]["endpoint"]
    try:
        result=client.get("/me")
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