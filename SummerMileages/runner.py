class Runner:
    miles = 0
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def addMiles(self, mile):
        self.miles = self.miles + mile

    def getMileages(self):
        return self.miles    