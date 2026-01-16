# 1. Prédiction de victoires NBA
# Prédire le résultat d'un match en utilisant les statistiques d'équipe 
# (points par match, pourcentage de tirs, rebonds). 
# Idéal pour apprendre la régression logistique et les arbres de décision.

import pandas as pd
from bs4 import BeautifulSoup

teams = ['Dallas Mavericks', 'San Antonio Spurs']
teams_min = ['mavs', 'spurs']
id = ['team_and_opponent', 'team_misc']

with open("./ml-nba/html/2025-26 Dallas Mavericks Roster and Stats _ Basketball-Reference.com.html", "r", encoding="utf-8") as f : 
    content = f.read()

# Parse HTML content with lxml parser (faster and more robust than default)
soup = BeautifulSoup(content, 'html.parser')

stat = soup.find('table', id='team_and_opponent')

df = pd.read_html(str(stat))[0]
print(df)

df.to_csv('ml-nba/csv/mavs/mavs_team_stats.csv')