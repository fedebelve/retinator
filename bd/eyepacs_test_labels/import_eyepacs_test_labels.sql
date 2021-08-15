USE retinator;
CREATE TABLE eyepacs_test_labels (
    num INT NOT NULL, 
    eye VARCHAR(5) NOT NULL,
    rd_level TINYINT,
    image_usage VARCHAR(8),
    PRIMARY KEY(num, eye)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/eyepacs_test_labels.csv'
INTO TABLE eyepacs_test_labels
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/* Cantidad de imágenes con RD */
SELECT COUNT(*)
FROM eyepacs_test_labels l
WHERE l.rd_level > 0;