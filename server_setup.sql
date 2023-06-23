-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS NullExplicit_test_db;
CREATE USER IF NOT EXISTS 'NULL_TEST_USER'@'localhost' IDENTIFIED BY 'NULL_TEST_USER';
GRANT ALL PRIVILEGES ON `NullExplicit_test_db`.* TO 'NULL_TEST_USER'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'NULL_TEST_USER'@'localhost';
FLUSH PRIVILEGES;