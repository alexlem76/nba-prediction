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
from list_filenames import list_filenames
from bs4 import BeautifulSoup

df = pd.read_csv('./csv/nba_features.csv')
dossier = './html/games/'
filename_list = list_filenames(dossier)

# prendre le nom du fichier le mettre dans la colonne match_id
for file, row in zip(filename_list, range(len(df))):
    df.loc[row, 'match_id'] = file
    df.loc[row, 'team'] = 'DAL'
    df.loc[row, 'opp'] = None # ALLER CHERCHER DANS LES HTML

df.to_csv('./csv/nba_features.csv', index=False)