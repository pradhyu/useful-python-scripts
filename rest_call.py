#!/usr/bin/env python3.7
# importing the requests library 
import requests 

# api-endpoint 
URL = "https://api.github.com/users/hadley/orgs"

# location given here 
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

# extracting data in json format 
data = r.json() 

print(data)
