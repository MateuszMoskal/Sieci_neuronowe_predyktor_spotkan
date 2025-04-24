def getColumnLabels(dataset):
    if dataset == "laliga":
        return [["Home Team Goals Scored", "Away Team Goals Scored"], 
                ["Home Team", "Away Team"]]
    elif dataset == "worldcup":
        return [["home_score", "away_score"],
                ["home_team", "away_team"]]