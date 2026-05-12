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
faculty_Actor = Class(name="faculty_Actor")
_Component = Class(name="_Component")
admin_Actor = Class(name="admin_Actor")
FACULTY = Class(name="FACULTY")
STUDENT = Class(name="STUDENT")
PARENT = Class(name="PARENT")
ADMIN = Class(name="ADMIN")
take_attendance_call_external = Class(name="take_attendance_call_external")
generate_class_wise_attendance_report_external = Class(name="generate_class_wise_attendance_report_external")
post_attendance_external = Class(name="post_attendance_external")
answer_attendance_call_external = Class(name="answer_attendance_call_external")
login_external = Class(name="login_external")
logout_external = Class(name="logout_external")
send_attendance_sms_external = Class(name="send_attendance_sms_external")
view_cumiliative_attendance_external = Class(name="view_cumiliative_attendance_external")
modify_list_of_students_external = Class(name="modify_list_of_students_external")

# student_Actor class attributes and methods

# faculty_Actor class attributes and methods

# _Component class attributes and methods

# admin_Actor class attributes and methods

# FACULTY class attributes and methods
FACULTY_id: Property = Property(name="id", type=StringType)
FACULTY_password: Property = Property(name="password", type=StringType)
FACULTY.attributes={FACULTY_password, FACULTY_id}

# STUDENT class attributes and methods
STUDENT_id: Property = Property(name="id", type=StringType)
STUDENT_password: Property = Property(name="password", type=StringType)
STUDENT.attributes={STUDENT_id, STUDENT_password}

# PARENT class attributes and methods
PARENT_id: Property = Property(name="id", type=StringType)
PARENT_password: Property = Property(name="password", type=StringType)
PARENT_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
PARENT.attributes={PARENT_id, PARENT_password, PARENT_phoneNumber}

# ADMIN class attributes and methods
ADMIN_id: Property = Property(name="id", type=StringType)
ADMIN_password: Property = Property(name="password", type=StringType)
ADMIN.attributes={ADMIN_password, ADMIN_id}

# take_attendance_call_external class attributes and methods

# generate_class_wise_attendance_report_external class attributes and methods

# post_attendance_external class attributes and methods

# answer_attendance_call_external class attributes and methods

# login_external class attributes and methods

# logout_external class attributes and methods

# send_attendance_sms_external class attributes and methods

# view_cumiliative_attendance_external class attributes and methods

# modify_list_of_students_external class attributes and methods

# Relationships
STUDENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="STUDENT_ADMIN",
    ends={
        Property(name="sTUDENT27", type=STUDENT, multiplicity=Multiplicity(1, 9999)),
        Property(name="aDMIN26", type=ADMIN, multiplicity=Multiplicity(1, 1))
    }
)
PARENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="PARENT_ADMIN",
    ends={
        Property(name="aDMIN28", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="pARENT29", type=PARENT, multiplicity=Multiplicity(1, 9999))
    }
)
faculty_give_attendance: BinaryAssociation = BinaryAssociation(
    name="faculty_give_attendance",
    ends={
        Property(name="give_attendance0", type=take_attendance_call_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty1", type=faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_generate_class_wise_attendance_report: BinaryAssociation = BinaryAssociation(
    name="faculty_generate_class_wise_attendance_report",
    ends={
        Property(name="generate_class_wise_attendance_report2", type=generate_class_wise_attendance_report_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty3", type=faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_post_attendance: BinaryAssociation = BinaryAssociation(
    name="faculty_post_attendance",
    ends={
        Property(name="post_attendance4", type=post_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty5", type=faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_answer_attendance_call: BinaryAssociation = BinaryAssociation(
    name="student_answer_attendance_call",
    ends={
        Property(name="answer_attendance_call6", type=answer_attendance_call_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student7", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_login: BinaryAssociation = BinaryAssociation(
    name="faculty_login",
    ends={
        Property(name="login8", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty9", type=faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_logout: BinaryAssociation = BinaryAssociation(
    name="faculty_logout",
    ends={
        Property(name="logout10", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty11", type=faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_login: BinaryAssociation = BinaryAssociation(
    name="admin_login",
    ends={
        Property(name="login12", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin13", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_logout: BinaryAssociation = BinaryAssociation(
    name="admin_logout",
    ends={
        Property(name="logout14", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_send_attendance_sms: BinaryAssociation = BinaryAssociation(
    name="faculty_send_attendance_sms",
    ends={
        Property(name="send_attendance_sms16", type=send_attendance_sms_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty17", type=faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_view_cumiliative_attendance: BinaryAssociation = BinaryAssociation(
    name="faculty_view_cumiliative_attendance",
    ends={
        Property(name="view_cumiliative_attendance18", type=view_cumiliative_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty19", type=faculty_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_modify_list_of_students: BinaryAssociation = BinaryAssociation(
    name="admin_modify_list_of_students",
    ends={
        Property(name="modify_list_of_students20", type=modify_list_of_students_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin21", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
FACULTY_STUDENT: BinaryAssociation = BinaryAssociation(
    name="FACULTY_STUDENT",
    ends={
        Property(name="sTUDENT22", type=STUDENT, multiplicity=Multiplicity(1, 9999)),
        Property(name="fACULTY23", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)
FACULTY_ADMIN: BinaryAssociation = BinaryAssociation(
    name="FACULTY_ADMIN",
    ends={
        Property(name="aDMIN24", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="fACULTY25", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7c6a47a4_e566_4ebc_8c70_21b8056b962e",
    types={student_Actor, faculty_Actor, _Component, admin_Actor, FACULTY, STUDENT, PARENT, ADMIN, take_attendance_call_external, generate_class_wise_attendance_report_external, post_attendance_external, answer_attendance_call_external, login_external, logout_external, send_attendance_sms_external, view_cumiliative_attendance_external, modify_list_of_students_external},
    associations={STUDENT_ADMIN, PARENT_ADMIN, faculty_give_attendance, faculty_generate_class_wise_attendance_report, faculty_post_attendance, student_answer_attendance_call, faculty_login, faculty_logout, admin_login, admin_logout, faculty_send_attendance_sms, faculty_view_cumiliative_attendance, admin_modify_list_of_students, FACULTY_STUDENT, FACULTY_ADMIN},
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