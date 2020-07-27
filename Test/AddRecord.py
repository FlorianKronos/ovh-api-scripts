# -*- encoding: utf-8 -*-
import sys, getopt, json, ovh

def main(argv):
    zoneDomaine = ''
    sousDomaine = ''
    Cible= ''
    try:
      opts, args = getopt.getopt(argv,"hz:s:t:",["zone=","subdomain=","target="])
    except getopt.GetoptError:
      print ('AddRecord.py -z myDNSZone -s subdomain -t target')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('AddRecord.py -z myDNSZone -s subdomain -t target')
            sys.exit()
        elif opt in ("-z", "--zone"):
            zoneDomaine = arg
        elif opt in ("-s", "--subdomain"):
            sousDomaine = arg
        elif opt in ("-t", "--target"):
            Cible = arg
    client = ovh.Client()
    result = client.post('/domain/zone/'+zoneDomaine+'/record', 
        fieldType='A', # Resource record Name (type: zone.NamedResolutionFieldTypeEnum)
        subDomain=sousDomaine, # Resource record subdomain (type: string)
        target=Cible, # Resource record target (type: string)
        ttl=None, # Resource record ttl (type: long)
    )
    print(json.dumps(result, indent=4))
    result = client.post('/domain/zone/'+zoneDomaine+'/refresh')
    print(json.dumps(result, indent=4))
if __name__ == "__main__":
   main(sys.argv[1:])