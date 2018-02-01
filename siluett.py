#!/usr/bin/env python3

import time
import requests
import json
import re
import sys

filename = "input.txt"

# let's make sure every input line is just numbers

pattern = re.compile("^[0-9]+$")

with open(filename) as f:
    lines = [line.strip().strip('\n') for line in open(filename)]
			
def get_nplid_row(nplid):
    url = ("https://silonline.silinfo.se/sil_cache_api/search?q=" + nplid)
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, verify=False) # sorry
    data = json.loads(response.text)
    
    ##
    ## The list of interesting JSON values for our CSV row starts here
    ## 
    
    try:
        distributedTradeName = str(data["items"][0]["distributedTradeName"])
    except KeyError:
        distributedTradeName = 'NULL'

    ## You could fetch any amount of values here, but every nplid can give one or several "items".
    ## The scope/purpose here is to figure out what the market name of a certain nplid actually is,
    ## so we are grabbing the first "distributedTradeName" in the first item.

    return_string = str(nplid) + ';' + \
                    distributedTradeName + ';'

    return return_string;

print('NPLID;Handelsnamn;') #print header

# loop over the lines of the input file and print CSV formatted values for nplid and the name

for i in lines:
    if pattern.match(i): 
            print(get_nplid_row(i))