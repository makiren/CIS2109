create table Enrollment
(
    Student_ID char(8) not null,
    Course_ID  char(7) not null,
    primary key (Course_ID, Student_ID),
    constraint enroll_course_fk
        foreign key (Course_ID) references Course (Course_ID),
    constraint enroll_student_fk
        foreign key (Student_ID) references Student (Student_ID)
);

