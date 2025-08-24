-- Aggregated Tables
CREATE TABLE IF NOT EXISTS aggregated_transaction (
    State VARCHAR(255),
    Year INT,
    Quater INT,
    Transaction_type VARCHAR(255),
    Transaction_count DOUBLE,
    Transaction_amount DOUBLE
);

CREATE TABLE IF NOT EXISTS aggregated_insurance (
    State VARCHAR(255),
    Year INT,
    Quater INT,
    Insurance_type VARCHAR(255),
    Insurance_count DOUBLE,
    Insurance_amount DOUBLE
);

CREATE TABLE IF NOT EXISTS aggregated_user (
    State VARCHAR(255),
    Year INT,
    Quater INT,
    Brands VARCHAR(255),
    User_count DOUBLE,
    Percentage FLOAT
);

-- Map Tables
CREATE TABLE IF NOT EXISTS map_transaction (
    State VARCHAR(255),
    Year INT,
    Quater INT,
    District VARCHAR(255),
    Transaction_count DOUBLE,
    Transaction_amount DOUBLE
);

CREATE TABLE IF NOT EXISTS map_insurance (
    State VARCHAR(255),
    Year INT,
    Quater INT,
    District VARCHAR(255),
    Insurance_count DOUBLE,
    Insurance_amount DOUBLE
);

CREATE TABLE IF NOT EXISTS map_user (
    State VARCHAR(255),
    Year INT,
    Quater INT,
    District VARCHAR(255),
    RegisteredUsers DOUBLE,
    AppOpens DOUBLE
);

-- Top Tables
CREATE TABLE IF NOT EXISTS top_transaction (
    State VARCHAR(255),
    Year INT,
    Quater INT,
    Entity_Level VARCHAR(255),
    Entity_Name VARCHAR(255),
    Transaction_count DOUBLE,
    Transaction_amount DOUBLE
);

CREATE TABLE IF NOT EXISTS top_insurance (
    State VARCHAR(255),
    Year INT,
    Quater INT,
    Entity_Level VARCHAR(255),
    Entity_Name VARCHAR(255),
    Insurance_count DOUBLE,
    Insurance_amount DOUBLE
);

CREATE TABLE IF NOT EXISTS top_user (
    State VARCHAR(255),
    Year INT,
    Quater INT,
    Entity_Level VARCHAR(255),
    Name VARCHAR(255),
    Registered_Users VARCHAR(255)
);
