#bowler : 10
#runs of bat : 11
#extras : 12
import pandas as pd
import csv

data = pd.read_csv('bowlingdata.csv', sep=",")
data = data[['match_id', 'venue', 'innings', 'striker', 'bowler', 'runs_off_bat', 'extras']]
length = data.shape[0]

file1 = open('edit.csv', 'w', newline='')
writer = csv.writer(file1)
writer.writerow([ 'matchid', 'venue', 'innings', 'striker', 'bowler', 'runs'])

i=0
while(i!=length-1):
    name = ""
    checklist = []
    scorelist = []
    j=data.iloc[i,2]
    while (data.iloc[i,2]==j):  
        batbowler = [str(data.iloc[i,3]), str(data.iloc[i,4])]
        if batbowler not in checklist:
            checklist.append(batbowler)
            scorelist.append(0)
        a = checklist.index(batbowler)
        scorelist[a] = scorelist[a] + int(data.iloc[i,5]) + int(data.iloc[i,6])
        i=i+1
        if i == length-1:
            break 
    for k in range (0,len(checklist)):
        writer.writerow([data.iloc[i-1,0], data.iloc[i-1,1], data.iloc[i-1,2], checklist[k][0], checklist[k][1], scorelist[k]])

file1.close