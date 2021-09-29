CREATE DATABASE todos_db;

USE todos_db;

CREATE TABLE users(
	username VARCHAR(50) NOT NULL PRIMARY KEY,
    password VARCHAR(250) NOT NULL
);

CREATE TABLE todos(
	todo_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	todo VARCHAR(500) NOT NULL,
    completed BOOL NOT NULL,
    username VARCHAR(50) NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
);

INSERT INTO users(username, password)
VALUES( 'michael08', 'pass123' ),
	  ( 'julie27', 'pass456' ),
      ( 'alfredo123', 'pass555' );

INSERT INTO todos(todo, completed, username)
VALUES( 'Wash the dishes', FALSE, 'michael08' ),
	  ( 'Clean the house', FALSE, 'michael08' ),
	  ( 'Go to the GYM', TRUE, 'julie27' ),
	  ( 'Make a birthday cake', FALSE, 'julie27' ),
	  ( 'Explain POST method', TRUE, 'alfredo123' ),
	  ( 'Explain sessions', TRUE, 'alfredo123' );