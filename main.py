import tkinter
import pymysql as pymy

# ! Database has to be created before the run!
# * Set up connection following database setting
connection = pymy.connect(host='localhost', port=3306,
                          user='root', password='2740',
                          db='student_management',
                          cursorclass=pymy.cursors.DictCursor)
cursor = connection.cursor()

# This Repository is for CIS 2109 Group Project.
# Refer to StudentManagement.jpg
# for the database design that is assumed on this project.

# * Start of element assignment of GUI *
root = tkinter.Tk()

root.title("TUJ Student Repository")
root.geometry('1024x768')
global frame_left, frame_right
frame_left = tkinter.Frame(root, bg='#9D2235', width="724", height="768")  # Temple Color
frame_right = tkinter.Frame(root, bg='gray', width="300", height="768")
frame_right.pack(side="right")
frame_left.pack(side="left")

global text  # * global text for label
text = 'This is text variable'
label_head = tkinter.Label(frame_left, text=text,
                           font=('Lucida Console', '25', 'bold'), justify='center', fg='white', bg='maroon',
                           anchor='center')  # ! Not placed, just declared!

# * TU Logo
tu_image = tkinter.PhotoImage(file='temple-logo-t-box.png')
disp_image = tkinter.Label(frame_left, image=tu_image)
disp_image.place(anchor="n", x=362, y=0)
# Welcome message
welcome = tkinter.Label(frame_left, text='Welcome to TUJ Student Repository',
                        justify='center', fg='white', bg='black',
                        anchor='center', font=("Lucida Console", "20", "bold"))
welcome.place(anchor='n', x=362, rely=0.16)


# * ----- FUNCTIONS FOR EACH BUTTONS -----


def common_parts():
    # frame_left = tkinter.Frame(root, bg='#9D2235', width="724", height="768")  # Temple Color
    # frame_right = tkinter.Frame(root, bg='gray', width="300", height="768")
    # frame_right.pack(side="right")
    # frame_left.pack(side="left")

    # TU Logo
    tu_image = tkinter.PhotoImage(file='temple-logo-t-box.png')
    disp_image = tkinter.Label(frame_left, image=tu_image)
    disp_image.place(anchor="n", x=362, y=1)


def add_student():  # Adding new student(first button)
    for widget in frame_left.winfo_children():
        widget.place_forget()
    # clear_left_frame()
    common_parts()

    text = 'Register to a New Course'
    label_head.config(text=text)
    label_head.place(anchor='n', x=362, rely=0.20)

    label_id.place(x=300, y=250, anchor='e')
    id_box.place(x=560, y=250, anchor='e')

    # Name label + box
    # label_name.place(x=300, y=290, anchor='e')
    # name_box.place(x=560, y=290, anchor='e')

    # Course ID label + box
    label_course_id.place(x=300, y=330, anchor='e')
    course_id_box.place(x=560, y=330, anchor='e')

    # Login Button
    button_submit_as.place(x=380, y=370, anchor='e')

    # Depreciated
    # label_as = tkinter.Label(frame_left, text='ADD Student', font=('Lucida Console', '25', 'bold'))
    # label_as.place(x=300, y=362)


def add_attendance():
    for widget in frame_left.winfo_children():
        widget.place_forget()
    common_parts()
    text = "CHECK-IN TODAY'S CLASS"

    label_head.config(text=text)
    label_head.place(anchor='n', x=362, rely=0.20)

    label_id.place(x=300, y=250, anchor='e')
    id_box.place(x=560, y=250, anchor='e')

    # Name label + box
    # label_name.place(x=300, y=290, anchor='e')
    # name_box.place(x=560, y=290, anchor='e')

    # Course ID label + box
    label_course_id.place(x=300, y=330, anchor='e')
    course_id_box.place(x=560, y=330, anchor='e')

    # Login Button
    button_submit_aa.place(x=380, y=370, anchor='e')

    # Depreciated
    # label_aa = tkinter.Label(frame_left, text='Check-in', font=('Lucida Console', '10', 'bold'))
    # label_aa.place(x=300, y=362)


def view_record():
    for widget in frame_left.winfo_children():
        widget.place_forget()
    common_parts()
    label_head.config(text="Enter Your TUID. Registration Data will be on Console Window.")
    label_head.place(anchor='n', x=362, rely=0.20)

    # ID label + box
    label_id.place(x=300, y=250, anchor='e')
    id_box.place(x=560, y=250, anchor='e')

    # # Name label + box
    # label_name.place(x=300, y=290, anchor='e')
    # name_box.place(x=560, y=290, anchor='e')
    #
    # # Course ID label + box
    # label_course_id.place(x=300, y=330, anchor='e')
    # course_id_box.place(x=560, y=330, anchor='e')

    # Login Button
    button_submit_vr.place(x=380, y=370, anchor='e')

    # Depreciated
    # label_vr = tkinter.Label(frame_left, text='View', font=('Lucida Console', '15', 'bold'))
    # label_vr.place(x=300, y=362)


def delete_record():
    for widget in frame_left.winfo_children():
        widget.place_forget()
    common_parts()

    text = 'Be Cautious! This will delete your registration IMMEDIATELY!'
    label_head.config(text=text)
    label_head.place(anchor='n', x=362, rely=0.20)

    label_id.place(x=300, y=250, anchor='e')
    id_box.place(x=560, y=250, anchor='e')

    # # Name label + box
    # label_name.place(x=300, y=290, anchor='e')
    # name_box.place(x=560, y=290, anchor='e')

    # Login Button
    button_submit_dr.place(x=380, y=370, anchor='e')

    # Depreciated
    # label_dr = tkinter.Label(frame_left, text='Delete', font=('Lucida Console', '5', 'bold'))
    # label_dr.place(x=300, y=362)


def is_valid(tuid):  # TUID validation function
    if not tuid.encode('utf-8').isalnum():
        return False
    return True


def sql_as():
    id_input = id_box.get()
    name_input = name_box.get()
    course_id_input = course_id_box.get()
    id_box.delete(0, 100)
    name_box.delete(0, 100)
    course_id_box.delete(0, 100)
    with cursor:
        sql = "INSERT INTO Enrollment (Student_ID, Course_ID) VALUES (%s, %s);"
        was_commited = cursor.execute(sql, (id_input, course_id_input))
        if was_commited:
            print("Course Registration Committed")
        connection.commit()

    print("TUID: " + id_input, "and Your name is: " + name_input)


def sql_aa():
    id_input = id_box.get()
    name_input = name_box.get()
    course_id_input = course_id_box.get()
    id_box.delete(0, 100)
    name_box.delete(0, 100)
    course_id_box.delete(0, 100)
    with cursor:
        sql = "INSERT INTO Attendance (Student_ID, Course_ID) " \
              "VALUES (%s, %s)"
        was_commited = cursor.execute(sql, (id_input, course_id_input))
        if was_commited:
            print("Check-in Update Committed")
        connection.commit()


def sql_vr():
    id_input = id_box.get()
    id_box.delete(0, 100)
    name_box.delete(0, 100)
    course_id_box.delete(0, 100)
    with cursor:
        sql = "SELECT Student_name FROM Student WHERE Student_ID = %s "
        was_commited = cursor.execute(sql, id_input)
        if was_commited:
            print("Finding Name from Roster...")
            text = "This is the list of registration for: " + (cursor.fetchall()[0]['Student_name']) + """
            """
        sql = "SELECT * FROM ENROLLMENT WHERE Student_ID = %s "
        was_commited = cursor.execute(sql, id_input)
        if was_commited:
            print("Exporting All Registration...")
            output = cursor.fetchall()
            for row in output:
                text += """
                """ + "Course ID: " + row['Course_ID']
        connection.commit()
        text += """

                    --- End of the list --- """
    print(text)


def sql_dr():
    id_input = id_box.get()
    name_input = name_box.get()
    course_id_input = course_id_box.get()
    id_box.delete(0, 100)
    name_box.delete(0, 100)
    course_id_box.delete(0, 100)
    with cursor:
        sql = "DELETE FROM Enrollment WHERE Student_ID = %s"
        was_commited = cursor.execute(sql, id_input)
        if was_commited:
            print("Deletion Completed")
        connection.commit()


tcl_is_valid = root.register(is_valid)
id_tcl = tkinter.StringVar()  # Stores tkinter input to the variable
name_tcl = tkinter.StringVar()  # Same
course_id_tcl = tkinter.StringVar()  # Same for course id

# * This is where you will *CREATE* all labels and text boxes needed in GUI
# * NOT PLACING! PLACE ACCORDINGLY IN THE FUNCTION!
# Left Elements
# global label_name
label_name = tkinter.Label(frame_left, text='Full Name (e.g. John Doe)', anchor='e',
                           font=('Lucida Console', '18', ('bold', 'underline')), fg='white', bg='#9D2235')
label_id = tkinter.Label(frame_left, text='TUID', anchor='e',
                         font=('Lucida Console', '18', ('bold', 'underline')), fg='white', bg='#9D2235')
label_course_id = tkinter.Label(frame_left, text='Course ID', anchor='e',
                                font=('Lucida Console', '18', ('bold', 'underline')), fg='white', bg='#9D2235')

name_box = tkinter.Entry(frame_left, width=18, textvariable=name_tcl)  # Name field
id_box = tkinter.Entry(frame_left, width=18, validate='key',
                       vcmd=(tcl_is_valid, '%S'),
                       textvariable=id_tcl)  # TUID field only accepts alphanumeric
course_id_box = tkinter.Entry(frame_left, width=18, validate='key',
                              vcmd=(tcl_is_valid, '%S'), textvariable=course_id_tcl)  # Course ID as well

# Submit Buttons
button_submit_as = tkinter.Button(frame_left, text='Register', anchor='center', bg='white', command=sql_as)
button_submit_aa = tkinter.Button(frame_left, text='Check-in', anchor='center', bg='white', command=sql_aa)
button_submit_vr = tkinter.Button(frame_left, text='Export', anchor='center', bg='white', command=sql_vr)
button_submit_dr = tkinter.Button(frame_left, text='Delete', anchor='center', bg='white', command=sql_dr)

# * ----- BUTTONS ----- * #

#   Add Student Button
button_add_student = tkinter.Button(frame_right,
                                    text='Register to Courses', fg='black', command=add_student)
button_add_student.place(relx=0.13, rely=0.25, relwidth=0.8)

#   Check-in Button
button_attendance = tkinter.Button(frame_right,
                                   text="Check-in Today's class", fg='black', command=add_attendance)
button_attendance.place(relx=0.13, rely=0.32, relwidth=0.8)

#   View Record Button
button_view_records = tkinter.Button(frame_right,
                                     text='Check My Registration', fg='black', command=view_record)
button_view_records.place(relx=0.13, rely=0.39, relwidth=0.8)

#   Delete Button
button_delete = tkinter.Button(frame_right,
                               text='Clear My Registrations', fg='red', command=delete_record)
button_delete.place(relx=0.13, rely=0.53, relwidth=0.8)

#   Exit Button
button_clear = tkinter.Button(frame_right,
                              text='Exit', fg='black', command=root.quit)
button_clear.place(relx=0.13, rely=0.6, relwidth=0.8)

# End of element assignment of GUI
root.mainloop()
