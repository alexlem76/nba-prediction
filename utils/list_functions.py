import pandas as pd
from bs4 import BeautifulSoup
import os

def list_filenames(directory_path):
    try:
        # Ensure the path exists and is a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a valid directory.")

        # List only files (not subdirectories)
        files = [os.path.splitext(f)[0] for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files

    except Exception as e:
        print(f"Error: {e}")
        return []


def find_opposite_team(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

    # Parse HTML content with lxml parser (faster and more robust than default)
    soup = BeautifulSoup(content, 'html.parser')
    line_score = soup.find('table', id='line_score') # prendre les deux noms d'équipes
    
    # On parcourt les lignes du tbody
    for row in line_score.tbody.find_all("tr"):
        team_cell = row.find("th", {"data-stat": "team"})
        # ne prend que l'équipe qui affronte DAL
        if team_cell and team_cell.text.strip() != 'DAL': 
            a = team_cell.find("a")
            opposite_team = a.text.strip()
    return opposite_team

def find_team_stats(csv_file_path):
    df = pd.read_csv(csv_file_path)
    stats = []
    # prend le numéro de la ligne des totaux
    totals_row = df[df['Players'] == 'Team Totals'].index[0]
    pts = df.loc[totals_row, 'PTS']
    fg_pct = df.loc[totals_row, 'FG%']
    tp_pct = df.loc[totals_row, '3P%']
    ft_pct = df.loc[totals_row, 'FT%']
    stats.append(pts, fg_pct, tp_pct, ft_pct)
    return stats

def find_opp_stats(csv_file_path):
    df = pd.read_csv(csv_file_path)
    opp_stats = []
    totals_row = df[df['Players'] == 'Team Totals'].index[0]
    opp_pts = df.loc[totals_row, 'PTS']
    opp_fg_pct = df.loc[totals_row, 'FG%']
    opp_stats.append(opp_pts, opp_fg_pct)
    return opp_stats

def find_context_stats(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')

    return content