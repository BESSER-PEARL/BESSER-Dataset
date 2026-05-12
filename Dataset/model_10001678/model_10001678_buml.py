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
Student = Class(name="Student")
Teacher = Class(name="Teacher")
Grade = Class(name="Grade")
Subject = Class(name="Subject")
Note = Class(name="Note")
Schedule = Class(name="Schedule")

# Student class attributes and methods
Student_phone: Property = Property(name="phone", type=StringType)
Student_email: Property = Property(name="email", type=StringType)
Student_surname: Property = Property(name="surname", type=StringType)
Student_name: Property = Property(name="name", type=StringType)
Student.attributes={Student_surname, Student_phone, Student_name, Student_email}

# Teacher class attributes and methods
Teacher_name: Property = Property(name="name", type=StringType)
Teacher_surname: Property = Property(name="surname", type=StringType)
Teacher_email: Property = Property(name="email", type=StringType)
Teacher_phone: Property = Property(name="phone", type=StringType)
Teacher.attributes={Teacher_surname, Teacher_name, Teacher_phone, Teacher_email}

# Grade class attributes and methods
Grade_name: Property = Property(name="name", type=StringType)
Grade.attributes={Grade_name}

# Subject class attributes and methods

# Note class attributes and methods

# Schedule class attributes and methods

# Relationships
Grade_Teacher: BinaryAssociation = BinaryAssociation(
    name="Grade_Teacher",
    ends={
        Property(name="teacher0", type=Teacher, multiplicity=Multiplicity(0, 1)),
        Property(name="grades1", type=Grade, multiplicity=Multiplicity(0, 1))
    }
)
Student_Grade: BinaryAssociation = BinaryAssociation(
    name="Student_Grade",
    ends={
        Property(name="grade2", type=Grade, multiplicity=Multiplicity(1, 1)),
        Property(name="students3", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
Student_Subject: BinaryAssociation = BinaryAssociation(
    name="Student_Subject",
    ends={
        Property(name="subjects4", type=Subject, multiplicity=Multiplicity(0, 1)),
        Property(name="student5", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
Note_Subject: BinaryAssociation = BinaryAssociation(
    name="Note_Subject",
    ends={
        Property(name="subject6", type=Subject, multiplicity=Multiplicity(1, 1)),
        Property(name="notes7", type=Note, multiplicity=Multiplicity(0, 1))
    }
)
Schedule_Student: BinaryAssociation = BinaryAssociation(
    name="Schedule_Student",
    ends={
        Property(name="student8", type=Student, multiplicity=Multiplicity(1, 1)),
        Property(name="schedule9", type=Schedule, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_OIapALpiEeehVczkwiTSNA",
    types={Student, Teacher, Grade, Subject, Note, Schedule},
    associations={Grade_Teacher, Student_Grade, Student_Subject, Note_Subject, Schedule_Student},
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