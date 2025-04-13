import unittest

import script


class TestMain(unittest.TestCase):

    # setUp allows us to run a piece of code that sets up before each call of the test
    def setUp(self) -> None:
        print('\nabout to test a function')

    def test_do_stuff(self):
        """
        HIIII!!!!
        """
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)  # add assertion here

    def test_do_stuff2(self):
        test_param = 'dfsfdasfdasfds'
        result = script.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))  # add assertion here

    def test_do_stuff3(self):
        test_param = 'dfsfdasfdasfds'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)  # add assertion here

    def test_do_stuff4(self):
        test_param = None
        result = script.do_stuff(test_param)
        # self.assertIsInstance(result, ValueError)  # add assertion here
        self.assertEqual(result, 'please enter number')  # add assertion here

    def test_do_stuff5(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')  # add assertion here

    # test case added for when the input is the int 0
    def test_do_stuff6(self):
        test_param = 0
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')  # add assertion here

    # we run the following method at the end of each method that we called.
    # we use this following method to clean up or reset some variables.
    def tearDown(self) -> None:
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()  # run all the tests in this file
