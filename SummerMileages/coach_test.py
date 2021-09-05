import unittest
import runner
import captain
import coach

class RunnerTest(unittest.TestCase):
    def testRankWinner(self):
        jRunnerTeam1 = runner.Runner("J", "Runner")
        jRunnerTeam1.addMiles(12)
        jRunnerTeam1.addMiles(10)
        
        jCaptainTeam1 = captain.Captain("J", "Captain")
        jCaptainTeam1.addMiles(13)
        jCaptainTeam1.addPicturePoints(3)
        jCaptainTeam1.addRunner(jRunnerTeam1)

        jRunnerTeam2 = runner.Runner("J", "Runner")
        jRunnerTeam2.addMiles(2)
        captainTeam2 = captain.Captain("T", "Captain")
        captainTeam2.addMiles(13)
        captainTeam2.addPicturePoints(20)
        captainTeam2.addRunner(jRunnerTeam2)

        cCoach = coach.Coach("C", "Coach")
        cCoach.addCaptain(jCaptainTeam1)
        cCoach.addCaptain(captainTeam2)
        self.assertEqual(captainTeam2, cCoach.rankWinner())

if __name__ == '__main__':
    unittest.main()        