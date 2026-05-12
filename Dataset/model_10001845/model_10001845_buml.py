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
user = Class(name="user")
admin = Class(name="admin")
teachers = Class(name="teachers")
student = Class(name="student")
claas1 = Class(name="claas1")
subject = Class(name="subject")
exam = Class(name="exam")

# user class attributes and methods
user_user_name: Property = Property(name="user_name", type=StringType)
user_pas: Property = Property(name="pas", type=StringType)
user_sex: Property = Property(name="sex", type=StringType)
user.attributes={user_user_name, user_sex, user_pas}

# admin class attributes and methods

# teachers class attributes and methods

# student class attributes and methods

# claas1 class attributes and methods
claas1_id: Property = Property(name="id", type=IntegerType)
claas1_name: Property = Property(name="name", type=StringType)
claas1.attributes={claas1_name, claas1_id}

# subject class attributes and methods
subject_id: Property = Property(name="id", type=IntegerType)
subject_name: Property = Property(name="name", type=StringType)
subject.attributes={subject_id, subject_name}

# exam class attributes and methods

# Relationships
admin_teachers: BinaryAssociation = BinaryAssociation(
    name="admin_teachers",
    ends={
        Property(name="teachers2", type=teachers, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin3", type=admin, multiplicity=Multiplicity(0, 1))
    }
)
admin_subject: BinaryAssociation = BinaryAssociation(
    name="admin_subject",
    ends={
        Property(name="subject4", type=subject, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin5", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
Class_subject: BinaryAssociation = BinaryAssociation(
    name="Class_subject",
    ends={
        Property(name="subject6", type=subject, multiplicity=Multiplicity(0, 9999)),
        Property(name="class17", type=claas1, multiplicity=Multiplicity(1, 1))
    }
)
Class_student: BinaryAssociation = BinaryAssociation(
    name="Class_student",
    ends={
        Property(name="student8", type=student, multiplicity=Multiplicity(1, 9999)),
        Property(name="class19", type=claas1, multiplicity=Multiplicity(1, 1))
    }
)
student_exam: BinaryAssociation = BinaryAssociation(
    name="student_exam",
    ends={
        Property(name="exam10", type=exam, multiplicity=Multiplicity(1, 9999)),
        Property(name="student11", type=student, multiplicity=Multiplicity(1, 9999))
    }
)
teachers_exam: BinaryAssociation = BinaryAssociation(
    name="teachers_exam",
    ends={
        Property(name="exam12", type=exam, multiplicity=Multiplicity(0, 9999)),
        Property(name="teachers13", type=teachers, multiplicity=Multiplicity(1, 1))
    }
)
teachers_Class: BinaryAssociation = BinaryAssociation(
    name="teachers_Class",
    ends={
        Property(name="class10", type=claas1, multiplicity=Multiplicity(1, 1)),
        Property(name="teachers1", type=teachers, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ZuptcNOqEeehRMl7r1_c5g",
    types={user, admin, teachers, student, claas1, subject, exam},
    associations={admin_teachers, admin_subject, Class_subject, Class_student, student_exam, teachers_exam, teachers_Class},
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