# -*- encoding: utf-8 -*-
import json
import ovh
# -*- encoding: utf-8 -*-

try:
        input = raw_input
except NameError:
        pass

import ovh

# create a client using configuration
client = ovh.Client()
client.new_consumer_key_request
# Request RO, /me API access
ck = client.new_consumer_key_request()
ck.add_recursive_rules(ovh.API_READ_WRITE, '/')
#ck.add_rules(ovh.API_READ_ONLY, "/me")

# Request token
validation = ck.request()

print("Please visit %s to authenticate" % validation['validationUrl'])
input("and press Enter to continue...")

# Print nice welcome message
print("Welcome", client.get('/me')['firstname'])
print("Btw, your 'consumerKey' is '%s'" % validation['consumerKey'])
print(validation)

result = client.get('/me/api/credential')

# Pretty print
#print(result)

for i in result:
    delresult = client.delete('/me/api/credential/'+str(i))
    print('Delete +'+str(i))    