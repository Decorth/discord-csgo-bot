import json
import os
from Classes import lcs

# input validation will check with list of requests
# will string match the user message with lists of requests
# if there is one string out of list of requests that fits the request the best return valid = true and update self.usermessage to that best fit


class RequestHandler:

    def __init__(self, usermessage):
        self.usermessage = usermessage
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        self.directorysmokes = fileDir + '/../resources/lists/smokes.json'
        self.directorycases = fileDir + '/../resources/lists/cases.json'
        self.directorycommands = fileDir + '/../resources/lists/commands.json'

    def getUserCommand(self):
        return self.usermessage.split()[0]

    def inputValidation(self):
        requests = self.listRequests()
        self.findMostSimilar(requests)
        if self.usermessage == 'none':
            return False
        else:
            return True

    # This looks through the possible requests, finds command with the highest longest common sequence and replaces the usermessage with this command
    # If there is no ONE highest longest common sequence then it replaces the usermessage with 'none'
    # THIS FUNCTION NEEDS LOOKING AT BADLY
    def findMostSimilar(self, requests):
        most = 'none'
        maximum = 0
        for i in range(0, len(requests)):
            comparator = lcs.lcs(requests[str(i)], self.usermessage)
            if comparator.getAnswer() > maximum:
                most = requests[str(i)]
                maximum = comparator.getAnswer()
            elif comparator.getAnswer() == maximum:
                most = 'none'
        self.usermessage = most
        return

    def buildRequest(self, index):
        request = ''
        for i in range(index, len(self.usermessage.split())):
            request += self.usermessage.split()[i]
        return request

    def buildRequestWithEnd(self, index, endIndex):
        request = ''
        for i in range(index, endIndex):
            request += self.usermessage.split()[i]
        return request

    def listRequests(self):
        if self.buildRequest(0) == '$smoke':
            file = open(self.directorysmokes, 'r')
        elif self.buildRequest(0) == '$case':
            file = open(self.directorycases, 'r')
        else:
            file = open(self.directorycommands, 'r')
        requests = json.loads(file.read())
        return requests