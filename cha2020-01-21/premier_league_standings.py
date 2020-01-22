def premier_league_standings(teams):
    ranks = teams.copy()
    res = {1: ranks.pop(1)}
    res.update({k: v for k,v in enumerate(sorted(ranks.values()), 2)})
    return res
