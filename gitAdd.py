import csv
import pandas as pd
import os
from subprocess import call

class githubAdd:

    def __init__(self):
        # test unix system call
        call('ls', shell=True)
        # get user and team list
        self.users, self.teams = self.readGithubUsersCSV('githubUserList.csv');

    def readGithubUsersCSV(self, inputFile):
        # read in csv File
        csvFile = pd.read_csv(inputFile)
        # get users in column named 'User'
        users = csvFile['User']
        # get teams in column named 'Team'
        teams = csvFile['Team']
        # loop through rows and print user and team
        for u in range(len(users)):
            print('User:', users[u], ' -----------  Team: ', teams[u])

        return users, teams
        
if __name__ == "__main__":
    githubAdd()



