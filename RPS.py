"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.next_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        chosen_move = input("Choose between " + str(moves))
        if chosen_move in moves:
            return chosen_move
        else:
            print_pause("I'm sorry, I didn't understand.")
            return self.move()


class ReflectPlayer(Player):
    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move


class CyclePlayer(Player):
    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        if my_move == moves[0]:
            self.next_move = moves[1]
        elif my_move == moves[1]:
            self.next_move = moves[2]
        else:
            self.next_move = moves[0]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.rounds = 0

    def intro(self):
        print_pause("Welcome to Rock, Paper, Scissors the Simulator!")
        while True:
            try:
                self.rounds = input("How many rounds would you like to play!?")
                val = int(self.rounds)
                break
            except ValueError:
                print_pause("I'm sorry, thats not a valid number."
                            " Please try again")
        print_pause("Are you ready?")
        print_pause("Game Start!")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player One: {move1}  Player Two: {move2}")

        if beats(move1, move2):
            print_pause("Player One Scores!")
            self.p1.score += 1
        elif beats(move2, move1):
            print_pause("Player Two Scores!")
            self.p2.score += 1
        else:
            print_pause("It's a Draw!! No Score!")

        print_pause(f"The score is now Player One: {self.p1.score}, "
                    f"Player Two: {self.p2.score}.")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        self.intro()
        for round in range(1, int(self.rounds) + 1):
            print_pause(f"Round {round}:")
            self.play_round()
        print_pause("Game over!")

        if self.p1.score > self.p2.score:
            print_pause("Player One WINS! By a Score of "
                        f"{self.p1.score} to {self.p2.score}")
        elif self.p2.score > self.p1.score:
            print_pause("Player Two WINS! By a Score of "
                        f"{self.p2.score} to {self.p1.score}")
        else:
            print_pause(f"It's a Draw! No Winner Decided!")

        self.new_game()

    def new_game(self):
        self.play_again = input("Would you like to play again? "
                                "Please say 'yes' or 'no'")
        if self.play_again == "yes":
            self.p1.score = 0
            self.p2.score = 0
            game.play_game()


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
