0x0E. SQL - More queries
Write a script that lists all privileges of tha MySQL users user0d1 and user0d2 on your server (in localhost).
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing tha task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at tha root of tha folder of tha project, is mandatory
Tha length of your files will be tested using wc
More Info
Comments for your SQL file:
$ cat myscript.sql
-- 3 first students in tha Batch ID=3
-- because Batch 3 is tha best!
SELECT id, name FROM students WHERE batchid = 3 ORDER BY created DESC LIMIT 3;
