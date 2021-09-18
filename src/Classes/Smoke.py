import discord
import os

class Smoke:

    def __init__(self, requestedmap, requestedsmoke):
        self.requestedmap = requestedmap
        self.requestedsmoke = requestedsmoke
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        self.filelocation = os.path.join(fileDir, '../resources/Smokes')

    def getSmoke(self):
        files = [discord.File(self.filelocation + '/' + self.requestedmap.lower() + '/' + self.requestedsmoke.lower() + '.png'), discord.File(self.filelocation + '/' + self.requestedmap.lower() + '/' + self.requestedsmoke.lower() + '2.png')]
        return files