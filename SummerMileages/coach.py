import captain

class Coach:
    
    captains = []

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def addCaptain(self, captain):
        self.captains.append(captain)

    def rankWinner(self):
        highestPoints = 0
        for captain in self.captains:
            if captain.getMileAndPicturePoints() > highestPoints:
                highestPoints = captain.getMileAndPicturePoints()
                winner = captain
        return winner        