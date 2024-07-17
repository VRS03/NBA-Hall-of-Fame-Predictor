# # NBA Hall of Fame Predictor
#
# from nba_api.stats.static import players
# from nba_api.stats.endpoints import playercareerstats
# import pandas as pd
#
# hall_of_fame_names = [
#     "Michael Jordan",
#     "Magic Johnson",
#     "Larry Bird",
#     "Kareem Abdul-Jabbar",
#     "Wilt Chamberlain",
#     "Stephen Curry",
# ]
#
#
# def get_player_stats(player_id):
#     career = playercareerstats.PlayerCareerStats(player_id=player_id)
#     return career.get_data_frames()[0]
#
#
# def get_player_id(name):
#     player_dict = players.find_players_by_full_name(name)
#     if player_dict:
#         return player_dict[0]['id']
#     return None
#
#
# hof_player_ids = []
# for name in hall_of_fame_names:
#     player_id = get_player_id(name)
#     if player_id:
#         hof_player_ids.append((name, player_id))
#
# hofStats = []
# for name, player_id in hof_player_ids:
#     stats = get_player_stats(player_id)
#     stats['player_name'] = name
#     hofStats.append(stats)
#
# print(hofStats)
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# List of known Hall of Fame players for training
hall_of_fame_names = [
    "Michael Jordan",
    "Magic Johnson",
    "Larry Bird",
    "Kareem Abdul-Jabbar",
    "Wilt Chamberlain",
    "Dirk Nowitzki",
]

# List of known non-Hall of Fame players for training
non_hall_of_fame_names = [
    "Shawn Bradley",
    "Manute Bol",
    "Calvin Booth",
    "Kwame Brown",
    "Greg Ostertag",
    "Adam Morrison",
]

def get_player_stats(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career.get_data_frames()[0]

def get_player_id(name):
    player_dict = players.find_players_by_full_name(name)
    if player_dict:
        return player_dict[0]['id']
    return None

def create_features(stats):
    features = {}
    features['points_per_game'] = stats['PTS'].mean()
    features['rebounds_per_game'] = stats['REB'].mean()
    features['assists_per_game'] = stats['AST'].mean()
    features['total_games'] = stats['GP'].sum()
    features['total_points'] = stats['PTS'].sum()
    features['total_rebounds'] = stats['REB'].sum()
    features['total_assists'] = stats['AST'].sum()
    features['years_played'] = len(stats)
    return features

player_data = []
for name in hall_of_fame_names + non_hall_of_fame_names:
    player_id = get_player_id(name)
    if player_id:
        stats = get_player_stats(player_id)
        features = create_features(stats)
        features['hall_of_fame'] = 1 if name in hall_of_fame_names else 0
        player_data.append(features)

df = pd.DataFrame(player_data)

# Prepare data for training
X = df.drop(columns=['hall_of_fame'])
y = df['hall_of_fame']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
# print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Function to predict Hall of Fame status for a player
def predict_hall_of_fame(player_name):
    player_id = get_player_id(player_name)
    if not player_id:
        return f"Player {player_name} not found."
    stats = get_player_stats(player_id)
    features = create_features(stats)
    features_df = pd.DataFrame([features])
    prediction = model.predict(features_df)
    return "Hall of Famer" if prediction[0] == 1 else "Not a Hall of Famer"

# Example prediction
print(predict_hall_of_fame("Dirk Nowitzki"))