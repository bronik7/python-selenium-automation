from pythonds.basic import Deque


def palindrome_checker(text):
    reversed_text = Deque()

    for char in text:
        reversed_text.addRear(char)
