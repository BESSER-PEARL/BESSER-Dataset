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
schol_Classroom = Class(name="schol::Classroom")
schol_Student = Class(name="schol::Student")
schol_Diagram = Class(name="schol::Diagram")
schol_School = Class(name="schol::School")

# schol_Classroom class attributes and methods
schol_Classroom_name: Property = Property(name="name", type=StringType)
schol_Classroom.attributes={schol_Classroom_name}

# schol_Student class attributes and methods
schol_Student_name: Property = Property(name="name", type=StringType)
schol_Student.attributes={schol_Student_name}

# schol_Diagram class attributes and methods

# schol_School class attributes and methods
schol_School_name: Property = Property(name="name", type=StringType)
schol_School.attributes={schol_School_name}

# Relationships
school1: BinaryAssociation = BinaryAssociation(
    name="school1",
    ends={
        Property(name="schol_School", type=schol_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="schol_Diagram", type=schol_School, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classrooms2: BinaryAssociation = BinaryAssociation(
    name="classrooms2",
    ends={
        Property(name="schol_Classroom4", type=schol_School, multiplicity=Multiplicity(1, 1)),
        Property(name="schol_School3", type=schol_Classroom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
friends6: BinaryAssociation = BinaryAssociation(
    name="friends6",
    ends={
        Property(name="schol_Student7", type=schol_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="schol_Student5", type=schol_Student, multiplicity=Multiplicity(0, 9999))
    }
)
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="schol_Student", type=schol_Classroom, multiplicity=Multiplicity(1, 1)),
        Property(name="schol_Classroom", type=schol_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="schol",
    types={schol_Classroom, schol_Student, schol_Diagram, schol_School},
    associations={school1, classrooms2, friends6, students0},
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