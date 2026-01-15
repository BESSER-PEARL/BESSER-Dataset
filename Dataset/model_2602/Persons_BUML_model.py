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

# Enumerations
GenderType: Enumeration = Enumeration(
    name="GenderType",
    literals={
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female")
    }
)

# Classes
Persons_Persons = Class(name="Persons::Persons")
Persons_Person = Class(name="Persons::Person")

# Persons_Persons class attributes and methods

# Persons_Person class attributes and methods
Persons_Person_lastname: Property = Property(name="lastname", type=StringType)
Persons_Person_gender: Property = Property(name="gender", type=StringType)
Persons_Person_firstname: Property = Property(name="firstname", type=StringType)
Persons_Person.attributes={Persons_Person_lastname, Persons_Person_gender, Persons_Person_firstname}

# Relationships
list1: BinaryAssociation = BinaryAssociation(
    name="list1",
    ends={
        Property(name="Persons", type=Persons_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=Persons_Persons, multiplicity=Multiplicity(1, 1))
    }
)
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="Person", type=Persons_Persons, multiplicity=Multiplicity(1, 1)),
        Property(name="list", type=Persons_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Persons",
    types={Persons_Persons, Persons_Person, GenderType},
    associations={list1, persons0},
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