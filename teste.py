import sys
import urllib.request
import json



def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                print(f"Error: Response code{response.status}")
                return
            data = json.loads(response.read().decode())
            if not data:
                print(f"No recent activity found for user '{username}'.")
                return
            print(f"Recent activity for user: {username}")
            for event in data:
                event_type = event.get('type')
                repo_name = event.get('repo', {}).get('name', 'unknown repository')

                if event_type == "PushEvent":
                    commits = len(event.get('payload',{}).get('commits',[]))
                    print(f"- Pushed {commits} commit(s) to {repo_name}")
                elif event_type == "IssuesEvent":
                    action = event.get('payload', {}).get('action', 'performed an action on')
                    print(f"- {action.capitalize()} an issue in {repo_name}")
                elif event_type == "WatchEvent":
                    print(f"- Starred {repo_name}")
                else:
                    print(f"- {event_type} in {repo_name}")
                
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found")
        else:
            print(f"HTTP Error: {e.code}")
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    username = input("Hello tell me the username of github you want: ")

    print(f"Proccesing information of {username}")
    fetch_github_activity(username)

if __name__ == "__main__":
    main()