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
education_Student = Class(name="education::Student")
education_Course = Class(name="education::Course")
education_School = Class(name="education::School")

# education_Student class attributes and methods
education_Student_name: Property = Property(name="name", type=StringType)
education_Student.attributes={education_Student_name}

# education_Course class attributes and methods
education_Course_name: Property = Property(name="name", type=StringType)
education_Course.attributes={education_Course_name}

# education_School class attributes and methods
education_School_name: Property = Property(name="name", type=StringType)
education_School_address: Property = Property(name="address", type=StringType)
education_School_phone: Property = Property(name="phone", type=StringType)
education_School.attributes={education_School_name, education_School_phone, education_School_address}

# Relationships
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="education_Student", type=education_School, multiplicity=Multiplicity(1, 1)),
        Property(name="education_School", type=education_Student, multiplicity=Multiplicity(0, 9999))
    }
)
courses1: BinaryAssociation = BinaryAssociation(
    name="courses1",
    ends={
        Property(name="education_Course", type=education_School, multiplicity=Multiplicity(1, 1)),
        Property(name="education_School2", type=education_Course, multiplicity=Multiplicity(0, 9999))
    }
)
schools3: BinaryAssociation = BinaryAssociation(
    name="schools3",
    ends={
        Property(name="education_School5", type=education_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="education_Student4", type=education_School, multiplicity=Multiplicity(1, 9999))
    }
)
courses6: BinaryAssociation = BinaryAssociation(
    name="courses6",
    ends={
        Property(name="education_Course8", type=education_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="education_Student7", type=education_Course, multiplicity=Multiplicity(0, 9999))
    }
)
students9: BinaryAssociation = BinaryAssociation(
    name="students9",
    ends={
        Property(name="education_Student11", type=education_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="education_Course10", type=education_Student, multiplicity=Multiplicity(0, 9999))
    }
)
school12: BinaryAssociation = BinaryAssociation(
    name="school12",
    ends={
        Property(name="education_School14", type=education_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="education_Course13", type=education_School, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="education",
    types={education_Student, education_Course, education_School},
    associations={students0, courses1, schools3, courses6, students9, school12},
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