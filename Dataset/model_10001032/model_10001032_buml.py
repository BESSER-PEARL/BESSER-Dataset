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
logout_external = Class(name="logout_external")
student_Actor = Class(name="student_Actor")
_Component = Class(name="_Component")
admin_Actor = Class(name="admin_Actor")
FACULTY = Class(name="FACULTY")
STUDENT = Class(name="STUDENT")
PARENT = Class(name="PARENT")
ADMIN = Class(name="ADMIN")
student_login_external = Class(name="student_login_external")
view_student_external = Class(name="view_student_external")
add_student_external = Class(name="add_student_external")
check_attendance_external = Class(name="check_attendance_external")

# logout_external class attributes and methods

# student_Actor class attributes and methods

# _Component class attributes and methods

# admin_Actor class attributes and methods

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
PARENT.attributes={PARENT_id, PARENT_password, PARENT_phoneNumber}

# ADMIN class attributes and methods
ADMIN_id: Property = Property(name="id", type=StringType)
ADMIN_password: Property = Property(name="password", type=StringType)
ADMIN.attributes={ADMIN_password, ADMIN_id}

# student_login_external class attributes and methods

# view_student_external class attributes and methods

# add_student_external class attributes and methods

# check_attendance_external class attributes and methods

# Relationships
student_login: BinaryAssociation = BinaryAssociation(
    name="student_login",
    ends={
        Property(name="login6", type=check_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student7", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_logout: BinaryAssociation = BinaryAssociation(
    name="student_logout",
    ends={
        Property(name="logout8", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student9", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_login: BinaryAssociation = BinaryAssociation(
    name="admin_login",
    ends={
        Property(name="login10", type=check_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin11", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_logout: BinaryAssociation = BinaryAssociation(
    name="admin_logout",
    ends={
        Property(name="logout12", type=logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin13", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
FACULTY_STUDENT: BinaryAssociation = BinaryAssociation(
    name="FACULTY_STUDENT",
    ends={
        Property(name="sTUDENT14", type=STUDENT, multiplicity=Multiplicity(1, 9999)),
        Property(name="fACULTY15", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)
FACULTY_ADMIN: BinaryAssociation = BinaryAssociation(
    name="FACULTY_ADMIN",
    ends={
        Property(name="aDMIN16", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="fACULTY17", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)
STUDENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="STUDENT_ADMIN",
    ends={
        Property(name="aDMIN18", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="sTUDENT19", type=STUDENT, multiplicity=Multiplicity(1, 9999))
    }
)
PARENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="PARENT_ADMIN",
    ends={
        Property(name="aDMIN20", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="pARENT21", type=PARENT, multiplicity=Multiplicity(1, 9999))
    }
)
student_answer_attendance_call: BinaryAssociation = BinaryAssociation(
    name="student_answer_attendance_call",
    ends={
        Property(name="answer_attendance_call0", type=student_login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student1", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_view_subject_wise_attendance: BinaryAssociation = BinaryAssociation(
    name="student_view_subject_wise_attendance",
    ends={
        Property(name="view_subject_wise_attendance2", type=view_student_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student3", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_view_cumiliative_attendance: BinaryAssociation = BinaryAssociation(
    name="student_view_cumiliative_attendance",
    ends={
        Property(name="view_cumiliative_attendance4", type=add_student_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student5", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7cfd81e2_bcb4_4a92_a5f6_d42d6e55d0f9",
    types={logout_external, student_Actor, _Component, admin_Actor, FACULTY, STUDENT, PARENT, ADMIN, student_login_external, view_student_external, add_student_external, check_attendance_external},
    associations={student_login, student_logout, admin_login, admin_logout, FACULTY_STUDENT, FACULTY_ADMIN, STUDENT_ADMIN, PARENT_ADMIN, student_answer_attendance_call, student_view_subject_wise_attendance, student_view_cumiliative_attendance},
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