create table Attendance
(
    Student_ID       char(8)  not null,
    Course_ID        char(7)  not null,
    checkin_datetime datetime not null,
    primary key (Student_ID, Course_ID),
    constraint fk1_att
        foreign key (Course_ID) references Course (Course_ID),
    constraint fk2_att
        foreign key (Student_ID) references Student (Student_ID)
);

