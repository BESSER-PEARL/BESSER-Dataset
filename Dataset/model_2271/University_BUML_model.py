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
Univerity_Courses = Class(name="Univerity::Courses")
Univerity_University = Class(name="Univerity::University")
Univerity_Person = Class(name="Univerity::Person")

# Univerity_Courses class attributes and methods
Univerity_Courses_Name: Property = Property(name="Name", type=StringType)
Univerity_Courses_CFU: Property = Property(name="CFU", type=IntegerType)
Univerity_Courses_Semester: Property = Property(name="Semester", type=StringType)
Univerity_Courses.attributes={Univerity_Courses_Semester, Univerity_Courses_Name, Univerity_Courses_CFU}

# Univerity_University class attributes and methods

# Univerity_Person class attributes and methods
Univerity_Person_Name: Property = Property(name="Name", type=StringType)
Univerity_Person_Email: Property = Property(name="Email", type=StringType)
Univerity_Person.attributes={Univerity_Person_Email, Univerity_Person_Name}

# Relationships
relatives8: BinaryAssociation = BinaryAssociation(
    name="relatives8",
    ends={
        Property(name="Univerity_Person9", type=Univerity_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_Person7", type=Univerity_Person, multiplicity=Multiplicity(0, 1))
    }
)
Courses10: BinaryAssociation = BinaryAssociation(
    name="Courses10",
    ends={
        Property(name="Univerity_Courses11", type=Univerity_University, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_University", type=Univerity_Courses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links1: BinaryAssociation = BinaryAssociation(
    name="links1",
    ends={
        Property(name="Univerity_Courses", type=Univerity_Courses, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_Courses0", type=Univerity_Courses, multiplicity=Multiplicity(0, 9999))
    }
)
Professor2: BinaryAssociation = BinaryAssociation(
    name="Professor2",
    ends={
        Property(name="Univerity_Person", type=Univerity_Courses, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_Courses3", type=Univerity_Person, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Student4: BinaryAssociation = BinaryAssociation(
    name="Student4",
    ends={
        Property(name="Univerity_Person6", type=Univerity_Courses, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_Courses5", type=Univerity_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Univerity",
    types={Univerity_Courses, Univerity_University, Univerity_Person},
    associations={relatives8, Courses10, links1, Professor2, Student4},
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