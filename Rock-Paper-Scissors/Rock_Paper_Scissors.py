"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random


moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.their_move = None
        self.my_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def beats(self, one, two):
        if one == two:
            return "** TIE **"
        elif one == 'rock' and two == 'scissors' or one == 'scissors' and \
                two == 'paper' or one == 'paper' and two == 'rock':
            self.human_score += 1
            return "** PLAYER 1 WON **"
        else:
            self.computer_score += 1
            return "** PLAYER 2 WON **"


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move = input("Rock, paper, scissors? > ").lower()
        while move != 'rock' and move != 'paper' and move != 'scissors':
            move = input("Rock, paper, scissors? > ")
        return move


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self, my_move):
        if self.my_move is None:
            return random.choice(moves)
        self.index = moves.index(self.my_move)
        self.index = (self.index + 1) % len(moves)
        return moves[self.index]

    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.human_score = 0
        self.computer_score = 0

    def play_game(self):
        print("Game start!\n")
        self.rounds = 3
        for round in range(self.rounds):
            print(f"Round {round+1}:")
            self.play_round()
        self.winner(self.human_score, self.computer_score)
        print("\nGame over!")

    def play_round(self):
        move1 = self.p1.move()
        if isinstance(self.p2, CyclePlayer):
            move2 = self.p2.move(move1)
        else:
            move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(self.beats(move1, move2))
        print("Score:")
        print(f"Player One {self.human_score}")
        print(f"Player Two {self.computer_score}\n")

    def beats(self, one, two):
        if one == two:
            return "** TIE **"
        elif one == 'rock' and two == 'scissors' or one == 'scissors' and \
                two == 'paper' or one == 'paper' and two == 'rock':
            self.human_score += 1
            return "** PLAYER 1 WON **"
        else:
            self.computer_score += 1
            return "** PLAYER 2 WON **"

    def winner(self, human_score, computer_score):
        if self.human_score > self.computer_score:
            print(f"Player 1 won the game with a score of {human_score}")
            print(f"While Player 2 score is {computer_score}!")
        elif self.human_score < self.computer_score:
            print(f"Player 2 won the game with a score of {computer_score}")
            print(f"While Player 1 score is {human_score}!")
        elif self.human_score == self.computer_score:
            print(f"The game ends in a tie with a score of {human_score}!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), Player())
    game.play_game()
