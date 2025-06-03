CREATE DATABASE IF NOT EXISTS todo_list;

USE todo_list;

CREATE TABLE IF NOT EXISTS users  (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    short_description VARCHAR(255) NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT IGNORE INTO users (
    id, name, email
) VALUES (1, 'rafael', 'dev@rafael.com'), (2, 'gustavo', 'dev@gustavo.com');


INSERT IGNORE tasks (
    id, short_description, user_id
) VALUES (1, 'some description', 1), (2 , 'some description test 2', 2);