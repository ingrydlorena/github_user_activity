import requests
import sys

''' requirements
[] List public events
[] The private timeline for the authenticated user
[] List watchers
[] Create repositories
[] Commit
[] 
https://github.com/AmanDevelops/python-mini-projects/blob/main/GitHub%20User%20Activity/utils.py
'''

class Summarizer:
    CURRENT_SUPPORTED_EVENTS = (
        "PushEvent",
        "IssuesEvent",
        "WatchEvent",
        "PullRequestEvent"
 )
    
    def __init__(self):
        self.summary = {
            "pushEvent": {

            },
            "issuesEvent": {

            },
            "watchEvent": {

            },
            "PullRequestEvent": {

            }
        }
    
    def PushEvent(self, event):
        repo_name = event["repo"]["name"]
        self.summary["pushEvent"][repo_name] = (
            self.summary["pushEvent"].get(repo_name, 0) + 1
        )
    
    def IssuesEvent(self, event):
        action = event['payload']['action']
        repo_name = event['repo']['name']

        if action not in self.summary['issuesEvent']:
            self.summary['issuesEvent'][action] = {}

        current_issues_count = self.summary['issuesEvent'][action].get(repo_name, 0)

        self.summary['issuesEvent'][action][repo_name] = current_issues_count + 1
    
    def WatchEvent(self, event):
        self.summary['watchEvent'].append(event['repo']['name'])
    
    def PullRequestEvent(self, event):
        action = event['payload']['action']
        repo_name = event['repo']['name']

        if action not in self.summary['PullRequestEvent']:
            self.summary['PullRequestEvent'][action] = {}
        
        current_pr_count = self.summary['PullRequestEvent'][action].get(repo_name, 0)
        self.summary['PullRequestEvent'][action][repo_name] = current_pr_count + 1

    def summarize(self, username):
        eventsResponse = requests.get(f'https://api.github.com/users/{username}/events')

        if not eventsResponse.ok:
            error_message = eventsResponse.json()
            print(
                f"[ERROR {error_message.get('status')}]: {error_message.get('message')}"
            )
            return
        events = eventsResponse.json()

        for event in events:
            event_type = event.get('type')
            if event_type not in self.CURRENT_SUPPORTED_EVENTS:
                continue

            handler = getattr(self.event_type, None)
            if handler:
                handler(event=event)
        
        print(f"Here is the recent activities of {username}:\n")

        for event_type, event_summary_data in self.summary.items():
            if not event_summary_data:
                continue
            if event_type == "pushEvent":
                print('Commits: ')
                for repo_name, number_of_commits in event_summary_data.items():
                    print(
                        f"- Pushed {number_of_commits} commits to {repo_name}"
                    )
                    
            elif event_type == "issuesEvent":
                print("Issues: ")
                for action_type, repos in event_summary_data.items():
                    for repo_name, count in repos.items():
                        print(f"- {action_type} {count} issue in {repo_name}")

            elif event_type == "watchEvent":
                print("Stars: ")
                for i in event_summary_data:
                    print(f"- Starred {i}")

            elif event_type == "PullRequestEvent":
                print("Pull Request: ")
                for action_type, repos in event_summary_data.items():
                    for repo_name, count in repos.items():
                        print(f"- {action_type} {count} pull request in {repo_name}")

if __name__ == "__main__":
    try:
        username = sys.argv[1]
        summarizer = Summarizer()
        summarizer.summarize(username=username)
    except IndexError:
        print("Please provide a username")