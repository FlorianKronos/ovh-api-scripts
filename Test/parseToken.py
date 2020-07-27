# -*- encoding: utf-8 -*-
import sys, getopt, json, ovh, re
from urllib import parse
# Fonctions
def decodeUrl(url=""):
    result = parse.parse_qs(parse.urlsplit(url).fragment)
    id = re.findall('\d+',list(result.keys())[0])[0]
    token = result["token"][0]
    return({'id': str(id), 'token': str(token)})

Geturl = input("Enter URL:")
result = decodeUrl(Geturl)
print('Token : '+result['token']+' ID: '+result['id'])
