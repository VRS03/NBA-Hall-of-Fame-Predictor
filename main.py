# NBA Hall of Fame Predictor

from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd


def get_hall_of_fame_players():
    allPlayers = players.get_players()
    hallOfFamePlayers = []

    for player in allPlayers:
        if player['is_hall_of_famer']:
            hallOfFamePlayers.append(player)

    return hallOfFamePlayers


# Main
print("Test")
hallOfFamePlayers = get_hall_of_fame_players()
print(hallOfFamePlayers)
