import pandas as pd
import csv

data = pd.read_csv('1/clean1.csv', sep=",")
data = data[['season', 'venue', 'innings', 'batting_team', 'bowling_team', 'runs','batsmen','bowlers']]
length = data.shape[0]

file1 = open('1/clean2.csv', 'w', newline='')
writer = csv.writer(file1)
writer.writerow(['season', 'matchno', 'venue', 'innings', 'batting_team', 'runs','batsmen','bowlers'])


i = 0
while(i!=length-1):
    l=i
    matchno = []
    matchtotal = []
    batteam = []
    venuelength = []
    scorelist = []
    venuelist = []
    j = data.iloc[i,0]
    while(data.iloc[i,0]==j):
        bat = data.iloc[i,3]
        if bat not in batteam:
            batteam.append(bat)
            matchtotal.append(0)
            matchno.append(0)
        a = batteam.index(bat)
        matchtotal[a] = matchtotal[a] + 1
        matchno[a] = matchno[a] + 1

        venue = data.iloc[i,1]
        if venue not in venuelist:
            venuelist.append(venue)
            scorelist.append(0)
            venuelength.append(0)
            matchno.append(0)
        score = data.iloc[i,5]
        a = venuelist.index(venue)
        scorelist[a] = scorelist[a] + score
        venuelength[a] = venuelength[a] + 1
        i=i+1
        if i == length-1:
            break
    for k in range(0,len(venuelength)):
        scorelist[k] = scorelist[k]/venuelength[k] 
        if int(data.iloc[i-1,0]) == 11:
            print(venuelist[k],"'s runs : ",scorelist[k])

    for k in range(l,i):
        ven = data.iloc[k,1]
        a = venuelist.index(ven)
        venue = scorelist[a]
        mat = data.iloc[k,3]
        a = batteam.index(mat)
        matchno[a] = matchno[a] - 1
        match = matchtotal[a]-matchno[a]
        writer.writerow([data.iloc[k,0], match, venue, data.iloc[k,2], data.iloc[k,3], data.iloc[k,5], data.iloc[k,6], data.iloc[k,7]])

file1.close

"""
i = 0
venuelength = []
scorelist = []
venuelist = []
while(i!=length-1):
    venue = data.iloc[i,1]
    if venue not in venuelist:
        venuelist.append(venue)
        scorelist.append(0)
        venuelength.append(0)
    score = data.iloc[i,5]
    a = venuelist.index(venue)
    scorelist[a] = scorelist[a] + score
    venuelength[a] = venuelength[a] + 1
    i=i+1


for i in range(0,len(venuelength)):
    scorelist[i] = scorelist[i]/venuelength[i] 
    print(venuelist[i],"'s runs : ",scorelist[i])

i = 0
while(i!=length):
    ven = data.iloc[i,1]
    a = venuelist.index(ven)
    venue = scorelist[a]
    writer.writerow([data.iloc[i,0], venue, data.iloc[i,2], data.iloc[i,3], data.iloc[i,5], data.iloc[i,6], data.iloc[i,7]])
    i=i+1
"""

