from github import Github, Auth
from dotenv import dotenv_values

class GitHubApi:
    time_format = "%y/%m/%d %H:%M:%S"
    config = dotenv_values(".env.github")
    auth = Auth.Token(config.get("ACCESS_TOKEN", ""))
    g = Github(auth=auth)
    
    def get_events_filter_type_and_datetime(self, type, time):
        events = self.get_events().get_page(0)
        events = [e for e in events if e.type == type and e.created_at > time ]
        return events
    
    def get_events(self):
        return self.g.get_user(self.config.get("USERNAME", "")).get_events()
    