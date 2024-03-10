-- DATABASE Creation
CREATE DATABASE weather;

-- TABLE in order to deal with the count of API consulted per day
DROP TABLE count_per_day;
CREATE TABLE IF NOT EXISTS count_per_day (
    id SERIAL PRIMARY KEY,
    count INTEGER NOT NULL DEFAULT 1,
    date DATE DEFAULT CURRENT_DATE
);

