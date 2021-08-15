USE retinator;
CREATE TABLE eyepacs_gradability_grades (
	/*id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,*/
    num INT NOT NULL, 
    eye VARCHAR(5) NOT NULL,
    gradability BOOLEAN,
    PRIMARY KEY(num, eye)
);

SHOW VARIABLES LIKE "secure_file_priv";

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/eyepacs_gradability_grades.csv'
INTO TABLE eyepacs_gradability_grades
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * 
FROM eyepacs_gradability_grades;

SELECT COUNT(*)
FROM eyepacs_gradability_grades;