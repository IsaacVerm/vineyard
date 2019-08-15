USE vineyard

INSERT INTO cleaned_weather_station (moment, temperature, rainfall)
VALUES
('2019-01-01 01:00:00',30,60),
('2019-01-01 01:00:00',28,0),
('2019-01-01 01:00:00',20,10),
('2019-01-01 01:00:00',10,14),
('2019-01-01 01:00:00',25,19);

INSERT INTO output_model (moment, prediction_boolean, prediction_percentage)
VALUES
('2019-01-01 01:00:00',0,34),
('2019-01-01 01:00:00',1,23),
('2019-01-01 01:00:00',1,15),
('2019-01-01 01:00:00',0,52),
('2019-01-01 01:00:00',1,90);