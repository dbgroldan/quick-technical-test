CREATE SCHEMA IF NOT EXISTS user_schema;
CREATE TABLE IF NOT EXISTS user_schema.user(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(250) NOT NULL,
  last_name VARCHAR(250) NOT NULL,
  email VARCHAR(250) NOT NULL UNIQUE,
  password VARCHAR(250) NOT NULL,
  token VARCHAR(255) NOT NULL,
  age INT CONSTRAINT alive_user CHECK (age < 100),
  image VARCHAR(250),
  description VARCHAR(255)
);
