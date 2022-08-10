import unittest
from SHA2 import SHA2

class TestSHA2(unittest.TestCase):

    def testcase1(self):
        answer1 = "81b637d8fcd2c6da6359e6963113a1170de795e4b725b84d1e0b4cfd9ec58ce9"
        t1 = SHA2("bob")
        result1 = t1.encrypt()
        self.assertEqual(result1, answer1)

    def testcase2(self):
        answer2 = "d0b0048839660b8a49324cb7c1108adaae27a4115fe4f9807963bb3b191b8d7c"
        t2 = SHA2("the dog jumped over the cat")
        result2 = t2.encrypt()
        self.assertEqual(result2, answer2)

    def testcase3(self):
        answer3 = "f08644150bf769c911357c5c5eee968cc803ed4d7fedb31f75d44d1d5f573814"
        t3 = SHA2("the dog jumped over the cat.")
        result3 = t3.encrypt()
        self.assertEqual(result3, answer3)

    def testcase4(self):
        answer4 = "96754022bc730859c1375dbb6354fde1ceb61421f5ef02ab869b87f19c512c8e"
        t4 = SHA2("the dog jumped over the moon")
        result4 = t4.encrypt()
        self.assertEqual(result4, answer4)

    def testcase5(self):
        answer5 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        t5 = SHA2("")
        result5 = t5.encrypt()
        self.assertEqual(result5, answer5)


unittest.main()
