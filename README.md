# nba-prediction
This is a personal data/ML project. 
The goal is creating a model that predicts the result of a NBA team's game (win or lose). 
I chose my favorite team's results, the Dallas Mavericks.

### Data processing:
1) **rename_html_files.py**
    taking the date and home team name

2) **get_games_to_csv.py**
    extracting from the html game files both teams game stats
    creating one csv file for each team game stat (1 game = 2 csv stats)

3) **create_features_csv.py**
    creating an empty csv file with the features

4) **add_features.py**
    adding the fetaures
        match_id: takes the html game file name
        team: DAL
        opp: if not DAL
