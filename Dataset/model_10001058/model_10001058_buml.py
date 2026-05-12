####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
User = Class(name="User")
student = Class(name="student")
Student = Class(name="Student")
Courses = Class(name="Courses")
CourseCalendar = Class(name="CourseCalendar")
admin_Actor = Class(name="admin_Actor")
student_Actor = Class(name="student_Actor")
courseCalendar_Actor = Class(name="courseCalendar_Actor")
user_Actor = Class(name="user_Actor")
organisation_Actor = Class(name="organisation_Actor")
course_Actor = Class(name="course_Actor")
providedCourse___UseCase = Class(name="providedCourse___UseCase")
modifyCalender4_UseCase = Class(name="modifyCalender4_UseCase")
publishCalender___UseCase = Class(name="publishCalender___UseCase")
add_UseCase = Class(name="add_UseCase")
registerCourse_UseCase = Class(name="registerCourse_UseCase")
delete_UseCase = Class(name="delete_UseCase")
viewCourse_UseCase = Class(name="viewCourse_UseCase")
searchCourse_UseCase = Class(name="searchCourse_UseCase")
Teacher = Class(name="Teacher")
Student2 = Class(name="Student2")
Student3 = Class(name="Student3")
Student4 = Class(name="Student4")
teacher = Class(name="teacher")
timetable = Class(name="timetable")
Quiz = Class(name="Quiz")
Assignment = Class(name="Assignment")
Events = Class(name="Events")
attendance = Class(name="attendance")
result = Class(name="result")
chatbox = Class(name="chatbox")
dropbox = Class(name="dropbox")

# User class attributes and methods
User_id: Property = Property(name="id", type=IntegerType)
User_name: Property = Property(name="name", type=StringType)
User_address: Property = Property(name="address", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User_phnNo: Property = Property(name="phnNo", type=IntegerType)
User.attributes={User_email, User_name, User_phnNo, User_address, User_id}

# student class attributes and methods
student_managestudent: Property = Property(name="managestudent", type=StringType)
student_result: Property = Property(name="result", type=StringType)
student__attr: Property = Property(name="_attr", type=StringType)
student_attribute: Property = Property(name="attribute", type=StringType)
student__attr1: Property = Property(name="_attr1", type=StringType)
student_e: Property = Property(name="e", type=StringType)
student.attributes={student__attr1, student_managestudent, student_result, student_attribute, student_e, student__attr}

# Student class attributes and methods
Student_courseName: Property = Property(name="courseName", type=StringType)
Student_courseId: Property = Property(name="courseId", type=IntegerType)
Student.attributes={Student_courseName, Student_courseId}

# Courses class attributes and methods
Courses_courseName: Property = Property(name="courseName", type=StringType)
Courses_courseId: Property = Property(name="courseId", type=IntegerType)
Courses_coursecode: Property = Property(name="coursecode", type=IntegerType)
Courses_credithour: Property = Property(name="credithour", type=IntegerType)
Courses__attr: Property = Property(name="_attr", type=StringType)
Courses.attributes={Courses_courseId, Courses_courseName, Courses_credithour, Courses_coursecode, Courses__attr}

# CourseCalendar class attributes and methods
CourseCalendar_startTime: Property = Property(name="startTime", type=IntegerType)
CourseCalendar_endTime: Property = Property(name="endTime", type=IntegerType)
CourseCalendar.attributes={CourseCalendar_startTime, CourseCalendar_endTime}

# admin_Actor class attributes and methods

# student_Actor class attributes and methods

# courseCalendar_Actor class attributes and methods

# user_Actor class attributes and methods

# organisation_Actor class attributes and methods

# course_Actor class attributes and methods

# providedCourse___UseCase class attributes and methods

# modifyCalender4_UseCase class attributes and methods

# publishCalender___UseCase class attributes and methods

# add_UseCase class attributes and methods

# registerCourse_UseCase class attributes and methods

# delete_UseCase class attributes and methods

# viewCourse_UseCase class attributes and methods

# searchCourse_UseCase class attributes and methods

# Teacher class attributes and methods
Teacher_courseName: Property = Property(name="courseName", type=StringType)
Teacher_courseId: Property = Property(name="courseId", type=IntegerType)
Teacher.attributes={Teacher_courseName, Teacher_courseId}

# Student2 class attributes and methods
Student2_courseName: Property = Property(name="courseName", type=StringType)
Student2_courseId: Property = Property(name="courseId", type=IntegerType)
Student2.attributes={Student2_courseName, Student2_courseId}

# Student3 class attributes and methods
Student3_courseName: Property = Property(name="courseName", type=StringType)
Student3_courseId: Property = Property(name="courseId", type=IntegerType)
Student3.attributes={Student3_courseName, Student3_courseId}

# Student4 class attributes and methods
Student4_courseName: Property = Property(name="courseName", type=StringType)
Student4_courseId: Property = Property(name="courseId", type=IntegerType)
Student4.attributes={Student4_courseName, Student4_courseId}

# teacher class attributes and methods

# timetable class attributes and methods
timetable_courseName: Property = Property(name="courseName", type=StringType)
timetable_courseId: Property = Property(name="courseId", type=IntegerType)
timetable_coursecode: Property = Property(name="coursecode", type=IntegerType)
timetable_credithour: Property = Property(name="credithour", type=IntegerType)
timetable__attr: Property = Property(name="_attr", type=StringType)
timetable_lectime: Property = Property(name="lectime", type=IntegerType)
timetable_day: Property = Property(name="day", type=StringType)
timetable_date: Property = Property(name="date", type=IntegerType)
timetable_teacher: Property = Property(name="teacher", type=StringType)
timetable.attributes={timetable_credithour, timetable_date, timetable__attr, timetable_teacher, timetable_lectime, timetable_day, timetable_coursecode, timetable_courseName, timetable_courseId}

# Quiz class attributes and methods
Quiz_quiztitle: Property = Property(name="quiztitle", type=StringType)
Quiz_quizfile: Property = Property(name="quizfile", type=StringType)
Quiz_subject: Property = Property(name="subject", type=StringType)
Quiz_timeduration: Property = Property(name="timeduration", type=IntegerType)
Quiz__attr: Property = Property(name="_attr", type=StringType)
Quiz_scale: Property = Property(name="scale", type=IntegerType)
Quiz_date: Property = Property(name="date", type=IntegerType)
Quiz_department: Property = Property(name="department", type=StringType)
Quiz.attributes={Quiz__attr, Quiz_quiztitle, Quiz_date, Quiz_timeduration, Quiz_quizfile, Quiz_subject, Quiz_department, Quiz_scale}

# Assignment class attributes and methods
Assignment_assignmenttitle: Property = Property(name="assignmenttitle", type=StringType)
Assignment_assignmentfile: Property = Property(name="assignmentfile", type=StringType)
Assignment_duedate: Property = Property(name="duedate", type=IntegerType)
Assignment_class: Property = Property(name="class", type=IntegerType)
Assignment__attr: Property = Property(name="_attr", type=StringType)
Assignment__attr1: Property = Property(name="_attr1", type=IntegerType)
Assignment_program: Property = Property(name="program", type=StringType)
Assignment_department: Property = Property(name="department", type=StringType)
Assignment_session: Property = Property(name="session", type=IntegerType)
Assignment_section: Property = Property(name="section", type=StringType)
Assignment.attributes={Assignment__attr, Assignment_session, Assignment_section, Assignment_duedate, Assignment__attr1, Assignment_class, Assignment_department, Assignment_program, Assignment_assignmentfile, Assignment_assignmenttitle}

# Events class attributes and methods
Events_Evantname: Property = Property(name="Evantname", type=StringType)
Events_eventId: Property = Property(name="eventId", type=IntegerType)
Events_eventtitle: Property = Property(name="eventtitle", type=IntegerType)
Events_eventdescription: Property = Property(name="eventdescription", type=IntegerType)
Events__attr: Property = Property(name="_attr", type=StringType)
Events.attributes={Events_eventId, Events__attr, Events_Evantname, Events_eventdescription, Events_eventtitle}

# attendance class attributes and methods
attendance_class: Property = Property(name="class", type=StringType)
attendance_present: Property = Property(name="present", type=StringType)
attendance_absent: Property = Property(name="absent", type=StringType)
attendance_leave: Property = Property(name="leave", type=StringType)
attendance__attr: Property = Property(name="_attr", type=StringType)
attendance_lecture: Property = Property(name="lecture", type=IntegerType)
attendance_day: Property = Property(name="day", type=StringType)
attendance_date: Property = Property(name="date", type=IntegerType)
attendance_class1: Property = Property(name="class1", type=StringType)
attendance_attribute: Property = Property(name="attribute", type=StringType)
attendance.attributes={attendance_day, attendance_class1, attendance_date, attendance__attr, attendance_present, attendance_class, attendance_absent, attendance_leave, attendance_attribute, attendance_lecture}

# result class attributes and methods
result_class: Property = Property(name="class", type=StringType)
result_midmarks: Property = Property(name="midmarks", type=IntegerType)
result_finalmarks: Property = Property(name="finalmarks", type=IntegerType)
result_practical: Property = Property(name="practical", type=IntegerType)
result__attr: Property = Property(name="_attr", type=StringType)
result_sessional: Property = Property(name="sessional", type=IntegerType)
result_subject: Property = Property(name="subject", type=StringType)
result_totalmarks: Property = Property(name="totalmarks", type=IntegerType)
result_class1: Property = Property(name="class1", type=StringType)
result_attribute: Property = Property(name="attribute", type=StringType)
result_obtainedmarks: Property = Property(name="obtainedmarks", type=IntegerType)
result.attributes={result_sessional, result_obtainedmarks, result_attribute, result__attr, result_practical, result_class, result_totalmarks, result_class1, result_subject, result_finalmarks, result_midmarks}

# chatbox class attributes and methods
chatbox_class: Property = Property(name="class", type=StringType)
chatbox_messagetype: Property = Property(name="messagetype", type=IntegerType)
chatbox_messagetitle: Property = Property(name="messagetitle", type=StringType)
chatbox_messagedcription: Property = Property(name="messagedcription", type=IntegerType)
chatbox__attr: Property = Property(name="_attr", type=StringType)
chatbox.attributes={chatbox__attr, chatbox_class, chatbox_messagedcription, chatbox_messagetype, chatbox_messagetitle}

# dropbox class attributes and methods
dropbox_filetype: Property = Property(name="filetype", type=StringType)
dropbox_file: Property = Property(name="file", type=StringType)
dropbox_date: Property = Property(name="date", type=IntegerType)
dropbox_class: Property = Property(name="class", type=IntegerType)
dropbox__attr: Property = Property(name="_attr", type=StringType)
dropbox__attr1: Property = Property(name="_attr1", type=IntegerType)
dropbox_program: Property = Property(name="program", type=StringType)
dropbox_department: Property = Property(name="department", type=StringType)
dropbox_session: Property = Property(name="session", type=IntegerType)
dropbox_section: Property = Property(name="section", type=StringType)
dropbox.attributes={dropbox_session, dropbox__attr, dropbox_date, dropbox_program, dropbox_section, dropbox__attr1, dropbox_file, dropbox_class, dropbox_department, dropbox_filetype}

# Relationships
Teacher_dropbox: BinaryAssociation = BinaryAssociation(
    name="Teacher_dropbox",
    ends={
        Property(name="student23", type=student, multiplicity=Multiplicity(1, 9999)),
        Property(name="dropbox22", type=dropbox, multiplicity=Multiplicity(0, 9999))
    }
)
Admin_Courses: BinaryAssociation = BinaryAssociation(
    name="Admin_Courses",
    ends={
        Property(name="courses0", type=Courses, multiplicity=Multiplicity(1, 9999)),
        Property(name="student1", type=student, multiplicity=Multiplicity(1, 9999))
    }
)
Courses_Student: BinaryAssociation = BinaryAssociation(
    name="Courses_Student",
    ends={
        Property(name="student2", type=Student, multiplicity=Multiplicity(1, 9999)),
        Property(name="courses3", type=Courses, multiplicity=Multiplicity(1, 9999))
    }
)
Courses_CourseCalendar: BinaryAssociation = BinaryAssociation(
    name="Courses_CourseCalendar",
    ends={
        Property(name="courseCalendar4", type=CourseCalendar, multiplicity=Multiplicity(0, 1)),
        Property(name="courses5", type=Courses, multiplicity=Multiplicity(0, 1))
    }
)
teacher_Courses: BinaryAssociation = BinaryAssociation(
    name="teacher_Courses",
    ends={
        Property(name="teacher_Courses_06", type=Courses, multiplicity=Multiplicity(0, 1)),
        Property(name="teacher7", type=teacher, multiplicity=Multiplicity(1, 9999))
    }
)
timetable_Admin: BinaryAssociation = BinaryAssociation(
    name="timetable_Admin",
    ends={
        Property(name="student8", type=student, multiplicity=Multiplicity(1, 9999)),
        Property(name="timetable9", type=timetable, multiplicity=Multiplicity(1, 9999))
    }
)
Teacher_User: BinaryAssociation = BinaryAssociation(
    name="Teacher_User",
    ends={
        Property(name="student10", type=student, multiplicity=Multiplicity(1, 9999)),
        Property(name="quiz11", type=Quiz, multiplicity=Multiplicity(1, 9999))
    }
)
Admin_student: BinaryAssociation = BinaryAssociation(
    name="Admin_student",
    ends={
        Property(name="assignment12", type=Assignment, multiplicity=Multiplicity(1, 9999)),
        Property(name="student13", type=student, multiplicity=Multiplicity(1, 9999))
    }
)
Admin_Events: BinaryAssociation = BinaryAssociation(
    name="Admin_Events",
    ends={
        Property(name="events14", type=Events, multiplicity=Multiplicity(1, 9999)),
        Property(name="student15", type=student, multiplicity=Multiplicity(1, 9999))
    }
)
Teacher_attendance: BinaryAssociation = BinaryAssociation(
    name="Teacher_attendance",
    ends={
        Property(name="attendance16", type=attendance, multiplicity=Multiplicity(1, 9999)),
        Property(name="Teacher_attendance_117", type=student, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_result: BinaryAssociation = BinaryAssociation(
    name="Teacher_result",
    ends={
        Property(name="result18", type=result, multiplicity=Multiplicity(1, 9999)),
        Property(name="teacher19", type=student, multiplicity=Multiplicity(0, 1))
    }
)
Teacher_chatbox: BinaryAssociation = BinaryAssociation(
    name="Teacher_chatbox",
    ends={
        Property(name="chatbox20", type=chatbox, multiplicity=Multiplicity(0, 9999)),
        Property(name="teacher21", type=student, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_80ecdd81_e4ce_4e87_adfe_4cc32fda6609",
    types={User, student, Student, Courses, CourseCalendar, admin_Actor, student_Actor, courseCalendar_Actor, user_Actor, organisation_Actor, course_Actor, providedCourse___UseCase, modifyCalender4_UseCase, publishCalender___UseCase, add_UseCase, registerCourse_UseCase, delete_UseCase, viewCourse_UseCase, searchCourse_UseCase, Teacher, Student2, Student3, Student4, teacher, timetable, Quiz, Assignment, Events, attendance, result, chatbox, dropbox},
    associations={Teacher_dropbox, Admin_Courses, Courses_Student, Courses_CourseCalendar, teacher_Courses, timetable_Admin, Teacher_User, Admin_student, Admin_Events, Teacher_attendance, Teacher_result, Teacher_chatbox},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)