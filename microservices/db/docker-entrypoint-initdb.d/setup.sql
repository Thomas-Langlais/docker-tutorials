CREATE TABLE Users(
    Id SERIAL PRIMARY KEY,
    FirstName varchar(150) NOT NULL
);

INSERT INTO Users(FirstName) VALUES ('Thomas'),
    ('Josh'),
    ('Mathieu'),
    ('Jeff');