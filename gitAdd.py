import csv
from subprocess import call

class githubAdd:

    def __init__(self):
        # You can modify githubUserList.csv to any .csv file of your choice. Remember to leave the first line blank
        self.readGithubUsersCSV('githubUserList.csv')

    def readGithubUsersCSV(self, inputFile):
        with open(inputFile) as csvfile:
            users = csv.reader(csvfile, delimiter=',')
            for row in users:
                # Replace username with your username, password with your password, and YOURORGNAMEHERE with your
                # organisation name
                call('curl -X PUT -u "username":"password" https://api.github.com/orgs/YOURORGNAMEHERE/memberships/' + row[0], shell=True)

        return users
        
if __name__ == "__main__":
    githubAdd()

