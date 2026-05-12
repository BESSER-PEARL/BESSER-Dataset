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
_Component = Class(name="_Component")
admin_Actor = Class(name="admin_Actor")
FACULTY = Class(name="FACULTY")
STUDENT = Class(name="STUDENT")
PARENT = Class(name="PARENT")
ADMIN = Class(name="ADMIN")
view_subject_wise_attendance_external = Class(name="view_subject_wise_attendance_external")
view_cumiliative_attendance_external = Class(name="view_cumiliative_attendance_external")
login_external = Class(name="login_external")
modify_list_of_students_external = Class(name="modify_list_of_students_external")

# student_Actor class attributes and methods

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
PARENT.attributes={PARENT_password, PARENT_phoneNumber, PARENT_id}

# ADMIN class attributes and methods
ADMIN_id: Property = Property(name="id", type=StringType)
ADMIN_password: Property = Property(name="password", type=StringType)
ADMIN.attributes={ADMIN_password, ADMIN_id}

# view_subject_wise_attendance_external class attributes and methods

# view_cumiliative_attendance_external class attributes and methods

# login_external class attributes and methods

# modify_list_of_students_external class attributes and methods

# Relationships
student_view_subject_wise_attendance: BinaryAssociation = BinaryAssociation(
    name="student_view_subject_wise_attendance",
    ends={
        Property(name="view_subject_wise_attendance0", type=view_subject_wise_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student1", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_view_cumiliative_attendance: BinaryAssociation = BinaryAssociation(
    name="student_view_cumiliative_attendance",
    ends={
        Property(name="view_cumiliative_attendance2", type=view_cumiliative_attendance_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student3", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
student_login: BinaryAssociation = BinaryAssociation(
    name="student_login",
    ends={
        Property(name="login4", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="student5", type=student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_login: BinaryAssociation = BinaryAssociation(
    name="admin_login",
    ends={
        Property(name="login6", type=login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin7", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_modify_list_of_students: BinaryAssociation = BinaryAssociation(
    name="admin_modify_list_of_students",
    ends={
        Property(name="modify_list_of_students8", type=modify_list_of_students_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin9", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
FACULTY_STUDENT: BinaryAssociation = BinaryAssociation(
    name="FACULTY_STUDENT",
    ends={
        Property(name="sTUDENT10", type=STUDENT, multiplicity=Multiplicity(1, 9999)),
        Property(name="fACULTY11", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)
FACULTY_ADMIN: BinaryAssociation = BinaryAssociation(
    name="FACULTY_ADMIN",
    ends={
        Property(name="aDMIN12", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="fACULTY13", type=FACULTY, multiplicity=Multiplicity(1, 9999))
    }
)
STUDENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="STUDENT_ADMIN",
    ends={
        Property(name="aDMIN14", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="sTUDENT15", type=STUDENT, multiplicity=Multiplicity(1, 9999))
    }
)
PARENT_ADMIN: BinaryAssociation = BinaryAssociation(
    name="PARENT_ADMIN",
    ends={
        Property(name="aDMIN16", type=ADMIN, multiplicity=Multiplicity(1, 1)),
        Property(name="pARENT17", type=PARENT, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b8ce60fe_470e_42e2_b893_fa925435240d",
    types={student_Actor, _Component, admin_Actor, FACULTY, STUDENT, PARENT, ADMIN, view_subject_wise_attendance_external, view_cumiliative_attendance_external, login_external, modify_list_of_students_external},
    associations={student_view_subject_wise_attendance, student_view_cumiliative_attendance, student_login, admin_login, admin_modify_list_of_students, FACULTY_STUDENT, FACULTY_ADMIN, STUDENT_ADMIN, PARENT_ADMIN},
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