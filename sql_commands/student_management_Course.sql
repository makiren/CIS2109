create table Course
(
    Course_ID   char(7)      not null
        primary key,
    Course_name varchar(100) not null
);

INSERT INTO student_management.Course (Course_ID, Course_name) VALUES ('CIS0835', 'Cyberspace & Society');
INSERT INTO student_management.Course (Course_ID, Course_name) VALUES ('CIS1051', 'Introduction to Problem Solving and Programming in Python');
INSERT INTO student_management.Course (Course_ID, Course_name) VALUES ('CIS1057', 'Computer Programming in C');
INSERT INTO student_management.Course (Course_ID, Course_name) VALUES ('CIS1068', 'Program Design and Abstraction');
INSERT INTO student_management.Course (Course_ID, Course_name) VALUES ('CIS1166', 'Mathematical Concepts in Computing I');
INSERT INTO student_management.Course (Course_ID, Course_name) VALUES ('CIS2107', 'Computer Systems and Low-Level Programming');
INSERT INTO student_management.Course (Course_ID, Course_name) VALUES ('CIS2109', 'Database Management Systems');
INSERT INTO student_management.Course (Course_ID, Course_name) VALUES ('CIS2166', 'Mathematical Concepts in Computing II');
