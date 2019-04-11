import csv
import pandas as pd

class githubAdd:

    def __init__(self):
        self.readGithubUsersCSV('githubUserList.csv');

    def readGithubUsersCSV(self, inputFile):
        csvFile = pd.read_csv(inputFile)
        users = csvFile['User']
        teams = csvFile['Team']
        for u in range(len(users)):
            print('User:', users[u], ' -----------  Team: ', teams[u])
        
if __name__ == "__main__":
    githubAdd()



