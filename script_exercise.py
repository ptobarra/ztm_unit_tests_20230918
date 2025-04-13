import random

def run_guess(guess, answer):
    # check if guess is a number int or float
    if not isinstance(guess, (int, float)):
        print('hey bozo, I said a number')
        return False
    
    # check if guess is between 1 and 10       
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
        else:
            print('wrong guess, try again')
            return False
    else:
        print('hey bozo, I said between 1 and 10')
        return False

if __name__ == '__main__':
    answer = random.randint(1, 10)
    print("answer :", answer)  # For testing purposes, you can see the answer
    while True:
        try:
            guess = int(input('Guess a number between 1 and 10: '))
            if (run_guess(guess, answer)):
                break
            # if 0 < guess < 11:
            #     if guess == answer:
            #         print('you are a genius!')
            #         break
            # else:
            #     print('hey bozo, I said between 1 and 10')
        except ValueError:
            print('Please enter a number.')
            continue

# For testing purposes, we'll move the code inside the try block into a function. And write the tests for it.