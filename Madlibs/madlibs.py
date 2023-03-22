from madlibsTemplates import madlib_selector
import random

if __name__ == '__main__':
    choice = random.choices([1, 2, 3, 4])
    madlib_selector(choice)
