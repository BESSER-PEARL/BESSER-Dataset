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
PersonsOne_Group = Class(name="PersonsOne::Group")
PersonsOne_Person = Class(name="PersonsOne::Person")
PersonsOne_Student = Class(name="PersonsOne::Student")
Person = Class(name="Person")

# PersonsOne_Group class attributes and methods
PersonsOne_Group_name: Property = Property(name="name", type=StringType)
PersonsOne_Group.attributes={PersonsOne_Group_name}

# PersonsOne_Person class attributes and methods
PersonsOne_Person_name: Property = Property(name="name", type=StringType)
PersonsOne_Person_age: Property = Property(name="age", type=IntegerType)
PersonsOne_Person.attributes={PersonsOne_Person_age, PersonsOne_Person_name}

# PersonsOne_Student class attributes and methods
PersonsOne_Student_grade: Property = Property(name="grade", type=StringType)
PersonsOne_Student.attributes={PersonsOne_Student_grade}

# Person class attributes and methods

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="PersonsOne_Person", type=PersonsOne_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="PersonsOne_Group", type=PersonsOne_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PersonsOne_Student_Person = Generalization(general=Person, specific=PersonsOne_Student)

# Domain Model
domain_model = DomainModel(
    name="PersonsOne",
    types={PersonsOne_Group, PersonsOne_Person, PersonsOne_Student, Person},
    associations={persons0},
    generalizations={gen_PersonsOne_Student_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)