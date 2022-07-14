create table Semester
(
    Semester_ID char(7) not null,
    Course_ID   char(7) not null,
    primary key (Course_ID, Semester_ID),
    constraint Semester_Course_Course_ID_fk
        foreign key (Course_ID) references Course (Course_ID)
);

INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('FAL2022', 'CIS0835');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('SUM2022', 'CIS0835');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('FAL2022', 'CIS1051');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('SUM2022', 'CIS1051');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('FAL2022', 'CIS1057');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('SUM2022', 'CIS1057');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('SUM2022', 'CIS1068');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('SUM2022', 'CIS1166');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('FAL2022', 'CIS2107');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('SUM2022', 'CIS2109');
INSERT INTO student_management.Semester (Semester_ID, Course_ID) VALUES ('FAL2022', 'CIS2166');
