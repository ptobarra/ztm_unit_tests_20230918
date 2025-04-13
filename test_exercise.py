import unittest
import script_exercise  # Assuming the game logic is in a file named script_exerise.py

class TestGame(unittest.TestCase):
    def test_input(self):
        # Test the game logic here        
        result = script_exercise.run_guess(guess=5, answer=5)
        self.assertTrue(result, "guess == answer")
        # pass

    def test_input_wrong_guess(self):
        # Test the game logic here        
        result = script_exercise.run_guess(guess=5, answer=3)
        self.assertFalse(result, "guess != answer")
    
    def test_input_wrong_number(self):
        # Test the game logic here        
        result = script_exercise.run_guess(guess=11, answer=5)
        self.assertFalse(result, "guess not between 1 and 10")
    
    def test_input_wrong_type(self):
        # Test the game logic here        
        result = script_exercise.run_guess(guess='dfdfs', answer=5)
        self.assertFalse(result, "guess is not a number")

    # Add more test cases as needed        
        

if __name__ == '__main__':
    unittest.main()
# The above code is a placeholder for the test case. You can implement your own test logic inside the test_input method.