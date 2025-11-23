--CREATE TABLE Students(id INTEGER PRIMARY KEY AUTOINCREMENT,
--                      firstname TEXT NOT NULL,
--                      lastname TEXT NOT NULL,
--                      dob TEXT NOT NULL);
--CREATE TABLE Marks(id INTEGER PRIMARY KEY AUTOINCREMENT,
--                      student_id INTEGER,
--                      subject TEXT NOT NULL,
--                      mark INTEGER);

--INSERT INTO Marks(student_id, subject, mark)
--              VALUES(1,'English',50),
--                    (1,'Maths',100),
--                    (2,'English',67),
--                    (2,'Science',80),
--                    (3,'English',24),
--                    (4,'English',97),
--                    (5,'Maths',82),
--                    (5,'Science',5);

--1 YES
SELECT lastname, dob FROM Students;
--2 
SELECT * FROM Students;
--3 YES
SELECT firstname, lastname, dob FROM Students
    WHERE dob LIKE '%%%%%%2007';
--4 
SELECT * FROM Students;
--5 
SELECT * FROM Students;
--6 
SELECT * FROM Students;
--7 
SELECT * FROM Students;