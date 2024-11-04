import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_does_player_exist_no(self):
        self.assertAlmostEqual(self.stats.search("Teppo"), None)

    def test_does_player_exist_yes(self):
        self.assertAlmostEqual(self.stats.search("Semenko").name, "Semenko")

    def test_does_teamname_exist_no(self):
        self.assertAlmostEqual(self.stats.team("SMTH"), [])

    def test_does_sort_by_points_return_right_amount_of_players(self):
        how_many = 2
        returned = [player.name for player in self.stats.top(how_many)]
        self.assertEqual(returned, ["Gretzky", "Lemieux"][:how_many])

    def test_does_sort_by_goals_return_right_amount_of_players(self):
        how_many = 2
        returned = [player.name for player in self.stats.top(how_many, SortBy.GOALS)]
        self.assertEqual(returned, ["Lemieux", "Yzerman"][:how_many])

    def test_does_sort_by_assists_return_right_amount_of_players(self):
        how_many = 2
        returned = [player.name for player in self.stats.top(how_many, SortBy.ASSISTS)]
        self.assertEqual(returned, ["Gretzky", "Yzerman"][:how_many])


