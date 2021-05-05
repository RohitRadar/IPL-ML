import pandas as pd
import csv

data = pd.read_csv('1/bowlingdata.csv', sep=",")
data = data[['season', 'venue', 'innings', 'batting_team', 'bowling_team','striker','bowler', 'runs_off_bat', 'extras']]
length = data.shape[0]

file1 = open('1/clean1.csv', 'w', newline='')
writer = csv.writer(file1)
writer.writerow(['season', 'venue', 'innings', 'batting_team', 'bowling_team', 'runs','batsmen','bowlers'])

#CLEAN
i=0
while(i!=length-1):
    #SEASON
    season = data.iloc[i,0]
    if str(data.iloc[i,0]) == "2020/21":
        season = 2020
    season = int(season) - 2010
    
    #TEAM
    team = list(data.iloc[i,3].split(" "))
    if "Chennai" in team:
        teamname = "che"
    elif "Challengers" in team:
        teamname = "ban"
    elif "Hyderabad" in team:
        teamname = "hyd"
    elif "Deccan" in team:
        teamname = "hyd"
    elif "Indians" in team:
        teamname = "mum"
    elif "Delhi" in team:
        teamname = "del"
    elif "Rajasthan" in team:
        teamname = "rr"
    elif "Kolkata" in team:
        teamname = "kol"
    else:
        teamname = "pun"
    
    #VENUE 
    name = list(data.iloc[i,1].split(" "))
    if "Chinnaswamy" in name:
        ven = "che"
    elif "M" in name:
        ven = "ban"    
    elif "Punjab" in name:
        ven = "pun"    
    elif "Kotla" in name:
        ven = "del"    
    elif "Wankhede" in name:
        ven = "mum"    
    elif "Arun" in name:
        ven = "del"    
    elif "Rajiv" in name:
        ven = "hyd"    
    elif "MA" in name:
        ven = "che"    
    elif "Eden" in name:
        ven = "kol"        
    elif "Chidambaram" in name:
        ven = "che"    
    elif "Patel" in name:
        ven = "ahm"
    elif "Modi" in name:
        ven  = "ahm"
    elif "Narendra" in name:
        ven = "ahm"
    else:
        ven = data.iloc[i-1,1]
    batsmen = 0
    bowlers = 0
    bowlist = []
    batlist = []
    runs = 0
    j=data.iloc[i,2]
    while (data.iloc[i,2]==j):
        runs = runs + int(data.iloc[i,7]) + int(data.iloc[i,8])
        strike = str(data.iloc[i,5])
        bowl = str(data.iloc[i,6])
        if strike not in batlist:
            batsmen = batsmen+1
            batlist.append(strike)
        if bowl not in bowlist:
            bowlers = bowlers+1
            bowlist.append(bowl)
        i=i+1
        if i == length-1:
            break 
    writer.writerow([season, ven, data.iloc[i-1,2], teamname, data.iloc[i-1,4], runs, batsmen, bowlers])

file1.close