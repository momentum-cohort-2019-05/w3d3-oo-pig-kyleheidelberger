Class:
- Player
Responsibilities:
- roll the die
Collaborators:
- Game
Subclasses:
- Human Player
- Computer Player

Class:
- Human Player
Responsibilities:
- roll die
- choose to hold or roll again
Collaborators:
- Game

Class: Computer Player
Responsibilities:
- roll die
- choose to roll again while turn score is less than 20
- choose to hold when turn score goes above 20
Collaborators:
- Game

Class: Game
Responsibilities:
- choose starting player randomly
- alternate turns for players
- keep track of current player
- keep track of both the turn scores and total score for both players
- get input from human player on whether to hold or roll
- set condition for end of game (when player reaches 100 points) and end game when that is achieved
Collaborators:
- human player
- computer player
- player