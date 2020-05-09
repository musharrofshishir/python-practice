CREATE TABLE flights(
    id SERIAL PRIMARY KEY, 
    origin VARCHAR (50) NOT NULL,
    destination VARCHAR (50) NOT NULL
    
);

CREATE TABLE passengers(
    id SERIAL PRIMARY KEY,
    name VARCHAR (50) NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers(name, flight_id) VALUES('Kazi','2');
INSERT INTO passengers(name, flight_id) VALUES('Zahed','1');
INSERT INTO passengers(name, flight_id) VALUES('Musharrof','3');
INSERT INTO passengers(name, flight_id) VALUES('Shishir','5');