import csv
import requests

class githubAdd:

    def __init__(self):
        self.readGithubUsersCSV('githubUserList.csv')

    def readGithubUsersCSV(self, inputFile):
        with open(inputFile) as csvfile:
            users = csv.reader(csvfile, delimiter=',')
            for row in users:
                #breakpoint()
                URL = "https://api.github.com/orgs/YOURORGNAMEHERE/memberships/" + row[0]
                r = requests.put(url=URL)
                print (r.json())

if __name__ == "__main__":
    #breakpoint()
    githubAdd()



