from new_random import *
from io import StringIO


game = GuessGame(0, 10)
def test_MakeGuess():
    game.actual_number = 5
    assert game.MakeGuess(5) == True

def test_makeGuess_2():
    assert game.MakeGuess(4) == False

# Two different ways of testing with input call

def test_get_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "akhil")
    i = input("What is your name? ")
    assert i == "akhil"

num_inputs = StringIO('1\n10\n')

def test_setupGame(monkeypatch):
    monkeypatch.setattr('sys.stdin', num_inputs)
    gme = setupGame()
    props = [gme.lower, gme.upper]
    assert props == [1, 10]