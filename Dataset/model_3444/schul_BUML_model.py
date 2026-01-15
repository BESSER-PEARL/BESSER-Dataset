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
schul_School = Class(name="schul::School")
schul_Classroom = Class(name="schul::Classroom")
schul_Student = Class(name="schul::Student")
schul_Diagram = Class(name="schul::Diagram")

# schul_School class attributes and methods
schul_School_name: Property = Property(name="name", type=StringType)
schul_School.attributes={schul_School_name}

# schul_Classroom class attributes and methods
schul_Classroom_name: Property = Property(name="name", type=StringType)
schul_Classroom.attributes={schul_Classroom_name}

# schul_Student class attributes and methods
schul_Student_name: Property = Property(name="name", type=StringType)
schul_Student.attributes={schul_Student_name}

# schul_Diagram class attributes and methods

# Relationships
school1: BinaryAssociation = BinaryAssociation(
    name="school1",
    ends={
        Property(name="schul_School", type=schul_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="schul_Diagram", type=schul_School, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classrooms2: BinaryAssociation = BinaryAssociation(
    name="classrooms2",
    ends={
        Property(name="schul_Classroom4", type=schul_School, multiplicity=Multiplicity(1, 1)),
        Property(name="schul_School3", type=schul_Classroom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
friends6: BinaryAssociation = BinaryAssociation(
    name="friends6",
    ends={
        Property(name="schul_Student7", type=schul_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="schul_Student5", type=schul_Student, multiplicity=Multiplicity(0, 9999))
    }
)
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="schul_Student", type=schul_Classroom, multiplicity=Multiplicity(1, 1)),
        Property(name="schul_Classroom", type=schul_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="schul",
    types={schul_School, schul_Classroom, schul_Student, schul_Diagram},
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