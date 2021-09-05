import unittest
import captain
import runner

class RunnerTest(unittest.TestCase):
    def testAddMiles(self):
        jCaptain = captain.Captain("J", "Runner")
        jCaptain.addMiles(12)
        jCaptain.addMiles(10)
        self.assertEqual(22, jCaptain.getMileages())

    def testGetTeamMileages(self): 
        jRunner = runner.Runner("J", "Runner")
        jRunner.addMiles(100)

        jCaptain = captain.Captain("j", "Captain")
        jCaptain.addMiles(200)
        jCaptain.addRunner(jRunner)

        self.assertEqual(300, jCaptain.getTeamMileages())

    def testGetPicturePoints(self):    
        jCaptain = captain.Captain("j", "Captain")
        jCaptain.addPicturePoints(2)
        self.assertEqual(0, jCaptain.getPicturePoints()) 

        jCaptain = captain.Captain("j", "Captain")
        jCaptain.addPicturePoints(3)
        self.assertEqual(5, jCaptain.getPicturePoints()) 

        jCaptain = captain.Captain("j", "Captain")
        jCaptain.addPicturePoints(5)
        self.assertEqual(9, jCaptain.getPicturePoints()) 

    def testGetMileAndPicturePoint(self):    
        jCaptain = captain.Captain("j", "Captain")
        jCaptain.addPicturePoints(5)
        jCaptain.addMiles(20)
        self.assertEqual(29, jCaptain.getMileAndPicturePoints()) 

if __name__ == '__main__':
    unittest.main()        