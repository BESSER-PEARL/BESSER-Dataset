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
edu_Course = Class(name="edu::Course")
edu_Student = Class(name="edu::Student")
edu_Take_Course = Class(name="edu::Take::Course")

# edu_Course class attributes and methods
edu_Course_name: Property = Property(name="name", type=StringType)
edu_Course_id: Property = Property(name="id", type=IntegerType)
edu_Course.attributes={edu_Course_name, edu_Course_id}

# edu_Student class attributes and methods
edu_Student_id: Property = Property(name="id", type=IntegerType)
edu_Student_name: Property = Property(name="name", type=StringType)
edu_Student_date_of_birth: Property = Property(name="date_of_birth", type=DateType)
edu_Student_m_getAge: Method = Method(name="getAge", parameters={}, type=IntegerType)
edu_Student.attributes={edu_Student_date_of_birth, edu_Student_id, edu_Student_name}
edu_Student.methods={edu_Student_m_getAge}

# edu_Take_Course class attributes and methods

# Relationships
student0: BinaryAssociation = BinaryAssociation(
    name="student0",
    ends={
        Property(name="edu_Student", type=edu_Take_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Take_Course", type=edu_Student, multiplicity=Multiplicity(0, 9999))
    }
)
course1: BinaryAssociation = BinaryAssociation(
    name="course1",
    ends={
        Property(name="edu_Course", type=edu_Take_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="edu_Take_Course2", type=edu_Course, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="edu",
    types={edu_Course, edu_Student, edu_Take_Course},
    associations={student0, course1},
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