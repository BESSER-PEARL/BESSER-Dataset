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
Persons_Male = Class(name="Persons::Male")
Person = Class(name="Person")
Persons_Female = Class(name="Persons::Female")
Persons_PersonsModel = Class(name="Persons::PersonsModel")
Persons_Person = Class(name="Persons::Person")
PersonsModel = Class(name="PersonsModel")
Persons_LocaledElement = Class(name="Persons::LocaledElement", is_abstract=True)
Persons_Employee = Class(name="Persons::Employee")

# Persons_Male class attributes and methods
Persons_Male_age: Property = Property(name="age", type=IntegerType)
Persons_Male.attributes={Persons_Male_age}

# Person class attributes and methods

# Persons_Female class attributes and methods
Persons_Female_age: Property = Property(name="age", type=IntegerType)
Persons_Female.attributes={Persons_Female_age}

# Persons_PersonsModel class attributes and methods

# Persons_Person class attributes and methods
Persons_Person_fullName: Property = Property(name="fullName", type=StringType)
Persons_Person.attributes={Persons_Person_fullName}

# PersonsModel class attributes and methods

# Persons_LocaledElement class attributes and methods

# Persons_Employee class attributes and methods

# Relationships
persons1: BinaryAssociation = BinaryAssociation(
    name="persons1",
    ends={
        Property(name="Person", type=Persons_PersonsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_PersonsModel", type=Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model0: BinaryAssociation = BinaryAssociation(
    name="model0",
    ends={
        Property(name="PersonsModel", type=Persons_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_Person", type=PersonsModel, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Persons_Male_Person = Generalization(general=Person, specific=Persons_Male)
gen_Persons_Female_Person = Generalization(general=Person, specific=Persons_Female)
gen_Persons_Employee_Person = Generalization(general=Person, specific=Persons_Employee)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Persons_Male, Person, Persons_Female, Persons_PersonsModel, Persons_Person, PersonsModel, Persons_LocaledElement, Persons_Employee},
    associations={persons1, model0},
    generalizations={gen_Persons_Male_Person, gen_Persons_Female_Person, gen_Persons_Employee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)