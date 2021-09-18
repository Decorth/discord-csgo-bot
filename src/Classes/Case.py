import random
import json

class Case:

    def __init__(self):
        self.MIN_ROLL = 1
        self.MAX_ROLL = 10000
        # NOTE: these are cumulative probabilities
        self.SPECIAL_PROBABILITY = 26
        self.RED_PROBABILITY = 90
        self.PINK_PROBABILITY = 410
        self.PURPLE_PROBABILITY = 2008

    def openCase(self, case):
        collection = json.loads(self.getCaseCollection(case))
        rarity = self.getRarity()
        maxitems = len(collection[rarity])
        index = random.randint(0, maxitems)
        word = "Opened " + case + " case for: " + collection[rarity][index]["Gun"] + " | " + collection[rarity][index]["Pattern"] + " (" + rarity + " rarity" + ")"
        return word

    def getCaseCollection(self, case):
        file = open("./resources/Cases/" + case + ".JSON", "r")
        return file.read()

    def getRarity(self):
        roll = random.randint(self.MIN_ROLL, self.MAX_ROLL)
        if(roll <= self.SPECIAL_PROBABILITY):
            return 'Special'
        elif(roll <= self.RED_PROBABILITY):
            return 'Red'
        elif(roll <= self.PINK_PROBABILITY):
            return 'Pink'
        elif(roll <= self.PURPLE_PROBABILITY):
            return 'Purple'
        else:
            return 'Blue'
