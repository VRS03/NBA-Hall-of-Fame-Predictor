# NBA Hall of Fame Predictor

from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

hall_of_fame_names = [
    "Michael Jordan",
    "Magic Johnson",
    "Larry Bird",
    "Kareem Abdul-Jabbar",
    "Wilt Chamberlain",
]


def get_player_stats(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career.get_data_frames()[0]


def get_player_id(name):
    player_dict = players.find_players_by_full_name(name)
    if player_dict:
        return player_dict[0]['id']
    return None


hof_player_ids = []
for name in hall_of_fame_names:
    player_id = get_player_id(name)
    if player_id:
        hof_player_ids.append((name, player_id))

hofStats = []
for name, player_id in hof_player_ids:
    stats = get_player_stats(player_id)
    stats['player_name'] = name
    hofStats.append(stats)

print(hofStats)