import csv

class githubAdd:

    def __init__(self):
        self.readGithubUsersCSV('githubUserList.csv');

    def readGithubUsersCSV(self, inputFile):
        with open(inputFile) as csvfile:
            users = csv.reader(csvfile, delimiter=',')
            for row in users:
                breakpoint()
                print(', '.join(row))

if __name__ == "__main__":
    #breakpoint()
    githubAdd()



