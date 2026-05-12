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
Employee_Actor = Class(name="Employee_Actor")
Supervisor_Actor = Class(name="Supervisor_Actor")
_Component = Class(name="_Component")
admin_Actor = Class(name="admin_Actor")
FACULTY = Class(name="FACULTY")
STUDENT = Class(name="STUDENT")
PARENT = Class(name="PARENT")
ADMIN = Class(name="ADMIN")
take_attendance_call_external = Class(name="take_attendance_call_external")
generate_attendance_report_external = Class(name="generate_attendance_report_external")
post_attendance_external = Class(name="post_attendance_external")
answer_attendance_call_external = Class(name="answer_attendance_call_external")
view_cumiliative_attendance_external = Class(name="view_cumiliative_attendance_external")
login_external = Class(name="login_external")
logout_external = Class(name="logout_external")
send_attendance_sms_external = Class(name="send_attendance_sms_external")
modify_list_of_students_external = Class(name="modify_list_of_students_external")

# Employee_Actor class attributes and methods

# Supervisor_Actor class attributes and methods

# _Component class attributes and methods

# admin_Actor class attributes and methods

# FACULTY class attributes and methods
FACULTY_id: Property = Property(name="id", type=StringType)
FACULTY_password: Property = Property(name="password", type=StringType)
FACULTY.attributes={FACULTY_password, FACULTY_id}

# STUDENT class attributes and methods
STUDENT_id: Property = Property(name="id", type=StringType)
STUDENT_password: Property = Property(name="password", type=StringType)
STUDENT.attributes={STUDENT_password, STUDENT_id}

# PARENT class attributes and methods
PARENT_id: Property = Property(name="id", type=StringType)
PARENT_password: Property = Property(name="password", type=StringType)
PARENT_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
PARENT.attributes={PARENT_id, PARENT_phoneNumber, PARENT_password}

# ADMIN class attributes and methods
ADMIN_id: Property = Property(name="id", type=StringType)
ADMIN_password: Property = Property(name="password", type=StringType)
ADMIN.attributes={ADMIN_password, ADMIN_id}

# take_attendance_call_external class attributes and methods

# generate_attendance_report_external class attributes and methods

# post_attendance_external class attributes and methods

# answer_attendance_call_external class attributes and methods

# view_cumiliative_attendance_external class attributes and methods

# login_external class attributes and methods

# logout_external class attributes and methods

# send_attendance_sms_external class attributes and methods

# modify_list_of_students_external class attributes and methods

# Relationships
FACULTY_STUDENT: BinaryAssociation = BinaryAssociation(
    name="FACULTY_STUDENT",
    ends={
        Property(name="sTUDENT28", type=STUDENT, multiplicity=Multiplicity(1, 9999)),
        Property(name="fACULTY29", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)
FACULTY_ADMIN: BinaryAssociation = BinaryAssociation(
    name="FACULTY_ADMIN",
    ends={
        Property(name="aDMIN30", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="fACULTY31", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)
STUDENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="STUDENT_ADMIN",
    ends={
        Property(name="aDMIN32", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="sTUDENT33", type=STUDENT, multiplicity=Multiplicity(1, 9999))
    }
)
PARENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="PARENT_ADMIN",
    ends={
        Property(name="aDMIN34", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="pARENT35", type=PARENT, multiplicity=Multiplicity(1, 9999))
    }
)
faculty_give_attendance: BinaryAssociation = BinaryAssociation(
    name="faculty_give_attendance",
    ends={
        Property(name="give_attendance0", type=take_attendance_call_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty1", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_generate_class_wise_attendance_report: BinaryAssociation = BinaryAssociation(
    name="faculty_generate_class_wise_attendance_report",
    ends={
        Property(name="generate_class_wise_attendance_report2", type=generate_attendance_report_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty3", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_post_attendance: BinaryAssociation = BinaryAssociation(
    name="faculty_post_attendance",
    ends={
        Property(name="post_attendance4", type=post_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty5", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_answer_attendance_call: BinaryAssociation = BinaryAssociation(
    name="student_answer_attendance_call",
    ends={
        Property(name="answer_attendance_call6", type=answer_attendance_call_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student7", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_view_cumiliative_attendance: BinaryAssociation = BinaryAssociation(
    name="student_view_cumiliative_attendance",
    ends={
        Property(name="view_cumiliative_attendance8", type=view_cumiliative_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student9", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_login: BinaryAssociation = BinaryAssociation(
    name="student_login",
    ends={
        Property(name="login10", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student11", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_logout: BinaryAssociation = BinaryAssociation(
    name="student_logout",
    ends={
        Property(name="logout12", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student13", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_login: BinaryAssociation = BinaryAssociation(
    name="faculty_login",
    ends={
        Property(name="login14", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty15", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_logout: BinaryAssociation = BinaryAssociation(
    name="faculty_logout",
    ends={
        Property(name="logout16", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty17", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_login: BinaryAssociation = BinaryAssociation(
    name="admin_login",
    ends={
        Property(name="login18", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin19", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_logout: BinaryAssociation = BinaryAssociation(
    name="admin_logout",
    ends={
        Property(name="logout20", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin21", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_send_attendance_sms: BinaryAssociation = BinaryAssociation(
    name="faculty_send_attendance_sms",
    ends={
        Property(name="send_attendance_sms22", type=send_attendance_sms_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty23", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
faculty_view_cumiliative_attendance: BinaryAssociation = BinaryAssociation(
    name="faculty_view_cumiliative_attendance",
    ends={
        Property(name="view_cumiliative_attendance24", type=view_cumiliative_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="faculty25", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_modify_list_of_students: BinaryAssociation = BinaryAssociation(
    name="admin_modify_list_of_students",
    ends={
        Property(name="modify_list_of_students26", type=modify_list_of_students_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin27", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a15043e5_0085_4bcf_8051_71ec86153795",
    types={Employee_Actor, Supervisor_Actor, _Component, admin_Actor, FACULTY, STUDENT, PARENT, ADMIN, take_attendance_call_external, generate_attendance_report_external, post_attendance_external, answer_attendance_call_external, view_cumiliative_attendance_external, login_external, logout_external, send_attendance_sms_external, modify_list_of_students_external},
    associations={FACULTY_STUDENT, FACULTY_ADMIN, STUDENT_ADMIN, PARENT_ADMIN, faculty_give_attendance, faculty_generate_class_wise_attendance_report, faculty_post_attendance, student_answer_attendance_call, student_view_cumiliative_attendance, student_login, student_logout, faculty_login, faculty_logout, admin_login, admin_logout, faculty_send_attendance_sms, faculty_view_cumiliative_attendance, admin_modify_list_of_students},
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