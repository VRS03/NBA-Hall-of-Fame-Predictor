# NBA Hall of Fame Predictor

from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

hall_of_fame_names = [
    "John Schommer",
    "George Mikan",
    "Hank Luisetii",
    "Charles Hyatt",
    "John Wooden",
    "Charles Murphy",
    "Branch McCracken",
    "Ed Macauley",
    "Victor Hanson",
    "Edward Wachter",
    "Christian Steinmetz",
    "John Roosma",
    "Andy Phillip",
    "Bob Kurland",
    "Forrest DeBernardi",
    "Bergnard Borgmann",
    "John Thompson",
    "Barney Sedran",
    "Harlan Page",
    "Jack McCracken",
    "Robert Gruenig",
    "John Russel",
    "Nat Holman",
    "Harold Foster",
    "Joe Lapchick",
    "Dutch Dehnert",
    "Bob Davies",
    "Bob Pettit",
    "Bob Cousy",
    "Max Friedman",
    "Paul Endacott",
    "Dolph Schayes",
    "John Beckman",
    "Ernest Schmidt",
    "Robert Vandivier",
    "Joseph Brennan",
    "Bill Russell",
    "Bill Sharman",
    "Ed Krause",
    "Tom Gola",
    "William Johnson",
    "Lauren Gale",
    "Charles Cooper",
    "Elgin Baylor",
    "Jim Pollard",
    "Cliff Hagan",
    "Joe Fulks",
    "Paul Arizin",
    "Wilt Chamberlain",
    "Jerry West",
    "Jerry Lucas",
    "Oscar Robertson",
    "Thomas Barlow",
    "Hal Greer",
    "Slater Martin",
    "Frank Ramsey",
    "Willis Reed",
    "Jack Twyman",
    "Dave DeBusschere",
    "Bill Bradley",
    "Sam Jones",
    "John Havlicek",
    "Al Cervi",
    "Nate Thurmond",
    "Billy Cunningham",
    "Tom Heinsohn",
    "Bob Houbregs",
    "Bobby Wanzer",
    "Pete Maravich",
    "Walt Frazier",
    "Rick Barry",
    "Clyde Lovellette",
    "Bob McDermott",
    "Wes Unseld",
    "K.C. Jones",
    "Pop Gates",
    "Lenny Wilkens",
    "Neil Johnston",
    "Elvin Hayes",
    "Dave Bing",
    "Earl Monroe",
    "Harry Gallatin",
    "Dave Cowens",
    "Tiny Archibald"

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