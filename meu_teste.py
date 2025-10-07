import urllib.request
import json

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
url = f'https://api.github.com/users/wesleysouza13/events'
res = urllib.request.urlopen(url)

response = json.loads(res.read().decode('utf-8'))
    

for event in response[:10]:
    event_type = event.get('type')
    repository_name = event.get('repo', {}).get('name', 'unknown repository')
    if event_type == 'PushEvent':
        commits = len(event.get('payload', {}).get('commits', []))
        print(f"- Pushed {commits} commits to {repository_name}")
    elif event_type == 'IssuesEvent':
        action = event.get('payload', {}).get('action', 'performed an action on')
        print(f"- {action.capitalize()} an issue in {repository_name}")
    elif event_type == 'WatchEvent':
        print(f"- Starred {repository_name}")
    else:
        print(f"- {event_type} in {repository_name}")
    


    
    
       

    
 
        
       
    

