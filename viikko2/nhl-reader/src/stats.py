import requests
from player import Player
from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
            self.reader = reader

    def get_nationalities(self):
        nats = set()

        for player in self.reader:
            nats.add(player.nationality)

        sorted_nats = sorted(nats)
        as_str = "/".join(sorted_nats)

        return as_str

    def top_scorers_by_nationality(self, nationality):
        sorted_players = filter(self.reader.sort(key=lambda x: x.points, reverse=True), self.reader)

        ret = []

        for player in sorted_players:
             if player.nationality == nationality:
                  ret.append(player)

        return ret