# 1. Receive a GitHub username from the command line.
# 2. Retrieve a list of "events" associated with that user.
#        User events include things like pushing to a repository or opening up an issue on a repository.
# 3. Print out the time stamp associated with the first event in that list.

import sys
import json

import requests

if __name__ == "__main__":
    try:
        username = sys.argv[1]
    except IndexError:
        print('Usage:\npython github_latest.py <github-username>')
        sys.exit(1)

    # 1. Retrieve a list of "events" associated with the given user name
    print('Requesting data...')
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    print('Parsing data...')
    events = json.loads(response.content)

    # 2. Print out the time stamp associated with the first event in that list.
    print(f'Time stamp associated with the first event for user {username}:' )
    print(events[0]['created_at'])





