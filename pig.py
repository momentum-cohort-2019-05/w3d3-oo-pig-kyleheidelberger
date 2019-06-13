import random

def roll_die():
    """
    Rolls a six-sided die and returns an integer.
    """
    return random.randint(1,6)

class Player:
    """
    The class of all players in Pig.
    Parent class of both HumanPlayer and ComputerPlayer
    """

    def __init__(self, name):
        """
        Creates an object with the class Player and give it the attributes name and score.
        """
        self.name = name
        self.round_score = 0

    # def __str__(self):
    #     """
    #     Gives the class Player a string method to return its name.
    #     """
    #     return self.name

    def start_round(self):
        """
        Sets the Player's score at the start of each round to 0.
        """
        self.round_score = 0

    def roll(self, number):
        """
        Takes the argument number (the number rolled by the die) and adds it to the players score to get the new round score.
        """
        # number = roll_die()
        self.round_score += number


class ComputerPlayer(Player):
    """
    The computer player for Pig. A subclass of Player, inheriting all its methods.
    """
    def roll_again(self):
        return self.round_score < 20
        # number = roll_die()
        # if self.round_score < 20:
        #     self.round_score += number
        # else:
        #     return self.round_score

class HumanPlayer(Player):
    """
    The user / human player. A subclass of Player, inheriting all its methods.
    """

    def roll_again(self):
        make_choice = input("Do you want to (h)old or (r)oll? ").lower()
        return make_choice[0] == "r"


class Game:
    """
    The game of Pig. Includes methods for taking turns, keeping score.
    """

    def __init__(self, die, p1, p2):
        self.die = die
        self.players = [p1, p2]
        self.current_player = None
        self.reset_scores()

    def reset_scores(self):
        self.scores = [0, 0]
        self.round_score = 0

    def starting_player(self):
        self.current_player = random.randint(0, 1)
        if self.current_player == 0:
            print(f"Player {self.current_player + 1} (User) goes first!")
            return self.current_player
        else:
            print(f"Player {self.current_player + 1} (Computer) goes first!")
            return self.current_player

    def get_current_player(self):
        return self.players[self.current_player]

    def take_turns(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0
        print(f"It is Player {self.current_player + 1}'s turn.")

    def end_game(self):
        return self.scores[0] >= 100 or self.scores[1] >= 100

    def start_game(self):
        self.reset_scores()
        self.starting_player()

        while not self.end_game():
            self.play_round()
            if not self.end_game():
                self.take_turns()

        print(f"Player {self.current_player + 1} wins!") 
   
    def play_round(self):
        turn_score = 0
        player = self.get_current_player()
        player.start_round()

        roll = self.die()
        player.roll(roll)
        print(f"Roll: {roll}")

        while roll != 1:
            turn_score += roll
            if not player.roll_again():
                break
            roll = self.die()
            player.roll(roll)
            print(f"Roll: {roll}")

        if roll == 1:
            turn_score = 0

        print(f"Turn Score: {turn_score}")

        self.scores[self.current_player] += turn_score
        print(f"Current score for Player {self.current_player + 1}: {self.scores[self.current_player]}")


if __name__ == "__main__":
    game = Game(roll_die, HumanPlayer("User"), ComputerPlayer("Computer"))
    game.start_game()