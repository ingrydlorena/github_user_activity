import urllib.request
import json
import urllib.error
import sys

def git(username):
    url = f'https://api.github.com/users/{username}/events'
    try:

        data = urllib.request.urlopen(url)
        if not data:
            print(f"No recent activity found for user '{username}'")
            return 
        response = json.loads(data.read().decode('utf-8'))

        for event in response[:10]:
            event_type = event.get('type')
            repository_name = event.get('repo', {}).get('name', 'unknown repository')

            match event_type:
                case 'PushEvent':
                    commits = len(event.get('payload', {}).get('commits', []))
                    print(f"- Pushed {commits} commits to {repository_name}")
                case 'IssuesEvent':
                    action = event.get('payload', {}).get('action', 'performed an action on')
                    print(f'- {action.capitalize()} an issue in {repository_name}')
                case 'WatchEvent':
                    print(f"- Starred {repository_name}")
                case _:
                    print(f"- {event_type} in {repository_name}")

    except urllib.error.HTTPError as http_error:
        if http_error.code == 404:
            print(f"{username} not found")
        else:
            print(f"Http Error: {http_error.code}")
    except urllib.error.URLError as url_error:
            print(f"Network error: {url_error.reason}")
    except Exception as error:
        print(f"Got a unexpected error: {error}")

if __name__ == '__main__':
    git(username= sys.argv[1])


    
    
       

    
 
        
       
    

