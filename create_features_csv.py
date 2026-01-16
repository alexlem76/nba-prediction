import pandas as pd

features_general = ['match_id', 'team', 'opp'] 
features_off = ['pts', 'fg_pct', 'fg3_pct', 'ft_pct', 'off_rating']
features_def = ['opp_pts', 'opp_fg_pct', 'def_rating']
features_context = ['home_away', 'win_streak', 'b2b', 'rest_days']
label = ['team_won']

# Step 2 Prepare your data
columns = features_general + features_off + features_def + features_context + label

# Step 3 Create a DataFrame using DataFrame function
df = pd.DataFrame(columns=columns)

# Step 4 Specify the file path to save data
csv_file_path = './ml-nba/csv/nba_features.csv'

# Step 5 Write the DataFrame to a CSV file using to_csv() function where file path is passed
df.to_csv(csv_file_path, index=False)

print(f'CSV file {csv_file_path} has been created successfully.')