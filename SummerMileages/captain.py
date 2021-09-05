import runner

class Captain(runner.Runner):
    
    runners = []
    picturePoints = 0

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def addRunner(self, runner):
        self.runners.append(runner)

    def getTeamMileages(self):
        totalMiles = 0 
        for runner in self.runners:
            totalMiles = totalMiles + runner.getMileages()   
        return totalMiles + self.getMileages()

    def addPicturePoints(self, peoples):
        if peoples == 3:
            self.picturePoints += 5
        elif peoples > 3:
            points = 5 + (peoples-3) * 2
            self.picturePoints += points 


    def getPicturePoints(self):
        return self.picturePoints

    def getMileAndPicturePoints(self):
        return self.picturePoints + self.getMileages()