import tweet
import datetime
from github_api import GitHubApi
import sys


def main(args):
    g = GitHubApi()
    time = datetime.datetime.now().astimezone(datetime.UTC) - datetime.timedelta(days=7)
    events = g.get_events_filter_type_and_datetime("PushEvent", time)
    repo_ids = get_unique_repo_ids(events)
    repos = []
    for id in repo_ids:
        repos.append((id, g.get_repo_name(id), [e.payload.get("commits") for e in events if e.payload.get('repository_id') == id]))
        
        
def get_unique_repo_ids(events):
    id_set = set()
    for event in events:
        id_set.add(event.payload.get('repository_id'))
    return id_set
    

if __name__ == "__main__":
    main(sys.argv[1:])