import tkinter
from tkinter import messagebox
import pymysql as pymy

# This package is for CIS 2109 Group Project.
# Refer to StudentManagement.jpg
# for the database design that is assumed on this project.


# Start of element assignment of GUI
root = tkinter.Tk()

root.title("TUJ Student Repository")
root.geometry('1024x768')
global frame_left, frame_right
frame_left = tkinter.Frame(root, bg='#9D2235', width="724", height="768") # Temple Color
frame_right = tkinter.Frame(root, bg='gray', width="300", height="768")
frame_right.pack(side="right")
frame_left.pack(side="left")


global text # global text for label
text = 'This is text variable'
label_head = tkinter.Label(frame_left, text=text,
                           font=('Lucida Console', '25', 'bold'), justify='center', fg='white', bg='maroon',
                           anchor='center')  # Not placed, just declared!


# TU Logo
tu_image = tkinter.PhotoImage(file='temple-logo-t-box.png')
disp_image = tkinter.Label(frame_left, image=tu_image)
disp_image.place(anchor="n", x=362, y=0)
# Welcome message
welcome = tkinter.Label(frame_left, text='Welcome to TUJ Student Repository',
                        justify='center', fg='white', bg='black',
                        anchor='center', font=("Lucida Console", "20", "bold"))
welcome.place(anchor='n', x=362, rely=0.16)

# ----- FUNCTIONS FOR EACH BUTTONS -----

# frame_left.place_forget is the process of cleaning left part.
# common_parts() reassigns the common parts.


def common_parts():
    # frame_left = tkinter.Frame(root, bg='#9D2235', width="724", height="768")  # Temple Color
    # frame_right = tkinter.Frame(root, bg='gray', width="300", height="768")
    # frame_right.pack(side="right")
    # frame_left.pack(side="left")

    # TU Logo
    tu_image = tkinter.PhotoImage(file='temple-logo-t-box.png')
    disp_image = tkinter.Label(frame_left, image=tu_image)
    disp_image.place(anchor="n", x=362, y=1)


def add_student():
    for widget in frame_left.winfo_children():
        widget.place_forget()
    # clear_left_frame()
    common_parts()
    text = 'This is add_student function'
    label_head.config(text=text)
    label_head.place(anchor='n', x=362, rely=0.20)

    # Depreciated
    # label_as = tkinter.Label(frame_left, text='ADD Student', font=('Lucida Console', '25', 'bold'))
    # label_as.place(x=300, y=362)


def add_attendance():
    for widget in frame_left.winfo_children():
        widget.place_forget()
    text = "Please check-in to today's class"
    label_head.config(text=text)
    label_head.place(anchor='n', x=362, rely=0.20)
    common_parts()
    # Depreciated
    # label_aa = tkinter.Label(frame_left, text='Check-in', font=('Lucida Console', '10', 'bold'))
    # label_aa.place(x=300, y=362)


def view_record():
    for widget in frame_left.winfo_children():
        widget.place_forget()
    common_parts()
    text = "This is view_record function"
    label_head.config(text=text)
    label_head.place(anchor='n', x=362, rely=0.20)
    label_name.place(relx=0.8, rely=0.5, anchor='center')

    # Depreciated
    # label_vr = tkinter.Label(frame_left, text='View', font=('Lucida Console', '15', 'bold'))
    # label_vr.place(x=300, y=362)


def update_record():
    for widget in frame_left.winfo_children():
        widget.place_forget()
    common_parts()
    text = 'This is update_record function'
    label_head.config(text=text)
    label_head.place(anchor='n', x=362, rely=0.20)

    # Depreciated
    # label_ur = tkinter.Label(frame_left, text='Update', font=('Lucida Console', '30', 'bold'))
    # label_ur.place(x=300, y=362)


def delete_record():
    for widget in frame_left.winfo_children():
        widget.place_forget()
    common_parts()
    text = 'This is delete_record function'
    label_head.config(text=text)
    label_head.place(anchor='n', x=362, rely=0.20)

    # Depreciated
    # label_dr = tkinter.Label(frame_left, text='Delete', font=('Lucida Console', '5', 'bold'))
    # label_dr.place(x=300, y=362)


# Making all the labels in GUI (NOT PLACING!)
# Left Elements
# global label_name
label_name = tkinter.Label(frame_left, text='Full Name ("John Doe")')
label_id = tkinter.Label(frame_left, text='TUID')


# ----- BUTTONS -----

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

#   Update Record Button
button_update_records = tkinter.Button(frame_right,
                                       text='Update My Registration', fg='black', command=update_record)
button_update_records.place(relx=0.13, rely=0.46, relwidth=0.8)

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

