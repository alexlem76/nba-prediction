# Features Essentielles
# Stats Offensives

# pts_per_game : Points marqués par match (moyenne des derniers N matchs)
# fg_pct : Pourcentage de tirs réussis (Field Goal %)
# fg3_pct : Pourcentage de tirs à 3 points
# ft_pct : Pourcentage de lancers francs
# off_rating : Rating offensif (points pour 100 possessions)

# Stats Défensives

# opp_pts_per_game : Points encaissés par match
# def_rating : Rating défensif (points concédés pour 100 possessions)
# opp_fg_pct : Pourcentage de tirs adverses réussis

import pandas as pd
from bs4 import BeautifulSoup
from list_filenames import list_filenames   

df = pd.read_csv('./ml-nba/csv/nba_features.csv')
dossier = './ml-nba/html/games/'
filename_list = list_filenames(dossier)

row = 0

# prendre le nom du fichier le mettre dans la colonne match_id
for file in filename_list:
    df.loc[row, 'match_id'] = file
    df.loc[row, 'team'] = 'DAL'
    row += 1

df.to_csv('./ml-nba/csv/nba_features.csv', index=False)