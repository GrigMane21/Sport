
INSERT INTO teams (name, city) VALUES 
('Lions FC', 'London'), 
('Eagles United', 'New York'), 
('Tigers SC', 'Tokyo');


INSERT INTO players (team_id, full_name, position, salary)
SELECT 
    (random() * 2 + 1)::int,
    'Player_Name_' || s.i,
    (ARRAY['Forward', 'Defender', 'Midfielder', 'Goalkeeper'])[floor(random() * 4 + 1)],
    (random() * 800000 + 20000)::decimal(12,2)
FROM generate_series(1, 15000) AS s(i);


INSERT INTO matches (home_team_id, away_team_id, match_date, stadium) 
VALUES (1, 2, '2024-05-10', 'Olympic Stadium');

INSERT INTO goals (match_id, player_id, goal_minute) 
VALUES (1, 5, 24), (1, 12, 88);
CREATE INDEX idx_players_salary_pos ON players(salary, position);

