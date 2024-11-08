import requests
from player import Player
from playerreader import PlayerReader
from stats import PlayerStats
from rich import print
from rich.console import Console
from rich.table import Table



def main():
    table = Table(title="NHL players")
    table.add_column("Name", style="bright_magenta", no_wrap=True)
    table.add_column("Team", style="blue")
    table.add_column("points", style="red")
    seasons = input(f"Select a season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25]: ")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{seasons}/players"
    reader = PlayerReader(url).get_players()
    stats = PlayerStats(reader)
    nationality = input(f"Select a nationality [{stats.get_nationalities()}]: ")
    players = stats.top_scorers_by_nationality(nationality)

    for player in players:
        table.add_row(player.name, player.team, f"{player.goals} + {player.assists} = {player.points}")

    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
