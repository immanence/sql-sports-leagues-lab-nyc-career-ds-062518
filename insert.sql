INSERT INTO leagues (name)
VALUES ("DC"), ("Marvel");

INSERT INTO teams (name, league_id)
VALUES ("Justice League", 1), ("Avengers", 2), ("X-Men", 2), ("New York City", 1);

INSERT INTO players (name, team_id)
VALUES ("Wonder Woman", 1), ("Batman", 4), ("Iron Man", 2), ("Deadpool", 3);

INSERT INTO games (date, location)
VALUES ("2018-07-10", "New York"), ("2017-06-26", "Boston"), ("2011-11-22", "Austin");

INSERT INTO team_games (team_id, game_id, score)
VALUES (1, 1, 22), (2, 1, 35), (3, 2, 5), (4, 2, 92), (2, 3, 17), (4, 3, 27);
