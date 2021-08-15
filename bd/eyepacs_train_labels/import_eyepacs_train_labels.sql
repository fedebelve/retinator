USE retinator;
CREATE TABLE eyepacs_train_labels (
    num INT NOT NULL, 
    eye VARCHAR(5) NOT NULL,
    rd_level TINYINT,
    PRIMARY KEY(num, eye)
);

SHOW VARIABLES LIKE "secure_file_priv";

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/eyepacs_train_labels.csv'
INTO TABLE eyepacs_train_labels
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/* Cantidad de imágenes con RD */
SELECT COUNT(*)
FROM eyepacs_train_labels l
WHERE l.rd_level > 0;