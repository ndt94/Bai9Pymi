import json
import sys
import requests

def getrepos():
    next_page = True
    username = sys.argv[1]
    api = 'https://api.github.com/users/{}/repos?per_page=100'.format(username)
    results = []
    while next_page:  # the list of repos is paginated
        r = requests.get(api)
        json_format= json.loads(r.text)
        for repo in json_format:
            results.append(repo['html_url'])
        head_request = requests.head(url=r.url)
        if 'next' in head_request.links:  # check if there is another page of repos
            api = head_request.links['next']['url']
        else:
            next_page = False
    return results

def main():
    for repo in getrepos():
        print(repo)
    print(len(getrepos()))

if __name__ == "__main__":
    main()