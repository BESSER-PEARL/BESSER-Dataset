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
myDsl_Person = Class(name="myDsl::Person")
myDsl_Student = Class(name="myDsl::Student")
Person = Class(name="Person")
myDsl_Teacher = Class(name="myDsl::Teacher")
myDsl_SchoolModel = Class(name="myDsl::SchoolModel")
myDsl_School = Class(name="myDsl::School")

# myDsl_Person class attributes and methods
myDsl_Person_name: Property = Property(name="name", type=StringType)
myDsl_Person.attributes={myDsl_Person_name}

# myDsl_Student class attributes and methods
myDsl_Student_registrationNum: Property = Property(name="registrationNum", type=IntegerType)
myDsl_Student.attributes={myDsl_Student_registrationNum}

# Person class attributes and methods

# myDsl_Teacher class attributes and methods

# myDsl_SchoolModel class attributes and methods

# myDsl_School class attributes and methods
myDsl_School_name: Property = Property(name="name", type=StringType)
myDsl_School.attributes={myDsl_School_name}

# Relationships
persons1: BinaryAssociation = BinaryAssociation(
    name="persons1",
    ends={
        Property(name="myDsl_Person", type=myDsl_School, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_School2", type=myDsl_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teachers3: BinaryAssociation = BinaryAssociation(
    name="teachers3",
    ends={
        Property(name="myDsl_Teacher", type=myDsl_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Student", type=myDsl_Teacher, multiplicity=Multiplicity(0, 9999))
    }
)
schools0: BinaryAssociation = BinaryAssociation(
    name="schools0",
    ends={
        Property(name="myDsl_School", type=myDsl_SchoolModel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SchoolModel", type=myDsl_School, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myDsl_Student_Person = Generalization(general=Person, specific=myDsl_Student)
gen_myDsl_Teacher_Person = Generalization(general=Person, specific=myDsl_Teacher)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Person, myDsl_Student, Person, myDsl_Teacher, myDsl_SchoolModel, myDsl_School},
    associations={persons1, teachers3, schools0},
    generalizations={gen_myDsl_Student_Person, gen_myDsl_Teacher_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)