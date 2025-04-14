def find_surebets(games):
    surebets = []
    for game in games:
        odd1 = game["odd1"]
        odd2 = game["odd2"]
        total = (1/odd1) + (1/odd2)
        if total < 1:
            profit_percent = round((1/total - 1) * 100, 2)
            game["profit"] = profit_percent
            surebets.append(game)
    return surebets