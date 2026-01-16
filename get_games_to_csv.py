import os
import pandas as pd
from bs4 import BeautifulSoup
from list_filenames import list_filenames
import time

start = time.time()

dossier = './ml-nba/html/games/'
filename_list = list_filenames(dossier)

for file in filename_list:
    ancien_chemin = os.path.join(dossier, file)
    with open(ancien_chemin, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse HTML content with lxml parser (faster and more robust than default)
    soup = BeautifulSoup(content, 'html.parser')

    teams = []
    line_score = soup.find('table', id='line_score') # prendre les deux noms d'équipes

    # On parcourt les lignes du tbody
    for row in line_score.tbody.find_all("tr"):
        team_cell = row.find("th", {"data-stat": "team"})
        if team_cell:
            a = team_cell.find("a")
            if a:
                teams.append(a.text.strip())

    print(teams[0] + ' at ' + teams[1])
    
    for team in teams:
        # faire un csv pour chaque équipe "{match_id sans 0DAL, que la date}_{TEAM}_stats"
        basic_stat = soup.find('table', id=f'box-{team}-game-basic')

        df = pd.read_html(str(basic_stat), header=1)[0]

        df = df[df["Starters"] != "Reserves"]

        df.rename(columns={'Starters': 'Players'}, inplace=True)

        # print(df)

        df.to_csv(f'./ml-nba/csv/games/{file[:-5]}_{team}.csv', index=True)

end = time.time()
print(f'execution time: {(end - start):2f} sec')