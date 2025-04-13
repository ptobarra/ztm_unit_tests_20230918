import unittest

import script


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
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


if __name__ == '__main__':
    unittest.main()  # run all the tests in this file
