# importing all things we need from nba_api
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import teamgamelog
import pandas as pd 
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.endpoints import commonplayerinfo
#consistant variables
player_dict = players.get_players()
teams = teams.get_teams()



#determin 2 teams compared
a = "Philadelphia 76ers"
b = "San Antonio Spurs"
#getting team IDs
Team1 = [x for x in teams if x['full_name'] == a][0]
Team1_id = Team1['id']
Team2 = [x for x in teams if x['full_name'] == b][0]
Team2_id = Team2['id']

#find games played by a team or player
Team1_Current = teamgamelog.TeamGameLog(Team1_id).get_data_frames()[0]
Team2_Current = teamgamelog.TeamGameLog(Team2_id).get_data_frames()[0]

#find current roster for each team
Team1_Roster = commonteamroster.CommonTeamRoster(Team1_id).get_data_frames()[0]
Team2_Roster = commonteamroster.CommonTeamRoster(Team2_id).get_data_frames()[0]


#find player ids for everyone on both teams
Team1_PlayerIds = Team1_Roster[['PLAYER_ID']]
Team1_PlayerIds_list = pd.DataFrame(Team1_Roster,columns=['PLAYER_ID'])
Team1_PlayerIds = Team1_PlayerIds_list.values.tolist()
Team2_PlayerIds = Team2_Roster[['PLAYER_ID']]
Team2_PlayerIds_list = pd.DataFrame(Team2_Roster,columns=['PLAYER_ID'])
Team2_PlayerIds = Team2_PlayerIds_list.values.tolist()

#for i in range(len(Team1_PlayerIds)):
Team1_PlayerInfo = commonplayerinfo.CommonPlayerInfo(Team1_PlayerI[0]).get_data_frames()[1]
print(Team1_PlayerInfo[i])
#for i in range(len(Team2_PlayerIds)):
Team2_PlayerInfo = commonplayerinfo.CommonPlayerInfo(Team2_PlayerIds[0]).get_data_frames()[1]
print(Team2_PlayerInfo[i])

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

#adding win percent to each team's chances
team1_Score = (team1_w_pct_final[0]*100)
team2_Score = (team2_w_pct_final[0]*100)
#print(team1_Score)
#print(team2_Score)

#adding team score per min to each team's chances
team1_Score = team1_Score + (Final_mean_Team1PTS[0]/Final_mean_Team1MIN[0])*100
team2_Score = team2_Score + (Final_mean_Team2PTS[0]/Final_mean_Team2MIN[0])*100


#print(team1_Score)
#print(team2_Score)


#displaying prediction
if team1_Score > team2_Score :
    print(a,"will win")
else:
    print(b,"will win")


