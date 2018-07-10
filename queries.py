
def select_name_of_player_with_shortest_name():
    return """SELECT name FROM players ORDER BY length(name) LIMIT 1"""

def select_all_new_york_players_names():
    return """SELECT players.name FROM players
                JOIN teams ON teams.id = players.team_id
                WHERE teams.name LIKE '%New York%'
                """

def select_team_name_and_total_goals_scored_for_new_york_rangers():
    return """SELECT teams.name, sum(team_games.score) FROM team_games
                JOIN teams ON teams.id = team_games.team_id
                WHERE teams.name = "New York Rangers"
                GROUP BY teams.name
                """

def select_all_games_date_and_info_teams_name_and_score_for_teams_in_nhl():
    return """SELECT games.date, games.info, teams.name, team_games.score FROM games
                JOIN team_games ON team_games.game_id = games.id
                JOIN teams ON team_games.team_id = teams.id
                JOIN leagues ON leagues.id = teams.league_id
                WHERE leagues.name = "NHL"
                """

def select_date_info_and_total_points_for_highest_scoring_nba_game():
    return """SELECT games.date, games.info, SUM(team_games.score) FROM games
                JOIN team_games ON team_games.game_id = games.id
                JOIN teams ON team_games.team_id = teams.id
                JOIN leagues ON leagues.id = teams.league_id
                GROUP BY games.date
                ORDER BY SUM(team_games.score) DESC
                LIMIT 1
                """
