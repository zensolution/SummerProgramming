import unittest
import runner

class RunnerTest(unittest.TestCase):
    def testAddMiles(self):
        jRunner = runner.Runner("J", "Runner")
        jRunner.addMiles(12)
        jRunner.addMiles(10)
        self.assertEqual(22, jRunner.getMileages())

if __name__ == '__main__':
    unittest.main()        