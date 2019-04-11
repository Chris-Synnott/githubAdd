import csv
from subprocess import call

class githubAdd:

    def __init__(self):
        self.readGithubUsersCSV('githubUserList.csv')

    def readGithubUsersCSV(self, inputFile):
        with open(inputFile) as csvfile:
            users = csv.reader(csvfile, delimiter=',')
            for row in users:
                print (row)
                
            call('curl -X PUT -u "username":"password" https://api.github.com/orgs/orgName/memberships/'+row[0], shell=True)

        return users
        
if __name__ == "__main__":
    githubAdd()

