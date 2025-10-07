import urllib.request
import json
import sys

# Show commits
# Show issues
# Shows stars
# Handle errors
'''Each endpoint has a path. The REST API reference documentation gives the path for every endpoint. 
For example, the path for the "List repository issues" endpoint is /repos/{owner}/{repo}/issues.
The curly brackets {} in a path denote path parameters that you need to specify. Path parameters modify 
the endpoint path and are required in your request. For example, the path parameters for the "List 
repository issues" endpoint are {owner} and {repo}. To use this path in your API request, replace {repo} 
with the name of the repository where you would 
like to request a list of issues, and replace {owner} with the name of the account that owns the repository.
'''


    # receive a name from user
url = f'https://api.github.com/users/ingrydlorena/events'
res = urllib.request.urlopen(url)

response = json.loads(res).read().decode('utf-8')
# print(json.dumps(res, indent=2))

# for event in res['PushEvent']:
#     print(event['type'])
    

for event in response:
    event_type = event.get('type')
    print(event_type)
    
       

    
 
        
       
    

