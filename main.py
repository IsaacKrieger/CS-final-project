# importing all things we need from nba_api
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import teamgamelog
import pandas as pd 
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats.static import teams
#consistant variables
player_dict = players.get_players()
teams = teams.get_teams()



#determin 2 teams compared
a = "Brooklyn Nets"
b = "Utah Jazz"
#getting team IDs
Team1 = [x for x in teams if x['full_name'] == a][0]
Team1_id = Team1['id']
Team2 = [x for x in teams if x['full_name'] == b][0]
Team2_id = Team2['id']

#find games played by a team or player
Team1_Current = teamgamelog.TeamGameLog(Team1_id).get_data_frames()[0]
Team2_Current = teamgamelog.TeamGameLog(Team2_id).get_data_frames()[0]

#finding win precent and converting from dataframe to list to int
team1_w_pct = Team1_Current[["W_PCT"]]
team1_w_pct_list = pd.DataFrame(Team1_Current, columns= ['W_PCT'])
team1_w_pct = team1_w_pct_list.values.tolist()
team1_w_pct_final=(team1_w_pct[0])

team2_w_pct = Team2_Current[["W_PCT"]]
team2_w_pct_list = pd.DataFrame(Team2_Current, columns= ['W_PCT'])
team2_w_pct = team2_w_pct_list.values.tolist()
team2_w_pct_final=(team2_w_pct[0])

#Find the average points scored per game for each team and converting to a list
Team1PTS = Team1_Current[["PTS"]]
mean_Team1PTS = Team1PTS.mean()
Final_mean_Team1PTS = mean_Team1PTS.values.tolist()

Team2PTS = Team2_Current[["PTS"]]
mean_Team2PTS = Team2PTS.mean()
Final_mean_Team2PTS = mean_Team2PTS.values.tolist()

#Find the average minutes per game for each team and converting
Team1MIN = Team1_Current[["MIN"]]
mean_Team1MIN = Team1MIN.mean()
Final_mean_Team1MIN = mean_Team1MIN.values.tolist()

Team2MIN = Team2_Current[["MIN"]]
mean_Team2MIN = Team2MIN.mean()
Final_mean_Team2MIN = mean_Team2MIN.values.tolist()

#adding win percent to each team chances
team1_Score = (team1_w_pct_final[0]*100)
team2_Score = (team2_w_pct_final[0]*100)
print(team1_Score)
print(team2_Score) ho;suhifawhfe;hfdsiluhfdvs;kojdfsLIUGAFSD


team1_Score = team1_Score + (Final_mean_Team1PTS[0]/Final_mean_Team1MIN[0])*100
team2_Score = team2_Score + (Final_mean_Team2PTS[0]/Final_mean_Team2MIN[0])*100


print(team1_Score)
print(team2_Score)



if team1_Score > team2_Score :
    print(a,"will win")
else:
    print(b,"will win")

##if mean_x > mean_y:
##    print("team1 will win")
##else:
##    print("team 2 will win")

"""
Spyder Editor

This is a temporary script file.
"""

