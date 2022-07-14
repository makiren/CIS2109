create table Student
(
    Student_ID   char(8)     not null
        primary key,
    Student_name varchar(50) not null
);

INSERT INTO student_management.Student (Student_ID, Student_name) VALUES ('tuk40001', 'John Doe');
INSERT INTO student_management.Student (Student_ID, Student_name) VALUES ('tuk40005', 'Jane Doe');
INSERT INTO student_management.Student (Student_ID, Student_name) VALUES ('tuk40010', 'Owl Hooter');
INSERT INTO student_management.Student (Student_ID, Student_name) VALUES ('tuk40015', 'Master Yoda');
