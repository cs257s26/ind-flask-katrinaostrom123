import unittest
import sys
import os

sys.path.append(os.path.abspath("../ProductionCode"))
from app import app
from game_command_line import *
from leaderboard_command_line import *

class TestFlaskLeaderboard(unittest.TestCase):

    def setUp(self):
        """Set up"""
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.client = app.test_client()

    def test_home_page(self):
        """Test that the home page loads correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)

    def test_game_page(self):
        """Test that /game loads the game."""
        response = self.client.get('/game')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Species Quiz", response.data)
        self.assertIn(b"Submit Guess", response.data)

    def test_leaderboard_page(self):
        """Test that /leaderboard/Coyote loads the correct data."""
        response = self.client.get('/leaderboard/Coyote')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Leaderboard", response.data)
        self.assertIn(b"Coyote", response.data)

if __name__ == '__main__':
    unittest.main()