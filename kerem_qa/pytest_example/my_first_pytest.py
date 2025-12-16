import unittest


class myfirstpytest(unittest.TestCase):

    def setUp(self):
        print("into setup")
        self.num1 = 2
        self.num2 = 3

    def tearDown(self):
        print("into test end")

    def test_summery(self):
        summery = self.num1 + self.num2
        # if summery == 5 :
        #     print("summery is correct")
        # else :
        #     print("summery is incorrect")

        assert summery == 5 , "the summery of 3 and 4 is not 5"
        result = summery*2
        print(result)

    def test_multiple(self):
        multiple = self.num1 * self.num2
        assert multiple == 6, "our code did not suport multiple "
