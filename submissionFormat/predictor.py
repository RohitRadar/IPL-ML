### Custom definitions and classes if any ###
### Custom definitions and classes if any ###
import pandas as pd
import numpy as np
import pickle
import math

def predictRuns(testInput):
    ### Your Code Here ###
    import pandas as pd
import numpy as np
import pickle

def predictRuns(testInput):
    ### Your Code Here ###
    prediction = 0
    data = pd.read_csv(testInput, sep=",")
    season = 11
    matchno = 8
    ven = 44.25   
    innings = data.iloc[0,1]
    team = list(data.iloc[0,2].split(" "))
    if "Chennai" in team:
        team = 1
    elif "Challengers" in team:
        team = 0
    elif "Hyderabad" in team:
        team = 3
    elif "Deccan" in team:
        team = 2
    elif "Indians" in team:
        team = 5
    elif "Delhi" in team:
        team = 2
    elif "Rajasthan" in team:
        team = 7
    elif "Kolkata" in team:
        team = 4
    else:
        teamname = 6
    bats = list(data.iloc[0,4].split(","))
    bowls = list(data.iloc[0,5].split(","))
    bat = len(bats)
    bowl = len(bowls)
    #data1 = [{'season':season, 'matchno':matchno, 'venue':ven, 'innings':innings, 'team':team, 'batsmen':bat, 'bowlers':bowl}]
    #df = pd.DataFrame(data1)
    df = np.array([[season,matchno,ven,innings,team,bat,bowl]])
    pickle_in = open('lr.pickle', "rb")
    linear = pickle.load(pickle_in)
    predicted= linear.predict(df)
    if predicted%1 <0.5:
        prediction = predicted//1
    else:
        prediction = (predicted//1) + 1
    return int(prediction)
