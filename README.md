# Game-of-Real-Estate 
(A Westeros inspired Monopoly Game)

The class RealEstateGame is a multi-player simplified version of the game Monopoly.

Players start at the "GO" space, take turns rolling a single die (number generated randomly), and move around the circular board spaces.  Players recieve an initial sum of money and a bonus amount for passing the GO space. With the exception of the GO space, each space on the board is available for purchase. Once purchased, non-owner players who land on the space must pay rent.  When a player runs out of money, that player becomes inactive and forfeits all properties. The game continues until only one player with money remains. 
## Driver Code
An example of how the RealEstateGame class methods are called to create a game is provided at the end of the RealEstateGame.py file.  The user specifies the number of players (1-10) and provides unique player names.  The user also has the option to add the computer as an opponent. 

![image](https://github.com/boothcat/Real-Estate-Game/assets/97126252/1b8b727c-5b8c-4d16-9c01-b8072fbfcd17)





## RealEstateGame class methods 
* create_spaces - takes two optional parameters: the amount of money given to players when they land on or pass the "GO" space, and an array of 24 integers (rent amounts). Default values for the parameters are provided. 
  * Creates a space named "GO". This space cannot be purchased.
  * Creates exactly 24 more game spaces (for a total of 25):
    * Does not allow duplicate game space names
    * Purchase price is equal to 5 times the rent amount
* create_player - takes two parameters: a unique name and an optional initial account balance
  * Default initial account balance is provided
  * Players always start at the "GO" Space
* get_player_account_balance - takes as a parameter the name of the player and returns the player's account balance
* get_players - returns the dictionary of player info.  Keyword player name.
* get_spaces - returns the dictionary of all space info. Keyword space number (0-24).
* get_spaces_name - takes the space number as a parameter and returns the property name.
* get_properties - takes the player name as a parameter and returns a list of that player's properties.
* get_player_current_position - takes as a parameter the name of the player and returns the player's current position on the board as an integer (where the "GO" space is position zero)
* get_rent - takes the space number as a parameter and returns the rent of the space.
* get_purchase_price - take the space number as a parameter and returns the purchase price of the space.
* get_owner - takes the space number as a parameter and returns the current owner, None is no owner and False if GO space.
* set_position - takes the player's name and the space to move that player as parameters. Moves the player to that space.
* set_balance - takes the player's name and balance as parameters and overwrite's the player's balance to the provided amount.
* 
* buy_space - takes as parameters the name of the player
  * The player can buy a space if their balance is greater than the purchase price and the space has no owner.
    * The purchase price of the space is deducted from the player's account
    * The player is set as the owner of the current space
    * The method returns True
  * Otherwise, the method returns False
* move_player - takes as parameters the name of the player, and the number of spaces to move (1-6)
  * If the player's account balance is 0, the method returns
  * The method moves the player around the circular board by the number of spaces
  * If the player lands on or passes "GO" while being moved, the player receives the "GO" amount of money
  * After the move is complete the player pays rent if necessary.
    * No rent is paid if the player is occupying the "GO" space, or if the space has no owner, or if the owner is the player
    * Otherwise:
      * The player must pay the rent for the space currently occupied
      * The player cannot pay more than the amount in player's account balance
      * The amount paid is deducted from the players account and deposited into the game space owner's account
      * If the player's new account balance is 0, the player has lost the game, and forfeits their properties.  Their properties are now available for purchase.
* check_game_over
  * The game is over if all players but one have an account balance of 0
  * If the game is over, the method returns the winning player's name
  * Otherwise, the method returns False
