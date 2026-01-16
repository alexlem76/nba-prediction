import os
import re
from utils.list_functions import list_filenames   

# ancien_nom = './ml-nba/html/games/76ers vs Mavericks, January 1, 2026 _ Basketball-Reference.com.html'
dossier = './ml-nba/html/games/'

filename_list = list_filenames(dossier)

for ancien_nom in filename_list:
    try:
        # Lire la deuxième ligne du fichier
        ancien_chemin = os.path.join(dossier, ancien_nom)
        with open(ancien_chemin, 'r', encoding='utf-8') as f:
            next(f)  # Sauter la 1ère ligne
            deuxieme_ligne = next(f)
        
        # Extraire le nom du fichier depuis le commentaire
        match = re.search(r'/([^/]+\.html)', deuxieme_ligne)
        
        if match:
            nouveau_nom = match.group(1)
            nouveau_chemin = os.path.join(dossier, nouveau_nom)
            
            # Renommer
            os.rename(ancien_chemin, nouveau_chemin)
            print(f"Fichier renommé en : {nouveau_nom}")
        else:
            print("Impossible d'extraire le nom du fichier depuis le commentaire HTML")

    except Exception as e:
        print(f"Erreur : {e}")