import os
import json
import pprint

URL = "https://api.github.com/users/hadley/orgs"


import subprocess
out = subprocess.Popen(['curl','-s', URL],
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
print (stderr)
string_out=stdout.decode("utf-8")
json_out=json.loads(string_out)
pprint.pprint(json_out)