from github import Github, Auth
from dotenv import dotenv_values

class GitHubApi:
    time_format = "%y/%m/%d %H:%M:%S"
    config = dotenv_values(".env.github")
    auth = Auth.Token(config.get("ACCESS_TOKEN", ""))
    g = Github(auth=auth)
    
    def get_events_filter_type_and_datetime(self, type, time):
        events = self.get_user_events_as_list()
        events = [e for e in events if e.type == type and e.created_at > time ]
        return events
    
    def get_events(self):
        return self.g.get_user(self.config.get("USERNAME", "")).get_events()
    
    def get_user_events_as_list(self):
        eventsList = []
        events = self.g.get_user(self.config.get("USERNAME", "")).get_events()
        i = 0
        while True: 
            toAppend = events.get_page(i)
            if toAppend == []:
                break
            else:
                eventsList.extend(toAppend)
            i += 1
        return eventsList