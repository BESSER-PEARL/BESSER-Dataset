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
skol_Student = Class(name="skol::Student")
skol_Diagram = Class(name="skol::Diagram")
skol_School = Class(name="skol::School")
skol_Classroom = Class(name="skol::Classroom")

# skol_Student class attributes and methods
skol_Student_name: Property = Property(name="name", type=StringType)
skol_Student.attributes={skol_Student_name}

# skol_Diagram class attributes and methods

# skol_School class attributes and methods
skol_School_name: Property = Property(name="name", type=StringType)
skol_School.attributes={skol_School_name}

# skol_Classroom class attributes and methods
skol_Classroom_name: Property = Property(name="name", type=StringType)
skol_Classroom.attributes={skol_Classroom_name}

# Relationships
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="skol_Student", type=skol_Classroom, multiplicity=Multiplicity(1, 1)),
        Property(name="skol_Classroom", type=skol_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
school1: BinaryAssociation = BinaryAssociation(
    name="school1",
    ends={
        Property(name="skol_School", type=skol_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="skol_Diagram", type=skol_School, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classrooms2: BinaryAssociation = BinaryAssociation(
    name="classrooms2",
    ends={
        Property(name="skol_Classroom4", type=skol_School, multiplicity=Multiplicity(1, 1)),
        Property(name="skol_School3", type=skol_Classroom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
friends6: BinaryAssociation = BinaryAssociation(
    name="friends6",
    ends={
        Property(name="skol_Student7", type=skol_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="skol_Student5", type=skol_Student, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="skol",
    types={skol_Student, skol_Diagram, skol_School, skol_Classroom},
    associations={students0, school1, classrooms2, friends6},
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