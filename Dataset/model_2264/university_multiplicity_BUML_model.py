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
university_University = Class(name="university::University")
university_Course = Class(name="university::Course")
university_Student = Class(name="university::Student")

# university_University class attributes and methods
university_University_name: Property = Property(name="name", type=StringType)
university_University.attributes={university_University_name}

# university_Course class attributes and methods
university_Course_id: Property = Property(name="id", type=StringType)
university_Course_name: Property = Property(name="name", type=StringType)
university_Course.attributes={university_Course_name, university_Course_id}

# university_Student class attributes and methods
university_Student_id: Property = Property(name="id", type=StringType)
university_Student_name: Property = Property(name="name", type=StringType)
university_Student.attributes={university_Student_name, university_Student_id}

# Relationships
student3: BinaryAssociation = BinaryAssociation(
    name="student3",
    ends={
        Property(name="course", type=university_Student, multiplicity=Multiplicity(5, 7)),
        Property(name="Student", type=university_Course, multiplicity=Multiplicity(1, 1))
    }
)
courses0: BinaryAssociation = BinaryAssociation(
    name="courses0",
    ends={
        Property(name="university_Course", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University", type=university_Course, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
students1: BinaryAssociation = BinaryAssociation(
    name="students1",
    ends={
        Property(name="university_Student", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University2", type=university_Student, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
course4: BinaryAssociation = BinaryAssociation(
    name="course4",
    ends={
        Property(name="Course", type=university_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=university_Course, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="university",
    types={university_University, university_Course, university_Student},
    associations={student3, courses0, students1, course4},
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