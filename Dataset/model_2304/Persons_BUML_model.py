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
Persons_Person = Class(name="Persons::Person", is_abstract=True)
PersonsModel = Class(name="PersonsModel")
Persons_Male = Class(name="Persons::Male")
Person = Class(name="Person")
Persons_Female = Class(name="Persons::Female")
Persons_PersonsModel = Class(name="Persons::PersonsModel")

# Persons_Person class attributes and methods
Persons_Person_fullName: Property = Property(name="fullName", type=StringType)
Persons_Person.attributes={Persons_Person_fullName}

# PersonsModel class attributes and methods

# Persons_Male class attributes and methods

# Person class attributes and methods

# Persons_Female class attributes and methods

# Persons_PersonsModel class attributes and methods

# Relationships
model0: BinaryAssociation = BinaryAssociation(
    name="model0",
    ends={
        Property(name="#", type=Persons_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=PersonsModel, multiplicity=Multiplicity(1, 1))
    }
)
persons1: BinaryAssociation = BinaryAssociation(
    name="persons1",
    ends={
        Property(name="#3", type=Persons_PersonsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Persons_Male_Person = Generalization(general=Person, specific=Persons_Male)
gen_Persons_Female_Person = Generalization(general=Person, specific=Persons_Female)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Persons_Person, PersonsModel, Persons_Male, Person, Persons_Female, Persons_PersonsModel},
    associations={model0, persons1},
    generalizations={gen_Persons_Male_Person, gen_Persons_Female_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)