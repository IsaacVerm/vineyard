DROP DATABASE IF EXISTS vineyard;

CREATE DATABASE vineyard;

USE vineyard;

DROP TABLE IF EXISTS cleaned_weather_station;
DROP TABLE IF EXISTS output_model;

CREATE TABLE cleaned_weather_station
(
    id INT NOT NULL
    AUTO_INCREMENT,
    moment TIMESTAMP,
    temperature INT,
    rainfall INT,
    PRIMARY KEY (id)
);

CREATE TABLE output_model
(
    id INT NOT NULL
    AUTO_INCREMENT,
    moment TIMESTAMP,
    prediction_boolean TINYINT (1),
    prediction_percentage INT,
    PRIMARY KEY (id)
);