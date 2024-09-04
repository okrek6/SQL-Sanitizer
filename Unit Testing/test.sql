-- Sample T-SQL script for testing

-- String literals
SELECT 'Hello World' AS Greeting;
SELECT 'Another string literal' AS AnotherGreeting;

-- NVARCHAR and NCHAR types
CREATE TABLE TestTable (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Description CHAR(100)
);

-- More string literals
INSERT INTO TestTable (ID, Name, Description) VALUES (1, 'Sample Name', 'Sample Description');