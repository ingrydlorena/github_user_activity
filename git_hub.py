from urllib.request import Request, urlopen
import json
import sys

# Show commits
# Show issues
# Shows stars
# Handle errors


class Git_Hub:
    # receive a name from user
    def __init__(self, username):
        self.url_git = f'https://api.github.com/users/{username}/events'
        self.headers = {"User-Agent": "Oython-urllib"}
        

    # search recent activity    
    def recent_activity(self):
        request = Request(self.url_git, headers=self.headers)
        response = urlopen(request)
        
       
    


obj = Git_Hub(username=sys.argv[1])
resposta = obj.recent_activity()
lendo = resposta.read()

for le  in lendo:
    print(le.key())