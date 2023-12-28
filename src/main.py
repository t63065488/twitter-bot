import tweet
import datetime
from github_api import GitHubApi
import sys

def main(args):
    g = GitHubApi()
    time = datetime.datetime.now().astimezone(datetime.UTC) - datetime.timedelta(days=7)
    events = g.get_events_filter_type_and_datetime("PushEvent", time)
    for event in events:
        print(event.created_at)
        print(event.payload)
    print('do stuff')
    
if __name__ == "__main__":
    main(sys.argv[1:])