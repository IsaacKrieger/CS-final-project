# importing all things we need from nba_api
from nba_api.stats.static import players, teams
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog, teamgamelog, teamyearbyyearstats, leaguegamefinder, commonteamroster, commonplayerinfo, playercareerstats
import pandas as pd
import time
#consistant variables
player_dict = players.get_players()
teams = teams.get_teams()

def convert(dataframe, data):
  lists = pd.DataFrame(dataframe, columns= [data])
  dataframe = lists.values.tolist()
  return(dataframe)
#determin 2 teams compared
a = "Minnesota Timberwolves"
b = "Brooklyn Nets"
team1_Score = 0
team2_Score = 0
Home = a
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
Team1_PlayerIds = convert(Team1_PlayerIds, 'PLAYER_ID')

Team2_PlayerIds = Team2_Roster[['PLAYER_ID']]
Team2_PlayerIds = convert(Team2_PlayerIds, 'PLAYER_ID')

Team1_length = len(Team1_PlayerIds)
Team2_length = len(Team2_PlayerIds)


Team1_PlayerInfo = []
Team2_PlayerInfo = []
Team1_PlayerCumeInfo = []
Team2_PlayerCumeInfo = []

for i in range(Team1_length):
    print(i)
    Team1_PlayerPIE = commonplayerinfo.CommonPlayerInfo(Team1_PlayerIds[i]).get_data_frames()[1][['PIE']]
    Team1_PlayerCumeInfo.append(playercareerstats.PlayerCareerStats(Team1_PlayerIds[i]).get_data_frames()[1])

    time.sleep(.8)
    Team1_PlayerPIE_List = Team1_PlayerPIE.values.tolist()
    Team1_PlayerInfo.append(Team1_PlayerPIE_List)
Team1_PlayerPIE_Sorted = sorted(Team1_PlayerInfo, reverse = True)
print(Team1_PlayerPIE_Sorted)

for k in range(Team2_length):
    print(k)
    Team2_PlayerPIE = commonplayerinfo.CommonPlayerInfo(Team2_PlayerIds[k]).get_data_frames()[1][['PIE']]
    Team2_PlayerCumeInfo.append(playercareerstats.PlayerCareerStats(Team2_PlayerIds[k]).get_data_frames()[1])
    time.sleep(.8)
    Team2_PlayerPIE_List = Team2_PlayerPIE.values.tolist()
    Team2_PlayerInfo.append(Team2_PlayerPIE_List)
Team2_PlayerPIE_Sorted = sorted(Team2_PlayerInfo, reverse = True)
print(Team2_PlayerPIE_Sorted)
o = 0
p = 0
for i in range (15):
  if (Team1_PlayerPIE_Sorted[o] > Team2_PlayerPIE_Sorted[p]):
    team1_Score += (15 - i)
    o += 1
  elif(Team1_PlayerPIE_Sorted[o] < Team2_PlayerPIE_Sorted[p]):
    team2_Score += (15 - i)
    p+= 1
  else:
    team1_Score += (15 - i)
    team2_Score += (15 - i)
    o+= 1
    p+= 1
    
#finding points per min of players
for k in range(Team1_length):
    Team1_CumePlayerMin = Team1_PlayerCumeInfo[k]
    Team1_PlayerMin = Team1_CumePlayerMin[['MIN']]
    Team1_PlayerMinComp = Team1_PlayerMin.values.tolist()
    print(Team1_PlayerMinComp)
    
for q in range(Team2_length):
    Team2_CumePlayerMin = Team2_PlayerCumeInfo[q]
    Team2_PlayerMin = Team2_CumePlayerMin[['MIN']]
    Team2_PlayerMinComp = Team2_PlayerMin.values.tolist()
    print(Team2_PlayerMinComp)


#finding win precent and converting from dataframe to list to int
team1_w_pct = Team1_Current[["W_PCT"]]
team1_w_pct_final = convert(team1_w_pct, 'W_PCT')[0]

team2_w_pct = Team2_Current[["W_PCT"]]
team2_w_pct_final = convert(team2_w_pct, 'W_PCT')[0]

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
team1_Score += (team1_w_pct_final[0]*100)
team2_Score += (team2_w_pct_final[0]*100)
print(team1_Score)
print(team2_Score)

#adding team score per min to each team's chances
team1_Score = team1_Score + (Final_mean_Team1PTS[0]/Final_mean_Team1MIN[0])*100
team2_Score = team2_Score + (Final_mean_Team2PTS[0]/Final_mean_Team2MIN[0])*100

print(team1_Score)
print(team2_Score)

#Addign the home teams win percentage
if Home == a:
    team1_Score = team1_Score*(1.04)
else:
    team2_Score = team2_Score*(1.04)

print(team1_Score)
print(team2_Score)

Total_Score = team1_Score+ team2_Score

Team1Percent = (team1_Score/Total_Score)*100
Team2Percent = (team2_Score/Total_Score)*100


#displaying prediction
if team1_Score > team2_Score :
    print(a,"will win")
else:
    print(b,"will win")
    
print(a, 'win percent')
print(Team1Percent)
print(b, 'win percent')
print(Team2Percent)