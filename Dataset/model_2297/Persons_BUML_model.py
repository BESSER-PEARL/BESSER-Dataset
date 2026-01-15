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
Persons_PersonRegister = Class(name="Persons::PersonRegister")
Persons_Person = Class(name="Persons::Person", is_abstract=True)

# Persons_Male class attributes and methods

# Person class attributes and methods

# Persons_Female class attributes and methods

# Persons_PersonRegister class attributes and methods

# Persons_Person class attributes and methods
Persons_Person_name: Property = Property(name="name", type=StringType)
Persons_Person_birthday: Property = Property(name="birthday", type=DateType)
Persons_Person.attributes={Persons_Person_birthday, Persons_Person_name}

# Relationships
personsInverse1: BinaryAssociation = BinaryAssociation(
    name="personsInverse1",
    ends={
        Property(name="PersonRegister", type=Persons_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=Persons_PersonRegister, multiplicity=Multiplicity(0, 1))
    }
)
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="Person", type=Persons_PersonRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="personsInverse", type=Persons_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Persons_Male_Person = Generalization(general=Person, specific=Persons_Male)
gen_Persons_Female_Person = Generalization(general=Person, specific=Persons_Female)

# Domain Model
domain_model = DomainModel(
    name="Persons",
    types={Persons_Male, Person, Persons_Female, Persons_PersonRegister, Persons_Person},
    associations={personsInverse1, persons0},
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