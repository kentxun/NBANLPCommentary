# NBA NLP - Final Project - CSC 582
# Data Scraping  - Yahoo Sports
# Jacob Bustamante

import csv, re
from datetime import datetime

"""
1) Get game URL list
   Iterate through each team's schedule page to get game URL list
   ex. http://sports.yahoo.com/nba/teams/lal/schedule/?season=2013_2
   30 teams - 82 games each (41home/41away) = 30 * 41 = 1230 games
   Keep url list to not duplicate a game
   NOTE: can possibly use inside hoops schedule to
   generate Yahoo's URL's since they are patterned, we just
   need the home team id yahoo uses

1.1) Remember to grab post-season as well

1.2) Build game database datastructure
     Can use Yahoo game URL string to get
     date - home - away - home_team_id


2) Get raw commentary
   Iterate through each game in game URL list and scrape commentary

2.1) Build team/player database datastructure as well
     Note: player-team relationships needed for Yahoo commentary
     
2.2) Possible player stats scrape
     Possibly grab stats / leaders / etcs.

"""


team_id = {
    'Atlanta Hawks' : '01',
    'Boston Celtics' : '02',
    'Brooklyn Nets' : '17',
    'Charlotte Bobcats' : '30',
    'Chicago Bulls' : '04',
    'Cleveland Cavaliers' : '05',
    'Dallas Mavericks' : '06',
    'Denver Nuggets' : '07',
    'Detroit Pistons' : '08',
    'Golden State Warriors' : '09',
    'Houston Rockets' : '10',
    'Indiana Pacers' : '11',
    'Los Angeles Clippers' : '12',
    'Los Angeles Lakers' : '13',
    'Memphis Grizzlies' : '29',
    'Miami Heat' : '14',
    'Milwaukee Bucks' : '15',
    'Minnesota Timberwolves' : '16',
    'New Orleans Pelicans' : '03',
    'New York Knicks' : '18',
    'Oklahoma City Thunder' : '25',
    'Orlando Magic' : '19',
    'Philadelphia 76ers' : '20',
    'Phoenix Suns' : '21',
    'Portland Trail Blazers' : '22',
    'Sacramento Kings' : '23',
    'San Antonio Spurs' : '24',
    'Toronto Raptors' : '28',
    'Utah Jazz' : '26',
    'Washington Wizards' : '27'
}

# game_date = datetime.strptime(game[0], '%a %b %d %Y').strftime('%Y%m%d')
# game = [date, Box Score, Away team, score, Home team, score, OT?, notes?]
# http://sports.yahoo.com/nba/chicago-bulls-miami-heat-2013102914/

def create_game_url_list():
    base_url = "http://sports.yahoo.com/nba/"
    
    csv = open("leagues_NBA_2014_games_games.csv").read().rstrip()
    games = [game.split(',') for game in csv.split('\n')]
    
    urls = []
    for game in games:
        date_string = datetime.strptime(game[0], '%a %b %d %Y').strftime('%Y%m%d')
        team_string = '-'.join(game[2].lower().split()) + '-' + '-'.join(game[4].lower().split())
        unique_string = team_string + '-' + date_string + team_id[game[2]]
        full_url = base_url + unique_string + '/'
        urls.append(full_url)
    
    return urls


