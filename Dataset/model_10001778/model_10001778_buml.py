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
student_Actor = Class(name="student_Actor")
Teachers_Actor = Class(name="Teachers_Actor")
Student_Attendance_at_INU_Component = Class(name="Student_Attendance_at_INU_Component")
parent_Actor = Class(name="parent_Actor")
admin_technician_Actor = Class(name="admin_technician_Actor")
FACULTY = Class(name="FACULTY")
STUDENT = Class(name="STUDENT")
PARENT = Class(name="PARENT")
ADMIN = Class(name="ADMIN")
call_students_for_attendance_external = Class(name="call_students_for_attendance_external")
generate_class_wise_attendance_report_external = Class(name="generate_class_wise_attendance_report_external")
post_attendance_external = Class(name="post_attendance_external")
answer_attendance_call_external = Class(name="answer_attendance_call_external")
view_subject_wise_attendance_external = Class(name="view_subject_wise_attendance_external")
view_cumiliative_attendance_external = Class(name="view_cumiliative_attendance_external")
login_external = Class(name="login_external")
logout_external = Class(name="logout_external")
send_attendance_sms_external = Class(name="send_attendance_sms_external")
recieve_attendance_sms_external = Class(name="recieve_attendance_sms_external")
modify_list_of_students_external = Class(name="modify_list_of_students_external")

# student_Actor class attributes and methods

# Teachers_Actor class attributes and methods

# Student_Attendance_at_INU_Component class attributes and methods

# parent_Actor class attributes and methods

# admin_technician_Actor class attributes and methods

# FACULTY class attributes and methods
FACULTY_id: Property = Property(name="id", type=StringType)
FACULTY_password: Property = Property(name="password", type=StringType)
FACULTY.attributes={FACULTY_id, FACULTY_password}

# STUDENT class attributes and methods
STUDENT_id: Property = Property(name="id", type=StringType)
STUDENT_password: Property = Property(name="password", type=StringType)
STUDENT.attributes={STUDENT_password, STUDENT_id}

# PARENT class attributes and methods
PARENT_id: Property = Property(name="id", type=StringType)
PARENT_password: Property = Property(name="password", type=StringType)
PARENT_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
PARENT.attributes={PARENT_phoneNumber, PARENT_password, PARENT_id}

# ADMIN class attributes and methods
ADMIN_id: Property = Property(name="id", type=StringType)
ADMIN_password: Property = Property(name="password", type=StringType)
ADMIN.attributes={ADMIN_password, ADMIN_id}

# call_students_for_attendance_external class attributes and methods

# generate_class_wise_attendance_report_external class attributes and methods

# post_attendance_external class attributes and methods

# answer_attendance_call_external class attributes and methods

# view_subject_wise_attendance_external class attributes and methods

# view_cumiliative_attendance_external class attributes and methods

# login_external class attributes and methods

# logout_external class attributes and methods

# send_attendance_sms_external class attributes and methods

# recieve_attendance_sms_external class attributes and methods

# modify_list_of_students_external class attributes and methods

# Relationships
faculty_give_attendance: BinaryAssociation = BinaryAssociation(
    name="faculty_give_attendance",
    ends={
        Property(name="give_attendance0", type=call_students_for_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty1", type=Teachers_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_generate_class_wise_attendance_report: BinaryAssociation = BinaryAssociation(
    name="faculty_generate_class_wise_attendance_report",
    ends={
        Property(name="generate_class_wise_attendance_report2", type=generate_class_wise_attendance_report_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty3", type=Teachers_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_post_attendance: BinaryAssociation = BinaryAssociation(
    name="faculty_post_attendance",
    ends={
        Property(name="post_attendance4", type=post_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty5", type=Teachers_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_answer_attendance_call: BinaryAssociation = BinaryAssociation(
    name="student_answer_attendance_call",
    ends={
        Property(name="answer_attendance_call6", type=answer_attendance_call_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student7", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_view_subject_wise_attendance: BinaryAssociation = BinaryAssociation(
    name="student_view_subject_wise_attendance",
    ends={
        Property(name="view_subject_wise_attendance8", type=view_subject_wise_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student9", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_view_cumiliative_attendance: BinaryAssociation = BinaryAssociation(
    name="student_view_cumiliative_attendance",
    ends={
        Property(name="view_cumiliative_attendance10", type=view_cumiliative_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student11", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_login: BinaryAssociation = BinaryAssociation(
    name="student_login",
    ends={
        Property(name="login12", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student13", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_logout: BinaryAssociation = BinaryAssociation(
    name="student_logout",
    ends={
        Property(name="logout14", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student15", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_login: BinaryAssociation = BinaryAssociation(
    name="faculty_login",
    ends={
        Property(name="login16", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty17", type=Teachers_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_logout: BinaryAssociation = BinaryAssociation(
    name="faculty_logout",
    ends={
        Property(name="logout18", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty19", type=Teachers_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_login: BinaryAssociation = BinaryAssociation(
    name="admin_login",
    ends={
        Property(name="login20", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin21", type=admin_technician_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_logout: BinaryAssociation = BinaryAssociation(
    name="admin_logout",
    ends={
        Property(name="logout22", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin23", type=admin_technician_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_send_attendance_sms: BinaryAssociation = BinaryAssociation(
    name="faculty_send_attendance_sms",
    ends={
        Property(name="send_attendance_sms24", type=send_attendance_sms_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty25", type=Teachers_Actor, multiplicity=Multiplicity(0, 1))
    }
)
parent_recieve_attendance_sms: BinaryAssociation = BinaryAssociation(
    name="parent_recieve_attendance_sms",
    ends={
        Property(name="recieve_attendance_sms26", type=recieve_attendance_sms_external, multiplicity=Multiplicity(0, 1)),
        Property(name="parent27", type=parent_Actor, multiplicity=Multiplicity(0, 1))
    }
)
STUDENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="STUDENT_ADMIN",
    ends={
        Property(name="aDMIN38", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="sTUDENT39", type=STUDENT, multiplicity=Multiplicity(1, 9999))
    }
)
PARENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="PARENT_ADMIN",
    ends={
        Property(name="aDMIN40", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="pARENT41", type=PARENT, multiplicity=Multiplicity(1, 9999))
    }
)
faculty_view_cumiliative_attendance: BinaryAssociation = BinaryAssociation(
    name="faculty_view_cumiliative_attendance",
    ends={
        Property(name="view_cumiliative_attendance28", type=view_cumiliative_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty29", type=Teachers_Actor, multiplicity=Multiplicity(0, 1))
    }
)
parent_logout: BinaryAssociation = BinaryAssociation(
    name="parent_logout",
    ends={
        Property(name="logout30", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="parent31", type=parent_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_modify_list_of_students: BinaryAssociation = BinaryAssociation(
    name="admin_modify_list_of_students",
    ends={
        Property(name="modify_list_of_students32", type=modify_list_of_students_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin33", type=admin_technician_Actor, multiplicity=Multiplicity(0, 1))
    }
)
FACULTY_STUDENT: BinaryAssociation = BinaryAssociation(
    name="FACULTY_STUDENT",
    ends={
        Property(name="sTUDENT34", type=STUDENT, multiplicity=Multiplicity(1, 9999)),
        Property(name="fACULTY35", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)
FACULTY_ADMIN: BinaryAssociation = BinaryAssociation(
    name="FACULTY_ADMIN",
    ends={
        Property(name="aDMIN36", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="fACULTY37", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_V0MeAIL7EeqWAK1R3DAmBw",
    types={student_Actor, Teachers_Actor, Student_Attendance_at_INU_Component, parent_Actor, admin_technician_Actor, FACULTY, STUDENT, PARENT, ADMIN, call_students_for_attendance_external, generate_class_wise_attendance_report_external, post_attendance_external, answer_attendance_call_external, view_subject_wise_attendance_external, view_cumiliative_attendance_external, login_external, logout_external, send_attendance_sms_external, recieve_attendance_sms_external, modify_list_of_students_external},
    associations={faculty_give_attendance, faculty_generate_class_wise_attendance_report, faculty_post_attendance, student_answer_attendance_call, student_view_subject_wise_attendance, student_view_cumiliative_attendance, student_login, student_logout, faculty_login, faculty_logout, admin_login, admin_logout, faculty_send_attendance_sms, parent_recieve_attendance_sms, STUDENT_ADMIN, PARENT_ADMIN, faculty_view_cumiliative_attendance, parent_logout, admin_modify_list_of_students, FACULTY_STUDENT, FACULTY_ADMIN},
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