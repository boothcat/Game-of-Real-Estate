import unittest
from RealEstateGame import RealEstateGame


class TestGame(unittest.TestCase):
    """Contains units tests for RealEstateGame class methods."""

    def setUp(self):
        self.game = RealEstateGame()
        self.game.create_spaces(100)                       # Go amount default value of $100
        self.game.create_player("Player 1", 1000)          # Starting balance $1000
        self.game.create_player("Player 2", 1000)

    def test1(self):
        """Tests that create_spaces creates "GO" space and 24 more game spaces."""
        self.assertEqual(len(self.game.get_spaces()), 25)

    def test2(self):
        """Tests that go space is set up correctly"""
        self.assertEqual(self.game.get_spaces()[0]["Name"], "GO")

    def test3(self):
        """Tests that space 24 is set up correctly"""
        self.assertEqual(self.game.get_spaces()[24], {"Name": "King's Landing", "Purchase": 1750, "Rent": 350,
                                                 "Owner": None})

    def test4(self):
        """Tests that a player can be added"""
        self.assertEqual(self.game.get_players()["Player 1"], {"Position": 0, "Balance": 1000, "Properties": []})

    def test5(self):
        """Test get_player_balance for default initial balance"""
        self.assertEqual(self.game.get_player_account_balance("Player 1"), 1000)

    def test6(self):
        """Test get_player_position for initial position"""
        self.assertEqual(self.game.get_player_current_position("Player 1"), 0)

    def test7(self):
        """Player cannot buy "GO" space.  buy_space returns False"""
        self.assertEqual(self.game.buy_space("Player 1"), False)

    def test8(self):
        """Player can move forward 6 spaces """
        self.game.move_player("Player 1", 6)
        self.assertEqual(self.game.get_player_current_position("Player 1"), 6)

    def test9(self):
        """Player can move completely around the board, land on "GO" space and position is 0"""
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 1)
        self.assertEqual(self.game.get_player_current_position("Player 1"), 0)

    def test10(self):
        """Player can move completely around the board, land on "GO" space and receive GO bonus"""
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 1)
        self.assertEqual(self.game.get_player_account_balance("Player 1"), 1100)

    def test11(self):
        """Player currently at position 23, rolls a 4.  Player's position is correctly moved to 2"""
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 5)
        self.game.move_player("Player 1", 4)
        self.assertEqual(self.game.get_player_current_position("Player 1"), 2)

    def test12(self):
        """Player currently at position 23, rolls a 4.  Player's receive "GO" bonus"""
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 5)
        self.game.move_player("Player 1", 4)
        self.assertEqual(self.game.get_player_account_balance("Player 1"), 1100)

    def test13(self):
        """Player currently at position 22, rolls a 4.  Player's position is correctly moved to 1"""
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 6)
        self.game.move_player("Player 1", 4)
        self.game.move_player("Player 1", 4)
        self.assertEqual(self.game.get_player_current_position("Player 1"), 1)

    def test14(self):
        """Player buys a space.  Buy space returns true."""
        self.game.move_player("Player 1", 3)
        self.assertEqual(self.game.buy_space("Player 1"), True)

    def test15(self):
        """Player buys a space.  Purchase price is deducted from player's account balance."""
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.assertEqual(self.game.get_player_account_balance("Player 1"), 625)

    def test16(self):
        """Player buys a space.  Space's owner is updated to player's name."""
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.assertEqual(self.game.get_owner(6), "Player 1")

    def test17(self):
        """Player buys a space.  Property is added to player's list of properties."""
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.assertEqual(self.game.get_properties("Player 1"), [6])

    def test18(self):
        """Player buys space 6, moves three more spaces, and buys space 9.  Properties are added to player's list of
        properties."""
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 1", 3)
        self.game.buy_space("Player 1")
        self.assertEqual(self.game.get_properties("Player 1"), [6, 9])

    def test19(self):
        """Player cannot buy a property owned by another player.  buy_space returns false"""
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 6)
        self.assertEqual(self.game.buy_space("Player 2"), False)

    def test20(self):
        """Player cannot buy a property if their balance is equal to the purchase price. Buy_space returns false."""
        self.game.set_balance("Player 1", 100)
        self.game.move_player("Player 1", 6)
        self.assertEqual(self.game.buy_space("Player 1"), False)

    def test21(self):
        """Player cannot buy a property if their balance is less than the purchase price. Buy_space returns false."""
        self.game.set_balance("Player 1", 50)
        self.game.move_player("Player 1", 6)
        self.assertEqual(self.game.buy_space("Player 1"), False)

    def test22(self):
        """Player cannot buy a property they already own.  buy_space returns false"""
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.assertEqual(self.game.buy_space("Player 1"), False)

    def test23(self):
        """Player moves to a space owned by another player.  Player pays rent."""
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 6)
        self.assertEqual(self.game.get_player_account_balance("Player 2"), 925)

    def test24(self):
        """Player moves to a space owned by another player.  Owner receives rent."""
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 6)
        self.assertEqual(self.game.get_player_account_balance("Player 1"), 700)

    def test25(self):
        """Player moves to a space they already own.  Player does not pay rent."""
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 1", 6)
        self.assertEqual(self.game.get_player_account_balance("Player 1"), 625)

    def test26(self):
        """Player has exactly the amount of rent.  Player has zero balance."""
        self.game.set_balance("Player 2", 75)
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 6)
        self.assertEqual(self.game.get_player_account_balance("Player 2"), 0)

    def test27(self):
        """Player has exactly the amount of rent.  Owner gets player's remaining balance."""
        self.game.set_balance("Player 2", 75)
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 6)
        self.assertEqual(self.game.get_player_account_balance("Player 1"), 700)

    def test28(self):
        """Player has does not have the rent money.  Owner gets player's remaining balance."""
        self.game.set_balance("Player 2", 70)
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 6)
        self.assertEqual(self.game.get_player_account_balance("Player 1"), 695)

    def test29(self):
        """Player cannot pay rent - properties are removed."""
        self.game.set_balance("Player 2", 300)
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 3)
        self.game.buy_space("Player 2")
        self.game.move_player("Player 2", 3)
        self.assertEqual(self.game.get_properties("Player 2"), [])

    def test30(self):
        """Player 2 goes around the board buys property 3 and property 1."""
        self.game.move_player("Player 2", 3)
        self.game.buy_space("Player 2")
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 5)
        self.game.buy_space("Player 2")
        self.assertEqual(self.game.get_properties("Player 2"), [3, 1])

    def test31(self):
        """Player's Balance is 0.  They will not be able to move position."""
        self.game.set_balance("Player 2", 0)
        self.game.set_position("Player 2", 10)
        self.game.move_player("Player 2", 3)
        self.assertEqual(self.game.get_player_current_position("Player 2"), 10)

    def test32(self):
        """Player 3 goes around the board buys property 3 and property 1 and then loses the game with zero balance."""
        self.game.set_balance("Player 2", 475)
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 3)
        self.game.buy_space("Player 2")
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 5)
        self.game.buy_space("Player 2")
        self.game.move_player("Player 2", 5)
        self.assertEqual(self.game.get_player_account_balance("Player 2"), 0)

    def test33(self):
        """Player 2 goes around the board buys property 3 and 1, loses, and properties are removed."""
        self.game.set_balance("Player 2", 475)
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 3)
        self.game.buy_space("Player 2")
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 5)
        self.game.buy_space("Player 2")
        self.game.move_player("Player 2", 5)
        self.assertEqual(self.game.get_properties("Player 2"), [])

    def test34(self):
        """Player 2 goes around the board buys property 3 and  1, loses, Owner of Property 3 is returned to None."""
        self.game.set_balance("Player 2", 475)
        self.game.move_player("Player 1", 6)
        self.game.buy_space("Player 1")
        self.game.move_player("Player 2", 3)
        self.game.buy_space("Player 2")
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 6)
        self.game.move_player("Player 2", 5)
        self.game.buy_space("Player 2")
        self.game.move_player("Player 2", 5)
        self.assertEqual(self.game.get_owner(3), None)

    def test35(self):
        """check_game_over returns winner's name."""
        self.game.set_balance("Player 2", 0)
        self.assertEqual(self.game.check_game_over(), "Player 1")

    def test36(self):
        """check_game_over returns False if more than one player has nonzero balance."""
        self.assertEqual(self.game.check_game_over(), False)

if __name__ == '__main__':
  unittest.main(verbosity=2)